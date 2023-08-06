from __future__ import annotations

from typing import Final, Optional, Any
from threading import Lock, Thread
from logging import LogRecord, StreamHandler

import time
import sys

from .log import Log
from .log_severity import LogSeverity
from ..networking import NetworkManager
from ..networking import RequestType


class _LoggerUploadWorker(Thread):

    def __init__(self, waitTime: int) -> None:
        super().__init__()

        self.setDaemon(True)
        self.setName("LoggerUploadWorker")

        self.__waitTime: Final = waitTime

    def run(self) -> None:
        while True:
            customLogHandler = LogHandler.instance()

            # Check if logger is attached to a experiment
            if customLogHandler.currentExperimentId is None:
                time.sleep(self.__waitTime)
                continue

            # Get the timestamp of the last log
            lastLogTimestamp = customLogHandler.lastLogTimestamp
            if lastLogTimestamp is None:
                time.sleep(self.__waitTime)
                continue

            # Calculate diff to current time
            timeDiff = time.time() - lastLogTimestamp

            # If it is more than the threshold flush the logs to Coretex, otherwise wait
            if timeDiff >= self.__waitTime:
                customLogHandler.flushLogs()
            else:
                time.sleep(self.__waitTime - timeDiff)


class LogHandler(StreamHandler):

    __instanceLock = Lock()
    __instance: Optional[LogHandler] = None

    MAX_LOG_QUEUE_SIZE = 10
    MAX_WAIT_TIME_BEFORE_UPDATE = 5  # in seconds

    @staticmethod
    def instance() -> LogHandler:
        if LogHandler.__instance is None:
            with LogHandler.__instanceLock:
                if LogHandler.__instance is None:
                    LogHandler.__instance = LogHandler(sys.stdout)

        return LogHandler.__instance

    def __init__(self, stream: Any) -> None:
        super().__init__(stream)

        self.__lock = Lock()
        self.__pendingLogs: list[Log] = []
        self.__uploadWorker = _LoggerUploadWorker(
            LogHandler.MAX_WAIT_TIME_BEFORE_UPDATE
        )
        self.currentExperimentId: Optional[int] = None
        self.severity = LogSeverity.info

        self.__uploadWorker.start()

    @property
    def lastLogTimestamp(self) -> Optional[float]:
        if len(self.__pendingLogs) == 0:
            return None

        return self.__pendingLogs[-1].timestamp

    def __restartUploadWorker(self) -> None:
        if self.__uploadWorker.is_alive():
            raise RuntimeError(">> [Coretex] Upload worker is already running")

        self.__uploadWorker = _LoggerUploadWorker(
            LogHandler.MAX_WAIT_TIME_BEFORE_UPDATE
        )
        self.__uploadWorker.start()

    def __shouldUploadLogs(self) -> bool:
        # Logs are sent in batches of #MAX_LOG_QUEUE_SIZE
        # Logs can only be sent to server if there is a experiment in progress
        return (len(self.__pendingLogs) >= LogHandler.MAX_LOG_QUEUE_SIZE and
                self.currentExperimentId is not None)

    def __uploadLogs(self) -> None:
        if len(self.__pendingLogs) == 0:
            return

        if self.currentExperimentId is None:
            return

        response = NetworkManager.instance().genericJSONRequest(
            endpoint = "model-queue/add-console-log",
            requestType = RequestType.post,
            parameters = {
                "model_queue_id": self.currentExperimentId,
                "logs": [log.encode() for log in self.__pendingLogs]
            }
        )

        # Only clear logs if they were successfully uploaded to coretex
        if not response.hasFailed():
            self.__pendingLogs.clear()

    def emit(self, record: LogRecord) -> None:
        super().emit(record)

        # Logs from library that is being used for making api requests is causing workspace to freeze because
        # logs inside requests library are going to be called while api request for log in coretexpylib is not finished
        # so request will never be done and it will enter infinite loop
        IGNORED_LOGGERS = [
            "urllib3.connectionpool"
        ]

        if record.name in IGNORED_LOGGERS:
            return

        with self.__lock:
            if not self.__uploadWorker.is_alive():
                self.__restartUploadWorker()

            severity = LogSeverity.fromStd(record.levelno)
            log = Log.create(record.message, severity)

            self.__pendingLogs.append(log)

            if self.__shouldUploadLogs() and not record.name in IGNORED_LOGGERS:
                self.__uploadLogs()

    def flushLogs(self) -> None:
        with self.__lock:
            self.__uploadLogs()

    def reset(self) -> None:
        with self.__lock:
            self.currentExperimentId = None
