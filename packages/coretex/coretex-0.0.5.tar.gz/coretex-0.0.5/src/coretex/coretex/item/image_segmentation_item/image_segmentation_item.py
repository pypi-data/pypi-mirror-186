from __future__ import annotations

from typing import Optional

from ..image_item import ImageItem


class ImageSegmentationItem(ImageItem):
    """
        Represents the Image segmentation item object from Coretex.ai
    """

    @classmethod
    def createImageSegmentationItem(cls, datasetId: int, filePath: str) -> Optional[ImageSegmentationItem]:
        """
            Creates a new item with the provided name and path

            Parameters:
            datasetId: int -> id of dataset to which item will be added
            filePath: str -> path to the item

            Returns:
            The created item object or None if creation failed
        """

        return cls.createImageItem(datasetId, filePath)
