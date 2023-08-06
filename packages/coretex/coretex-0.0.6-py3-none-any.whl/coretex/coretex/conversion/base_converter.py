from typing import Any, Final, Optional
from enum import Enum
from abc import ABC, abstractmethod

import logging

from ..annotation import CoretexImageAnnotation
from ...coretex import ImageDataset, ImageItem, ImageDatasetClass
from ...threading import MultithreadedDataProcessor


ImageDatasetType = ImageDataset[ImageItem]


class ConverterProcessorType(Enum):

    coco = 0
    yolo = 1
    createML = 2
    voc = 3
    labelMe = 4
    pascalSeg = 5

    # TODO: Migrate to Human Segmentation workspace repo, or try to make it generic
    humanSegmentation = 6

    cityScape = 7


class BaseConverter(ABC):

    """
        Base class for Coretex Annotation format conversion
    """

    def __init__(self, datasetName: str, projectId: int, datasetPath: str) -> None:
        dataset: Optional[ImageDatasetType] = ImageDataset.createDataset(datasetName, projectId)
        if dataset is None:
            raise ValueError(">> [Coretex] Failed to create dataset")

        self._dataset: Final = dataset
        self._datasetPath: Final = datasetPath

    def _saveImageAnnotationPair(self, imagePath: str, annotation: CoretexImageAnnotation) -> None:
        # Create item
        item = ImageItem.createImageItem(self._dataset.id, imagePath)
        if item is None:
            logging.info(">> [Coretex] Failed to create item")
            return

        # Add created item to dataset
        self._dataset.items.append(item)

        # Attach annotation to item
        if not item.saveAnnotation(annotation):
            logging.info(">> [Coretex] Failed to save ImageItem annotation")

    @abstractmethod
    def _dataSource(self) -> list[Any]:
        pass

    @abstractmethod
    def _extractLabels(self) -> set[str]:
        pass

    @abstractmethod
    def _extractSingleAnnotation(self, value: Any) -> None:
        pass

    def convert(self) -> ImageDatasetType:

        """
            Converts the dataset to Cortex Format

            Parameters:
            datasetPath: str -> path to dataset

            Returns:
            The converted ImageDataset object
        """

        # Extract classes
        labels = self._extractLabels()
        classes = ImageDatasetClass.generate(labels)

        if self._dataset.saveClasses(classes):
            logging.info(">> [Coretex] Dataset classes saved successfully")
        else:
            logging.info(">> [Coretex] Failed to save dataset classes")

        # Extract annotations
        MultithreadedDataProcessor(
            self._dataSource(),
            self._extractSingleAnnotation,
            title = "Converting dataset"
        ).process()

        return self._dataset
