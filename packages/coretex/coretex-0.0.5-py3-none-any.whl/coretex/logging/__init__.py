from pathlib import Path

import logging

from .logger import LogHandler, LogSeverity
from ..utils import DATE_FORMAT


def initializeLogger(logLevel: int, logPath: Path) -> None:
    logging.basicConfig(
        level = LogSeverity(logLevel).stdSeverity,
        format = "{levelname}: {message}",
        style = "{",
        datefmt = DATE_FORMAT,
        force = True,
        handlers = [
            LogHandler.instance(),
            logging.FileHandler(logPath)
        ]
    )
