from enum import Enum


class ExperimentStatus(Enum):

    queued = 1
    preparingToStart = 2
    inProgress = 3
    completedWithSuccess = 4
    completedWithError = 5
    stopped = 6
    stopping = 7

    @property
    def defaultMessage(self) -> str:
        if self == ExperimentStatus.preparingToStart:
            return "Preparing to start the experiment."

        if self == ExperimentStatus.completedWithSuccess:
            return "Experiment completed successfully."

        if self == ExperimentStatus.completedWithError:
            return "Experiment execution was interrupted due to an error. View experiment console for more details."

        if self == ExperimentStatus.stopped:
            return "Experiment execution was stopped by request from the user."

        if self == ExperimentStatus.stopping:
            return "Stopping the experiment."

        raise ValueError(f">> [MLService] {self.name} has no default message")

    @property
    def isFinal(self) -> bool:
        """
            Returns true if a status is a final status for a experiment
        """

        return (
                self == ExperimentStatus.completedWithSuccess or
                self == ExperimentStatus.completedWithError or
                self == ExperimentStatus.stopped
        )
