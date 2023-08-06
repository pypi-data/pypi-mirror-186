from typing import Dict

from ..image_dataset import ImageDataset
from ...item import ImageSegmentationItem
from ....codable import KeyDescriptor


class ImageSegmentationDataset(ImageDataset[ImageSegmentationItem]):

    @classmethod
    def _keyDescriptors(cls) -> Dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["items"] = KeyDescriptor("sessions", ImageSegmentationItem, list)

        return descriptors
