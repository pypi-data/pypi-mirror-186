from typing import Final

from .base_converter import ConverterProcessorType, BaseConverter
from .converters import *


class ConverterProcessorFactory:

    def __init__(self, convertProcessorType: ConverterProcessorType):
        self.type: Final = convertProcessorType

    def create(self, datasetName: str, projectId: int, datasetPath: str) -> BaseConverter:
        if self.type == ConverterProcessorType.coco:
            return COCOConverter(datasetName, projectId, datasetPath)

        if self.type == ConverterProcessorType.yolo:
            return YoloConverter(datasetName, projectId, datasetPath)

        if self.type ==  ConverterProcessorType.createML:
            return CreateMLConverter(datasetName, projectId, datasetPath)

        if self.type == ConverterProcessorType.voc:
            return VOCConverter(datasetName, projectId, datasetPath)

        if self.type == ConverterProcessorType.labelMe:
            return LabelMeConverter(datasetName, projectId, datasetPath)

        if self.type == ConverterProcessorType.pascalSeg:
            return PascalSegConverter(datasetName, projectId, datasetPath)

        if self.type == ConverterProcessorType.humanSegmentation:
            return HumanSegmentationConverter(datasetName, projectId, datasetPath)

        if self.type == ConverterProcessorType.cityScape:
            return CityScapeConverter(datasetName, projectId, datasetPath)

        raise RuntimeError()
