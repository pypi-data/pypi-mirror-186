from typing import Optional

from .converter_processor_factory import ConverterProcessorFactory
from .base_converter import ConverterProcessorType
from ..dataset import ImageDataset


def convert(type: ConverterProcessorType, datasetName: str, projectId: int, datasetPath: str) -> Optional[ImageDataset]:
    """
        Converts the given dataset to Cortex Format

        Parameters:
        datasetPath: str -> path to dataset
        type: ConverterProcessorType -> dataset format type (coco, yolo, createML, voc, labelMe, pascalSeg)

        Returns:
        The converted ImageDataset object
    """
    return ConverterProcessorFactory(type).create(datasetName, projectId, datasetPath).convert()
