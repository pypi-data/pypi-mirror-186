from typing import Any, Optional
from pathlib import Path

import os
import json
import glob
import logging

import numpy as np

from ..base_converter import BaseConverter
from ...annotation import CoretexImageAnnotation, CoretexSegmentationInstance, BBox


class LabelMeConverter(BaseConverter):

    """
        Represents the Converter from LabelMe Format to Cortex Format
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
                data = json.load(jsonFile)

                for shape in data["shapes"]:
                    labels.add(shape["label"])

        return labels

    def __extractInstance(self, shape: dict[str, Any]) -> Optional[CoretexSegmentationInstance]:
        label = shape["label"]

        coretexClass = self._dataset.classByName(label)
        if coretexClass is None:
            logging.info(f">> [Coretex] Class: ({label}) is not a part of dataset")
            return None

        points: list[float] = np.array(shape["points"]).flatten().tolist()
        bbox = BBox.fromPoly(points)

        return CoretexSegmentationInstance.create(coretexClass.classIds[0], bbox, [points])

    def __extractImageAnnotation(self, imageAnnotation: dict[str, Any]) -> None:
        imageName = Path(imageAnnotation["imagePath"]).stem
        imageName = f"{imageName}.jpg"

        width = imageAnnotation["imageWidth"]
        height = imageAnnotation["imageHeight"]

        coretexAnnotation = CoretexImageAnnotation.create(imageName, width, height, [])

        for shape in imageAnnotation["shapes"]:
            instance = self.__extractInstance(shape)
            if instance is None:
                continue

            coretexAnnotation.instances.append(instance)

        self._saveImageAnnotationPair(os.path.join(self.__imagesPath, imageName), coretexAnnotation)

    def _extractSingleAnnotation(self, fileName: str) -> None:
        with open(fileName) as jsonFile:
            data = json.load(jsonFile)
            self.__extractImageAnnotation(data)
