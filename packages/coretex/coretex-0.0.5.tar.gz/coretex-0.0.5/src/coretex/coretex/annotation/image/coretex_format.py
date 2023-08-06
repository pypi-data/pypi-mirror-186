from __future__ import annotations

from uuid import UUID
from typing import List

import numpy as np
import cv2

from .bbox import BBox
from .classes_format import ImageDatasetClasses
from ....codable import Codable, KeyDescriptor


SegmentationType = List[float]


class CoretexSegmentationInstance(Codable):

    classId: UUID
    bbox: BBox
    segmentations: List[SegmentationType]

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()

        descriptors["classId"] = KeyDescriptor("class_id", UUID)
        descriptors["bbox"] = KeyDescriptor("bbox", BBox)
        descriptors["segmentations"] = KeyDescriptor("annotations")

        return descriptors

    @staticmethod
    def create(classId: UUID, bbox: BBox, segmentations: List[SegmentationType]) -> CoretexSegmentationInstance:
        obj = CoretexSegmentationInstance()

        obj.classId = classId
        obj.bbox = bbox
        obj.segmentations = segmentations

        return obj

    def extractSegmentationMask(self, width: int, height: int) -> np.ndarray:
        reconstructed = np.zeros((width, height, 1), dtype="uint8")

        for segmentation in self.segmentations:
            mask = np.array(segmentation, dtype=np.int32).reshape((-1, 2))
            cv2.fillPoly(reconstructed, [mask], 1)

        return reconstructed

class CoretexImageAnnotation(Codable):

    name: str
    width: float
    height: float
    instances: list[CoretexSegmentationInstance]

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["instances"] = KeyDescriptor("instances", CoretexSegmentationInstance, list)

        return descriptors

    @staticmethod
    def create(
        name: str,
        width: float,
        height: float,
        instances: list[CoretexSegmentationInstance]
    ) -> CoretexImageAnnotation:
        obj = CoretexImageAnnotation()

        obj.name = name
        obj.width = width
        obj.height = height
        obj.instances = instances

        return obj

    def extractSegmentationMask(self, classes: ImageDatasetClasses) -> np.ndarray:
        reconstructed = np.zeros((int(self.height), int(self.width), 1), dtype="uint8")

        for instance in self.instances:
            labelId = classes.labelIdForClassId(instance.classId)
            if labelId is None:
                continue

            for segmentation in instance.segmentations:
                if len(segmentation) == 0:
                    raise ValueError(f">> [Coretex] Empty segmentation")

                mask = np.array(segmentation, dtype=np.int32).reshape((-1, 2))
                cv2.fillPoly(reconstructed, [mask], labelId + 1)

        return reconstructed
