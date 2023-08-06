import time
import logging

from ..threading import StoppableThread
from ..coretex import Experiment


class Heartbeat(StoppableThread):

    def __init__(self, experiment: Experiment, heartbeatRate: int = 10):
        super(Heartbeat, self).__init__()

        # Don't wait for this thread to finish once the
        # non daemon threads have exited
        self.setDaemon(True)
        self.setName("Heartbeat")

        if heartbeatRate < 1:
            raise ValueError(">> [Coretex] updateInterval must be expressed as an integer of seconds")

        self.__experiment = experiment
        self.__heartbeatRate = heartbeatRate

    def stop(self) -> None:
        logging.debug(">> [Coretex] Stopping the heartbeat...")

        return super().stop()

    def run(self) -> None:
        while not self.isStopped():
            for _ in range(self.__heartbeatRate):
                if self.isStopped():
                    return

                time.sleep(1)

            # Check whether the thread is stopped again in case it was stopped while sleeping
            if self.isStopped():
                return

            status = self.__experiment.status

            lastStatusMessage = self.__experiment.getLastStatusMessage()
            if lastStatusMessage is None:
                continue

            logging.debug(">> [Coretex] Heartbeat")
            self.__experiment.updateStatus(status, lastStatusMessage)

        logging.debug(">> [Coretex] Stopped the heartbeat")
