from typing import Optional, Type, TypeVar, Generic, List, Dict
from datetime import datetime
from pathlib import Path

import os

from .dataset import Dataset
from ..item import NetworkItem
from ...codable import KeyDescriptor
from ...networking import NetworkObject, DEFAULT_PAGE_SIZE
from ...threading import MultithreadedDataProcessor
from ...folder_management import FolderManager


DatasetType = TypeVar("DatasetType", bound = "NetworkDataset")
ItemType = TypeVar("ItemType", bound = "NetworkItem")


class NetworkDataset(Generic[ItemType], Dataset[ItemType], NetworkObject):
    """
        Represents the Dataset object from Coretex.ai
    """

    createdOn: datetime
    createdById: str
    isLocked: bool

    def __init__(self) -> None:
        pass

    @property
    def path(self) -> Path:
        return FolderManager.instance().datasetsFolder / str(self.id)

    # Codable overrides

    @classmethod
    def _keyDescriptors(cls) -> Dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["items"] = KeyDescriptor("sessions", NetworkItem, list)

        return descriptors

    # NetworkObject overrides

    @classmethod
    def _endpoint(cls) -> str:
        return "dataset"

    @classmethod
    def fetchById(cls: Type[DatasetType], objectId: int, queryParameters: Optional[List[str]] = None) -> Optional[DatasetType]:
        if queryParameters is None:
            queryParameters = ["include_sessions=1"]

        return super().fetchById(objectId, queryParameters)

    @classmethod
    def fetchAll(cls: Type[DatasetType], queryParameters: Optional[List[str]] = None, pageSize: int = DEFAULT_PAGE_SIZE) -> List[DatasetType]:
        if queryParameters is None:
            queryParameters = ["include_sessions=1"]

        return super().fetchAll(queryParameters, pageSize)

    # Dataset methods

    @classmethod
    def createDataset(cls: Type[DatasetType], name: str, projectId: int, itemIds: Optional[List[int]] = None) -> Optional[DatasetType]:
        """
            Creates a new dataset with the provided name, type
            and items (if present, items are not required)

            Parameters:
            name: str -> dataset name
            projectId: int -> project for which the dataset will be created
            itemsIds: list[int] -> items which should be added to dataset (if present)

            Returns:
            The created dataset object or None if creation failed
        """

        if itemIds is None:
            itemIds = []

        return cls.create({
            "name": name,
            "project_id": projectId,
            "sessions": itemIds
        })

    def download(self, ignoreCache: bool = False) -> None:
        self.path.mkdir(exist_ok = True)

        def itemDownloader(item: ItemType) -> None:
            item.download(ignoreCache)

            symlinkPath = self.path / f"{item.id}.zip"
            if not symlinkPath.exists():
                os.symlink(item.zipPath, symlinkPath)

        processor = MultithreadedDataProcessor(
            self.items,
            itemDownloader,
            title = "Downloading dataset"
        )

        processor.process()

    def add(self, item: ItemType) -> bool:
        if self.isLocked or item.isDeleted:
            return False

        success = self.update({
            "sessions": [item.id]
        })

        if success:
            return super().add(item)

        return success

    def rename(self, name: str) -> bool:
        success = self.update({
            "name": name
        })

        if success:
            return super().rename(name)

        return success
