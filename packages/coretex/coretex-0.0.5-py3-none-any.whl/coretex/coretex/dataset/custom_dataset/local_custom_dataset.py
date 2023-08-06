from pathlib import Path

from .base import BaseCustomDataset
from ..local_dataset import LocalDataset
from ...item import LocalCustomItem


class LocalCustomDataset(BaseCustomDataset, LocalDataset[LocalCustomItem]):

    def __init__(self, path: Path) -> None:
        super().__init__(path, LocalCustomItem)
