from typing import TypeVar, Type
from pathlib import Path

import json

from .base import BaseImageDataset
from ..local_dataset import LocalDataset
from ...item import LocalImageItem
from ...annotation import ImageDatasetClass, ImageDatasetClasses


ItemType = TypeVar("ItemType", bound = "LocalImageItem")


class LocalImageDataset(BaseImageDataset[ItemType], LocalDataset[ItemType]):  # type: ignore

    def __init__(self, path: Path, itemClass: Type[ItemType]) -> None:
        super().__init__(path, itemClass)

        self.classes = ImageDatasetClasses()

        if self.classesPath.exists():
            with open(path / "classes.json") as file:
                value = json.load(file)
                self.classes = ImageDatasetClasses(
                    [ImageDatasetClass.decode(element) for element in value]
                )
