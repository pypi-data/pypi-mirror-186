from pathlib import Path

from ..image_dataset import LocalImageDataset
from ...item import LocalObjectDetectionItem


class ObjectDetectionDataset(LocalImageDataset[LocalObjectDetectionItem]):

    def __init__(self, path: Path) -> None:
        super().__init__(path, LocalObjectDetectionItem)
