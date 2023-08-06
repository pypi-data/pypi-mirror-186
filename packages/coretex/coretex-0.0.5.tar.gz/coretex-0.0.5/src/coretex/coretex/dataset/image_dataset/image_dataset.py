from __future__ import annotations

from typing import TypeVar, Type, Optional

from .base import BaseImageDataset
from ..network_dataset import NetworkDataset
from ...item import ImageItem
from ...annotation import ImageDatasetClass, ImageDatasetClasses
from ....codable import KeyDescriptor
from ....networking import NetworkManager, RequestType


DatasetType = TypeVar("DatasetType", bound = "ImageDataset")
ItemType = TypeVar("ItemType", bound = "ImageItem")


class ImageDataset(BaseImageDataset[ItemType], NetworkDataset[ItemType]):  # type: ignore

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()

        descriptors["items"] = KeyDescriptor("sessions", ImageItem, list)
        descriptors["classes"] = KeyDescriptor("classes", ImageDatasetClass, ImageDatasetClasses)

        return descriptors

    @classmethod
    def fetchById(cls: Type[DatasetType], objectId: int, queryParameters: Optional[list[str]] = None) -> Optional[DatasetType]:
        obj = super().fetchById(objectId, queryParameters)
        if obj is None:
            return None

        response = NetworkManager.instance().genericJSONRequest(
            endpoint=f"annotation-class?dataset_id={obj.id}",
            requestType=RequestType.get,
        )

        if not response.hasFailed():
            obj.classes = cls._decodeValue("classes", response.json)
            obj._writeClassesToFile()

        return obj

    def saveClasses(self, classes: ImageDatasetClasses) -> bool:
        """
            Saves provided classes (including their color) to dataset.
            ImageDataset.classes property will be updated on successful save

            Parameters:
            classes: list[ImageDatasetClass] -> list of classes

            Returns:
            True if dataset classes were saved, False if failed to save dataset classes
        """

        parameters = {
            "dataset_id": self.id,
            "classes": [clazz.encode() for clazz in classes]
        }

        response = NetworkManager.instance().genericJSONRequest("annotation-class", RequestType.post, parameters)
        if not response.hasFailed():
            return super().saveClasses(classes)

        return not response.hasFailed()
