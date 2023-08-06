from pathlib import Path

from ..image_dataset import LocalImageDataset
from ...item import LocalImageSegmentationItem


class LocalImageSegmentationDataset(LocalImageDataset[LocalImageSegmentationItem]):

    def __init__(self, path: Path) -> None:
        super().__init__(path, LocalImageSegmentationItem)
