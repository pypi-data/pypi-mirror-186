from typing import Any, Optional

import os
import json
import glob
import logging

from PIL import Image

from ..base_converter import BaseConverter
from ...annotation import CoretexSegmentationInstance, CoretexImageAnnotation, BBox


class CreateMLConverter(BaseConverter):

    """
        Represents the Converter from CreateML Format to Cortex Format
    """

    def __init__(self, datasetName: str, projectId: int, datasetPath: str) -> None:
        super().__init__(datasetName, projectId, datasetPath)

        self.__imagesPath = os.path.join(datasetPath, "images")

        annotations = os.path.join(datasetPath, "annotations")
        self.__fileNames = glob.glob(os.path.join(annotations, "*.json"))

    def _dataSource(self) -> list[str]:
        return self.__fileNames

    def _extractLabels(self) -> set[str]:
        labels: set[str] = set()

        for fileName in self.__fileNames:
            with open(fileName) as jsonFile:
                data = json.load(jsonFile)[0]

                for annotation in data["annotations"]:
                    labels.add(annotation["label"])

        return labels

    def __extractBBox(self, bbox: dict[str, float]) -> BBox:
        return BBox(
            bbox["x"] - bbox["width"] / 2,
            bbox["y"] - bbox["height"] / 2,
            bbox["width"],
            bbox["height"]
        )

    def __extractInstance(self, annotation: dict[str, Any]) -> Optional[CoretexSegmentationInstance]:
        label = annotation["label"]

        coretexClass = self._dataset.classByName(label)
        if coretexClass is None:
            logging.info(f">> [Coretex] Class: ({label}) is not a part of dataset")
            return None

        bbox = self.__extractBBox(annotation["coordinates"])
        return CoretexSegmentationInstance.create(coretexClass.classIds[0], bbox, [bbox.polygon])

    def __extractImageAnnotation(self, imageAnnotation: dict[str, Any]) -> None:
        imageName = imageAnnotation["image"]
        image = Image.open(f"{self.__imagesPath}/{imageName}")

        coretexAnnotation = CoretexImageAnnotation.create(imageName, image.width, image.height, [])

        for annotation in imageAnnotation["annotations"]:
            instance = self.__extractInstance(annotation)
            if instance is None:
                continue

            coretexAnnotation.instances.append(instance)

        self._saveImageAnnotationPair(os.path.join(self.__imagesPath, imageName), coretexAnnotation)

    def _extractSingleAnnotation(self, fileName: str) -> None:
        with open(fileName) as jsonFile:
            data = json.load(jsonFile)[0]

            self.__extractImageAnnotation(data)
