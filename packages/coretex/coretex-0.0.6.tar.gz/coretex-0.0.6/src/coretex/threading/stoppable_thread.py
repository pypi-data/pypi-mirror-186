from threading import Thread, Event


class StoppableThread(Thread):

    def __init__(self) -> None:
        super(StoppableThread, self).__init__()

        self.__stop = Event()

    def stop(self) -> None:
        self.__stop.set()

    def isStopped(self) -> bool:
        return self.__stop.is_set()
