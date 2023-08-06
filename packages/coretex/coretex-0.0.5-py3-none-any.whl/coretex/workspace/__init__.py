from typing import Callable, Optional, Type, TypeVar
from enum import IntEnum
from datetime import datetime

import logging

from .remote import processRemote
from .local import processLocal
from .heartbeat import Heartbeat
from ..context import ExperimentContext
from ..coretex import ExperimentStatus, NetworkDataset
from ..logging import LogHandler, initializeLogger, LogSeverity
from ..networking import RequestFailedError
from ..folder_management import FolderManager


DatasetType = TypeVar("DatasetType", bound = "NetworkDataset")


class ExecutionType(IntEnum):
     # TODO: NYI on backend

     local = 1
     remote = 2


def _prepareForExecution(experimentId: int, datasetType: Optional[Type[DatasetType]] = None) -> None:
     context = ExperimentContext.create(experimentId, datasetType)

     logPath = FolderManager.instance().logs / f"{experimentId}.log"
     customLogHandler = LogHandler.instance()
     customLogHandler.currentExperimentId = experimentId

     # if logLevel exists apply it, otherwise default to info
     if not "logLevel" in context.config:
          initializeLogger(LogSeverity.info, logPath)
     else:
          initializeLogger(context.config["logLevel"], logPath)

     context.experiment.updateStatus(
          status = ExperimentStatus.inProgress,
          message = "Executing workspace."
     )

     logging.info("Experiment execution started")

     heartbeat = Heartbeat(context.experiment)
     heartbeat.start()


def initializeWorkspace(
     mainFunction: Callable[[ExperimentContext], None],
     datasetType: Optional[Type[DatasetType]] = None
) -> None:

     try:
          experimentId, callback = processRemote()
     except:
          experimentId, callback = processLocal()

     try:
          _prepareForExecution(experimentId, datasetType)
          mainFunction(ExperimentContext.instance())

          callback.onSuccess()
     except RequestFailedError:
          callback.onNetworkConnectionLost()
     except BaseException as ex:
          callback.onException(ex)

          raise
     finally:
          callback.onCleanUp()
