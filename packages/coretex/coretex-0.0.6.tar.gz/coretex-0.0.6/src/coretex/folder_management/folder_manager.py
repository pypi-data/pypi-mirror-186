from __future__ import annotations

from pathlib import Path
from typing import Optional, Final
from threading import Lock

import os
import shutil


class FolderManager:

    __instanceLock = Lock()
    __instance: Optional[FolderManager] = None

    @classmethod
    def instance(cls) -> FolderManager:
        if cls.__instance is None:
            with cls.__instanceLock:
                if cls.__instance is None:
                    cls.__instance = cls()

        return cls.__instance

    def __init__(self) -> None:
        self.__root: Final = Path(os.path.expanduser("~/coretex"))

        # These paths are str paths for backwards compatibility
        self.itemsFolder: Final = str(self.__createFolder("items"))
        self.modelsFolder: Final = str(self.__createFolder("models"))
        self.temp: Final = str(self.__createFolder("temp"))

        # These paths are pathlib.Paths
        # pathlib is a std python library for handling paths
        self.datasetsFolder: Final = self.__createFolder("datasets")
        self.cache: Final = self.__createFolder("cache")
        self.logs: Final = self.__createFolder("logs")
        self.environments: Final = self.__createFolder("environments")

        self.__artifactsFolder: Final = self.__createFolder("artifacts")

    def createTempFolder(self, name: str) -> str:
        tempFolderPath = os.path.join(self.temp, name)

        if os.path.exists(tempFolderPath):
            raise FileExistsError

        os.mkdir(tempFolderPath)
        return tempFolderPath

    def getTempFolder(self, name: str) -> str:
        return os.path.join(self.temp, name)

    def getArtifactsFolder(self, experimentId: int) -> Path:
        return self.__artifactsFolder / str(experimentId)

    def clearTempFiles(self) -> None:
        self.__clearDirectory(self.temp)
        self.__clearDirectory(self.__artifactsFolder)

    def __createFolder(self, name: str) -> Path:
        path = self.__root / name

        if not path.exists():
            path.mkdir(parents = True, exist_ok = True)

        return path

    def __clearDirectory(self, path: Path | str) -> None:
        for root, directories, files in os.walk(path):
            for file in files:
                os.unlink(os.path.join(root, file))

            for directory in directories:
                shutil.rmtree(os.path.join(root, directory))
