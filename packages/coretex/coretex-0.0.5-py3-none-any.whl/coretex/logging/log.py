from __future__ import annotations

from typing import Final

import time
import termcolor

from .log_severity import LogSeverity
from ..utils import mathematicalRound
from ..codable import Codable, KeyDescriptor


class Log(Codable):

    timestamp: float
    message: str
    severity: LogSeverity

    def __init__(self) -> None:
        super().__init__()

        # type is deprecated, leaving this here until backend no longer requires it
        self.type: Final = 1

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()

        descriptors["message"] = KeyDescriptor("content")
        descriptors["severity"] = KeyDescriptor(pythonType = LogSeverity)

        return descriptors

    @classmethod
    def create(cls, message: str, severity: LogSeverity) -> Log:
        log = cls()

        log.timestamp = mathematicalRound(time.time(), 6)
        log.message = Log.__createMessage(message, severity)
        log.severity = severity

        return log

    @staticmethod
    def __createMessage(message: str, severity: LogSeverity) -> str:
        message = f"{severity.prefix}: {message}"
        message = termcolor.colored(message, severity.color)

        return message
