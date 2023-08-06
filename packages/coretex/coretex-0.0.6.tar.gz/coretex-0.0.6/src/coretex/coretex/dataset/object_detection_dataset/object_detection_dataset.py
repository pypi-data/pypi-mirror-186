from typing import Dict

from ..image_dataset import ImageDataset
from ...item import ObjectDetectionItem
from ....codable import KeyDescriptor


class ObjectDetectionDataset(ImageDataset[ObjectDetectionItem]):

    @classmethod
    def _keyDescriptors(cls) -> Dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["items"] = KeyDescriptor("sessions", ObjectDetectionItem, list)

        return descriptors
