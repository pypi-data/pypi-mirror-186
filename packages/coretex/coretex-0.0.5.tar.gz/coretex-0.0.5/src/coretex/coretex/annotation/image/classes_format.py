from __future__ import annotations

from typing import Optional, List
from uuid import UUID

import uuid
import random

from ....codable import Codable, KeyDescriptor


class ImageDatasetClass(Codable):
    """
        Represents the Image Dataset metadata format
    """

    classIds: list[UUID]
    label: str
    color: str

    def __init__(self, label: Optional[str] = None, color: Optional[str] = None):
        if label is None:
            label = ""

        if color is None:
            color = ""

        self.classIds = [uuid.uuid4()]
        self.label = label
        self.color = color

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()

        descriptors["classIds"] = KeyDescriptor("ids", UUID, list)
        descriptors["label"] = KeyDescriptor("name")

        return descriptors

    @classmethod
    def generate(cls, labels: set[str]) -> ImageDatasetClasses:
        colors: set[str] = set()

        while len(colors) != len(labels):
            color = f'#{"%06x" % random.randint(0, 0xFFFFFF)}'
            colors.add(color)

        return ImageDatasetClasses(
            [cls(label, color) for label, color in zip(labels, colors)]
        )


class ImageDatasetClasses(List[ImageDatasetClass]):

    @property
    def labels(self) -> List[str]:
        labels = [element.label for element in self]
        labels.sort()

        return labels

    def classById(self, classId: UUID) -> Optional[ImageDatasetClass]:
        for element in self:
            for other in element.classIds:
                if str(classId) == str(other):
                    return element

        return None

    def classByLabel(self, label: str) -> Optional[ImageDatasetClass]:
        for element in self:
            if element.label == label:
                return element

        return None

    def labelIdForClassId(self, classId: UUID) -> Optional[int]:
        clazz = self.classById(classId)
        if clazz is None:
            return None

        try:
            return self.labels.index(clazz.label)
        except ValueError:
            return None

    def labelIdForClass(self, clazz: ImageDatasetClass) -> Optional[int]:
        return self.labelIdForClassId(clazz.classIds[0])

    def filter(self, keep: list[str]) -> None:
        classes = [
            element for element in self
            if element.label in keep
        ]

        self.clear()
        self.extend(classes)
