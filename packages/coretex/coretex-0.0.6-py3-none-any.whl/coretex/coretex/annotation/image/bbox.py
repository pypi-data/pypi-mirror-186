from __future__ import annotations

from typing import Final

from ....codable import Codable, KeyDescriptor


class BBox(Codable):

    def __init__(self, minX: float=0, minY: float=0, width: float=0, height: float=0) -> None:
        self.minX: Final = minX
        self.minY: Final = minY

        self.width: Final = width
        self.height: Final = height

    @property
    def maxX(self) -> float:
        return self.minX + self.width

    @property
    def maxY(self) -> float:
        return self.minY + self.height

    @property
    def polygon(self) -> list[float]:
        return [
            self.minX, self.minY,  # top left
            self.maxX, self.minY,  # top right
            self.maxX, self.maxY,  # bottom right
            self.minX, self.maxY,  # bottom left
            self.minX, self.minY   # top left
        ]

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()

        descriptors["minX"] = KeyDescriptor("top_left_x")
        descriptors["minY"] = KeyDescriptor("top_left_y")

        return descriptors

    @classmethod
    def create(cls, minX: float, minY: float, maxX: float, maxY: float) -> BBox:
        return cls(minX, minY, maxX - minX, maxY - minY)

    @classmethod
    def fromPoly(cls, polygon: list[float]) -> BBox:
        x: list[float] = []
        y: list[float] = []

        for index, value in enumerate(polygon):
            if index % 2 == 0:
                x.append(value)
            else:
                y.append(value)

        return cls.create(min(x), min(y), max(x), max(y))
