from typing import TypeVar, Generic, Final
from pathlib import Path

import logging

from .item import Item


ItemDataType = TypeVar("ItemDataType")


class LocalItem(Generic[ItemDataType], Item[ItemDataType]):

    def __init__(self, path: Path) -> None:
        super().__init__()

        self.name: Final = path.stem
        self._path: Final = path

    @property
    def path(self) -> str:
        return str(self._path.parent / self._path.stem)

    @property
    def zipPath(self) -> str:
        return str(self._path)

    def download(self, ignoreCache: bool = False) -> None:
        logging.warning(">> [Coretex] Local item cannot be downloaded")

    def load(self) -> ItemDataType:
        return super().load()
