from __future__ import annotations

from typing import Any, Type, TypeVar, Optional, Generic

import os

from .item import Item
from ..project import ProjectTask
from ...codable import KeyDescriptor
from ...networking import NetworkObject, NetworkManager
from ...folder_management import FolderManager
from ...utils import guessMimeType


T = TypeVar("T", bound="NetworkItem")
ItemDataType = TypeVar("ItemDataType")


class NetworkItem(Generic[ItemDataType], Item[ItemDataType], NetworkObject):

    """
        Represents the Item object from Coretex.ai
    """

    isLocked: bool
    projectTask: ProjectTask

    @property
    def path(self) -> str:
        return os.path.join(FolderManager.instance().itemsFolder, str(self.id))

    @property
    def zipPath(self) -> str:
        return f"{self.path}.zip"

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["projectTask"] = KeyDescriptor("project_task", ProjectTask)

        return descriptors

    @classmethod
    def _endpoint(cls) -> str:
        return "session"

    @classmethod
    def _genericItemImport(cls: Type[T], endpoint: str, parameters: dict[str, Any], filePath: str) -> Optional[T]:
        mimeType = guessMimeType(filePath)

        with open(filePath, "rb") as itemFile:
            files = [
                ("file", ("file", itemFile, mimeType))
            ]

            response = NetworkManager.instance().genericUpload(f"items/{endpoint}", files, parameters)
            if response.hasFailed():
                return None

            return cls.decode(response.json)

    def download(self, ignoreCache: bool = False) -> None:
        if os.path.exists(self.zipPath) and not ignoreCache:
            return

        NetworkManager.instance().genericDownload(
            endpoint = f"{self.__class__._endpoint()}/export?id={self.id}",
            destination = self.zipPath
        )

    def load(self) -> ItemDataType:
        return super().load()
