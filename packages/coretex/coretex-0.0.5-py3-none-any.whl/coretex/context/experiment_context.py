from __future__ import annotations

from typing import Final, Any, Generic, Optional, Type, TypeVar

import os
import json

from ..coretex import Experiment, Model, ProjectTask
from ..coretex.dataset import *


T = TypeVar("T", bound = "NetworkDataset")


class ContextBuilder(Generic[T]):

    def __init__(self, experimentId: int) -> None:
        self.experimentId: Final = experimentId

        self.__datasetType: Optional[Type[T]] = None

    def setDatasetType(self, datasetType: Optional[Type[T]]) -> ContextBuilder:
        self.__datasetType = datasetType
        return self

    def __getDatasetType(self, experiment: Experiment) -> Type[T]:
        if self.__datasetType is not None:
            return self.__datasetType

        if experiment.projectTask == ProjectTask.other:
            return CustomDataset  # type: ignore

        if experiment.projectTask == ProjectTask.imageSegmentation:
            return ImageSegmentationDataset  # type: ignore

        if experiment.projectTask == ProjectTask.objectDetection:
            return ObjectDetectionDataset  # type: ignore

        raise ValueError(f">> [Coretex] ProjectTask ({experiment.projectTask}) not supported")

    def build(self) -> ExperimentContext[T]:
        experiment = Experiment.fetchById(self.experimentId)
        if experiment is None:
            raise Exception(f">> [Coretex] Experiment (ID: {self.experimentId}) not found")

        if not os.path.exists("experiment.config"):
            raise FileNotFoundError(">> [Coretex] (experiment.config) file not found")

        with open("experiment.config", "r") as configFile:
            config: dict[str, Any] = {}
            configContent = json.load(configFile)

            # load parameters array as key => value pairs
            if "parameters" in configContent:
                parameters = configContent["parameters"]

                if not isinstance(parameters, list):
                    raise ValueError(">> [Coretex] Invalid experiment.config file. Property 'parameters' must be an array")

                for parameter in parameters:
                    config[parameter["name"]] = parameter["value"]

            dataset = self.__getDatasetType(experiment).fetchById(config["dataset"])
            if dataset is None:
                raise Exception(f">> [Coretex] Dataset (ID: {config['dataset']}) not found")

        return ExperimentContext(experiment, dataset, config)


class ExperimentContext(Generic[T]):

    __instance: Optional[ExperimentContext] = None

    @classmethod
    def instance(cls) -> ExperimentContext:
        if cls.__instance is None:
            raise ValueError(">> [Coretex] Invalid context access")

        return cls.__instance

    def __init__(self, experiment: Experiment, dataset: T, config: dict[str, Any]):
        self.experiment: Final = experiment
        self.dataset: Final = dataset
        self.config: Final = config

    @classmethod
    def create(cls, experimentId: int, datasetType: Optional[Type[T]] = None) -> ExperimentContext:
        if cls.__instance is not None:
            raise ValueError(">> [Coretex] Context already exists")

        cls.__instance = ContextBuilder(experimentId).setDatasetType(datasetType).build()  # type: ignore
        return cls.__instance

    @classmethod
    def destroy(cls) -> None:
        if cls.__instance is None:
            raise ValueError(">> [Coretex] Context already destroyed")

        cls.__instance = None

    def createModel(self) -> Model:
        return Model(self.experiment)
