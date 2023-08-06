from __future__ import annotations

from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from zipfile import BadZipFile, ZipFile
from pathlib import Path

import os
import shutil


ItemDataType = TypeVar("ItemDataType")


class Item(ABC, Generic[ItemDataType]):

    """
        Represents the Item object from Coretex.ai
    """

    name: str

    @property
    @abstractmethod
    def path(self) -> str:
        pass

    @property
    @abstractmethod
    def zipPath(self) -> str:
        pass

    @abstractmethod
    def download(self, ignoreCache: bool = False) -> None:
        pass

    def __unzipItem(self) -> None:
        if os.path.exists(self.path):
            shutil.rmtree(self.path)

        with ZipFile(self.zipPath) as zipFile:
            zipFile.extractall(self.path)

    def unzip(self, ignoreCache: bool = False) -> None:
        if os.path.exists(self.path) and not ignoreCache:
            return

        try:
            self.__unzipItem()
        except BadZipFile:
            # Delete invalid zip file
            os.unlink(self.zipPath)

            # Re-download
            self.download()

            # Try to unzip - if it fails again it should crash
            self.__unzipItem()

    @abstractmethod
    def load(self) -> ItemDataType:
        pass

    def joinPath(self, other: Path | str) -> Path:
        if isinstance(other, str):
            other = Path(other)

        return Path(self.path) / other
