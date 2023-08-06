from __future__ import annotations

from typing import Any, Callable, Final, Optional
from concurrent.futures import ThreadPoolExecutor, Future

from ..utils import ConsoleProgressBar


class MultithreadedDataProcessor:

    def __init__(self, data: list[Any], singleElementProcessor: Callable[[Any], None], threadCount: int = 1, title: Optional[str] = None) -> None:
        self.__data: Final = data
        self.__singleElementProcessor: Final = singleElementProcessor
        self.__threadCount: Final = threadCount
        self.__progressBar: Final = ConsoleProgressBar(len(data), "" if title is None else title)

    def process(self) -> None:
        futures: list[Future] = []

        with ThreadPoolExecutor(max_workers = self.__threadCount) as pool:
            for element in self.__data:
                future = pool.submit(self.__singleElementProcessor, element)
                future.add_done_callback(lambda _: self.__progressBar.update())
                futures.append(future)

        self.__progressBar.finish()

        for future in futures:
            exception = future.exception()
            if exception is not None:
                raise exception
