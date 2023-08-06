from typing import Any, Optional, Dict
from datetime import datetime
from zipfile import ZipFile

import os
import shutil
import json
import logging

from keras import Model as KerasModel

import tensorflowjs as tfjs

from ..experiment import Experiment
from ...networking import NetworkManager, NetworkObject
from ...folder_management import FolderManager


class Model(NetworkObject):

    # override id type for Model class
    id: Optional[int]  # type: ignore

    name: str
    createdById: str
    createdOn: datetime
    datasetId: int
    projectId: int
    subProjectId: int
    isTrained: bool
    isDeleted: bool
    accuracy: float
    modelQueueId: int
    modelValidationId: Optional[int]
    meta: Dict[str, Any]

    def __init__(self, experiment: Optional[Experiment] = None):
        if experiment is not None:
            self.name = experiment.name
            self.createdById = experiment.createdById
            self.datasetId = experiment.datasetId
            self.projectId = experiment.projectId
            self.subProjectId = experiment.subProjectId
            self.modelQueueId = experiment.id

        self.createdOn = datetime.now()
        self.isTrained = False
        self.isDeleted = False
        self.accuracy = 0.0
        self.modelValidationId = None
        self.meta = {}

    @property
    def modelDescriptorFileName(self) -> str:
        return "model_descriptor.json"

    def save(self) -> bool:
        """
            Saves model data to server

            Returns:
            True if model saved successfully, False if model saving has failed
        """

        model = self.__class__.create(parameters = {
            "name": self.name,
            "model_queue_id": self.modelQueueId,
            "accuracy": self.accuracy,
            "meta": self.meta
        })

        if model is None:
            return False

        self.refresh(model.encode())
        return True

    def saveTFJSModelFromTFModel(self, model: KerasModel, path: str) -> None:
        tensorflowModelPath = os.path.join(path, "tensorflow-model")
        model.save(tensorflowModelPath)

        tensorflowJSModelPath = os.path.join(path, "tensorflow-js-model")
        tfjs.converters.convert_tf_saved_model(
            tensorflowModelPath,
            tensorflowJSModelPath
        )

        shutil.rmtree(tensorflowModelPath)

    def saveModelDescriptor(self, path: str, contents: Dict[str, Any]) -> None:
        modelDescriptorPath = os.path.join(path, self.modelDescriptorFileName)

        with open(modelDescriptorPath, "w", encoding = "utf-8") as file:
            json.dump(contents, file, ensure_ascii = False, indent = 4)

    def download(self) -> None:
        """
            Downloads and extracts the model zip file from Coretex.ai
        """

        if self.isDeleted or not self.isTrained:
            return

        modelZipDestination = os.path.join(FolderManager.instance().modelsFolder, f"{self.id}.zip")

        modelFolderDestination = os.path.join(FolderManager.instance().modelsFolder, f"{self.id}")
        if os.path.exists(modelFolderDestination):
            return

        os.mkdir(modelFolderDestination)

        response = NetworkManager.instance().genericDownload(
            endpoint=f"model/download?id={self.id}",
            destination=modelZipDestination
        )

        if response.hasFailed():
            logging.info(">> [Coretex] Failed to download the model")

        zipFile = ZipFile(modelZipDestination)
        zipFile.extractall(modelFolderDestination)
        zipFile.close()

    def upload(self, path: str) -> bool:
        """
            Uploads the model zip file to Coretex.ai

            Parameters:
            path: str -> Path to the saved model dir

            Returns:
            True if model data uploaded successfully, False if model data upload has failed
        """

        if self.isDeleted:
            return False

        logging.info(">> [Coretex] Uploading model file...")

        shutil.make_archive(path, "zip", path)

        files = {
            ("file", open(f"{path}.zip", "rb"))
        }

        parameters = {
            "id": self.id
        }

        response = NetworkManager.instance().genericUpload("model/upload", files, parameters)
        if response.hasFailed():
            logging.info(">> [Coretex] Failed to upload model file")
        else:
            logging.info(">> [Coretex] Uploaded model file")

        return not response.hasFailed()
