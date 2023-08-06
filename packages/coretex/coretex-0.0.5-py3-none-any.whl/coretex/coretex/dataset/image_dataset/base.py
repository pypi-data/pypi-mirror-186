from typing import TypeVar, Generic, Optional, List
from pathlib import Path

import json

from ...item import Item
from ...annotation import ImageDatasetClass, ImageDatasetClasses


ItemType = TypeVar("ItemType", bound = "Item")


class BaseImageDataset(Generic[ItemType]):

    items: List[ItemType]
    classes: ImageDatasetClasses
    path: Path

    @property
    def classesPath(self) -> Path:
        return self.path / "classes.json"

    def classByName(self, name: str) -> Optional[ImageDatasetClass]:
        for clazz in self.classes:
            if clazz.label == name:
                return clazz

        return None

    def _writeClassesToFile(self) -> None:
        self.path.mkdir(exist_ok = True)

        with open(self.classesPath, "w") as file:
            json.dump([clazz.encode() for clazz in self.classes], file)

    def saveClasses(self, classes: ImageDatasetClasses) -> bool:
        """
            Saves provided classes (including their color) to dataset.
            ImageDataset.classes property will be updated on successful save

            Parameters:
            classes: list[ImageDatasetClass] -> list of classes

            Returns:
            True if dataset classes were saved, False if failed to save dataset classes
        """

        self.classes = classes
        self._writeClassesToFile()

        return True
