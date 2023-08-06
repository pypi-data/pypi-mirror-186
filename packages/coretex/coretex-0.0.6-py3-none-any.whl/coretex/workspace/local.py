from typing import Any, Dict, List, Tuple

import json
import logging
import traceback

from tap import Tap

from .base import WorkspaceCallback
from ..coretex import Experiment, ExperimentStatus
from ..networking import NetworkManager


class LocalWorkspaceCallback(WorkspaceCallback):

    def onSuccess(self) -> None:
        super().onSuccess()

        self._experiment.updateStatus(ExperimentStatus.completedWithSuccess)

    def onException(self, exception: BaseException) -> None:
        super().onException(exception)

        self._experiment.updateStatus(ExperimentStatus.completedWithError)

        exceptionStackTrace = "".join(traceback.format_exception(
            type(exception),
            exception,
            exception.__traceback__
        ))

        for line in exceptionStackTrace.split("\n"):
            if len(line.strip()) == 0:
                continue

            logging.fatal(line)


class LocalArgumentParser(Tap):

    username: str
    password: str

    datasetId: int
    subProjectId: int
    description: str

    def configure(self) -> None:
        self.add_argument("--username", type = str)
        self.add_argument("--password", type = str)

        self.add_argument("--datasetId", type = int)
        self.add_argument("--subProjectId", type = int)
        self.add_argument("--description", nargs = "?", type = str, default = "")


def loadLocalParameters() -> List[Dict[str, Any]]:
    with open("experiment.config", "r") as configFile:
        configContent = json.load(configFile)

        if "parameters" in configContent:
            parameters: List[Dict[str, Any]] = configContent["parameters"]

    return parameters


def processLocal() -> Tuple[int, WorkspaceCallback]:
    parser = LocalArgumentParser().parse_args()

    NetworkManager.instance().authenticate(parser.username, parser.password)
    parameters = loadLocalParameters()

    experiment = Experiment.startCustomExperiment(
        parser.datasetId,
        parser.subProjectId,
        # Dummy Local service ID, hardcoded as it is only a temporary solution,
        # backend will add a new ExperimentType (local) which does not require a specific
        # machine to run
        43,
        parser.description,
        parameters=parameters
    )

    if experiment is None:
        raise RuntimeError(">> [Coretex] Failed to create experiment")

    experiment.updateStatus(ExperimentStatus.preparingToStart)

    return experiment.id, LocalWorkspaceCallback(experiment)
