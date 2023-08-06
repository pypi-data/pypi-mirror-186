from typing import Final, TypeVar, Type

import sys
import logging

from ..coretex import Experiment
from ..folder_management import FolderManager
from ..logging import LogHandler

T = TypeVar("T", bound = "WorkspaceCallback")


class WorkspaceCallback:

    def __init__(self, experiment: Experiment) -> None:
        self._experiment: Final = experiment

    @classmethod
    def create(cls: Type[T], experimentId: int) -> T:
        experiment = Experiment.fetchById(experimentId)
        if experiment is None:
            raise ValueError

        return cls(experiment)

    def onSuccess(self) -> None:
        pass

    def onException(self, exception: BaseException) -> None:
        pass

    def onNetworkConnectionLost(self) -> None:
        FolderManager.instance().clearTempFiles()

        sys.exit()

    def onCleanUp(self) -> None:
        logging.info("Experiment execution finished")
        LogHandler.instance().flushLogs()
        LogHandler.instance().reset()

        FolderManager.instance().clearTempFiles()
