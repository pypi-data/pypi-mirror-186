from __future__ import annotations

from typing import TypeVar, Generic, Type, Generator, Optional
from pathlib import Path

import logging
import zipfile

from .dataset import Dataset
from ..item import LocalItem, AnyLocalItem


ItemType = TypeVar("ItemType", bound = "LocalItem")
ItemGenerator = Generator[ItemType, None, None]


def _generateZippedItems(path: Path, itemClass: Type[ItemType]) -> Generator[ItemType, None, None]:
    for itemPath in path.glob("*"):
        if not zipfile.is_zipfile(itemPath):
            continue

        yield itemClass(itemPath)


class LocalDataset(Generic[ItemType], Dataset[ItemType]):

    def __init__(self, path: Path, itemClass: Type[ItemType], generator: Optional[ItemGenerator] = None) -> None:
        if generator is None:
            generator = _generateZippedItems(path, itemClass)

        self.__path = path

        self.name = path.stem
        self.items = list(generator)

    @staticmethod
    def default(path: Path) -> LocalDataset:
        return LocalDataset(path, LocalItem)

    @staticmethod
    def custom(path: Path, generator: ItemGenerator) -> LocalDataset:
        return LocalDataset(path, AnyLocalItem, generator)

    @property
    def path(self) -> Path:
        return self.__path

    def download(self, ignoreCache: bool = False) -> None:
        logging.warning(">> [Coretex] Local dataset cannot be downloaded")
