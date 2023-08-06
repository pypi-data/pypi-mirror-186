from __future__ import annotations

from typing import Final, Optional, Any, Generator
from threading import Lock
from zipfile import ZipFile
from pathlib import Path

import os
import logging
import zipfile

from .status import ExperimentStatus
from .artifact import Artifact
from ..project import ProjectTask
from ...codable import KeyDescriptor
from ...networking import NetworkManager, NetworkObject, RequestType
from ...folder_management import FolderManager
from ...utils import file as fileUtils


class Experiment(NetworkObject):

    """
        Represents the Experiment object from Coretex.ai
    """

    __statusUpdateLock: Final = Lock()

    datasetId: int
    name: str
    description: str
    meta: dict[str, Any]
    status: ExperimentStatus
    projectName: str
    projectId: int
    projectTask: ProjectTask
    subProjectName: str
    subProjectId: int
    createdById: str
    useCachedEnv: bool

    def __init__(self) -> None:
        super(Experiment, self).__init__()

        self.__lastStatusMessage: Optional[str] = None
        self.__parameters: dict[str, Any] = {}

    @property
    def parameters(self) -> dict[str, Any]:
        return self.__parameters

    @property
    def workspacePath(self) -> str:
        return FolderManager.instance().getTempFolder(str(self.id))

    # Codable overrides

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()

        descriptors["status"] = KeyDescriptor("status", ExperimentStatus)
        descriptors["projectTask"] = KeyDescriptor("project_task", ProjectTask)

        # private properties of the object should not be encoded
        descriptors["__lastStatusMessage"] = KeyDescriptor(isEncodable = False)
        descriptors["__parameters"] = KeyDescriptor(isEncodable = False)

        return descriptors

    # NetworkObject overrides

    @classmethod
    def _endpoint(cls) -> str:
        return "model-queue"

    def onDecode(self) -> None:
        if self.meta["parameters"] is None:
            self.meta["parameters"] = []

        parameters = self.meta["parameters"]

        if not isinstance(parameters, list):
            raise ValueError

        for p in parameters:
            self.__parameters[p["name"]] = p["value"]

        return super().onDecode()

    # Experiment methods

    def updateStatus(self, status: ExperimentStatus, message: Optional[str] = None) -> None:
        """
            Updates Experiment status

            Parameters:
            status: ExperimentStatus -> ExperimentStatus type
            message: Optional[str] -> Descriptive message for experiment status
        """

        with Experiment.__statusUpdateLock:
            if message is None:
                message = status.defaultMessage

            assert(len(message) > 10)  # Some information needs to be sent to Coretex.ai
            self.status = status
            self.__lastStatusMessage = message

            parameters: dict[str, Any] = {
                "id": self.id,
                "status": status.value,
                "status_message": message
            }

            # TODO: Should API rename this too?
            endpoint = "model-queue/job-status-update"
            response = NetworkManager.instance().genericJSONRequest(
                endpoint = endpoint,
                requestType = RequestType.post,
                parameters = parameters
            )

            if response.hasFailed():
                logging.info(">> [MLService] Error while updating experiment status")

    def getLastStatusMessage(self) -> Optional[str]:
        return self.__lastStatusMessage

    def downloadWorkspace(self) -> bool:
        """
            Download workspace

            Returns:
            True if workspace downloaded successfully, False if workspace download has failed
        """

        zipFilePath = f"{self.workspacePath}.zip"

        response = NetworkManager.instance().genericDownload(
            endpoint=f"workspace/download?model_queue_id={self.id}",
            destination=zipFilePath
        )

        with ZipFile(zipFilePath) as zipFile:
            zipFile.extractall(self.workspacePath)

        # remove zip file after extract
        os.unlink(zipFilePath)

        if response.hasFailed():
            logging.info(">> [MLService] Workspace download has failed")

        return not response.hasFailed()

    def createArtifact(self, localFilePath: str, remoteFilePath: str, mimeType: Optional[str] = None) -> Optional[Artifact]:
        return Artifact.create(self.id, localFilePath, remoteFilePath, mimeType)

    def createQiimeArtifact(self, rootArtifactFolderName: str, qiimeArtifactPath: Path) -> None:
        if not zipfile.is_zipfile(qiimeArtifactPath):
            raise ValueError(">> [Coretex] Not an archive")

        localFilePath = str(qiimeArtifactPath)
        remoteFilePath = f"{rootArtifactFolderName}/{qiimeArtifactPath.name}"

        artifact = self.createArtifact(localFilePath, remoteFilePath)
        if artifact is None:
            logging.warning(f">> [Coretex] Failed to upload {localFilePath} to {remoteFilePath}")

        # TODO: Enable when uploading file by file is not slow anymore
        # tempDir = Path(FolderManager.instance().createTempFolder(rootArtifactFolderName))
        # fileUtils.recursiveUnzip(qiimeArtifactPath, tempDir, remove = False)

        # for path in fileUtils.walk(tempDir):
        #     relative = path.relative_to(tempDir)

        #     localFilePath = str(path)
        #     remoteFilePath = f"{rootArtifactFolderName}/{str(relative)}"

        #     logging.debug(f">> [Coretex] Uploading {localFilePath} to {remoteFilePath}")

        #     artifact = self.createArtifact(localFilePath, remoteFilePath)
        #     if artifact is None:
        #         logging.warning(f">> [Coretex] Failed to upload {localFilePath} to {remoteFilePath}")

    @classmethod
    def startCustomExperiment(
        cls,
        datasetId: int,
        subProjectId: int,
        serviceId: int,
        name: str,
        description: Optional[str] = None,
        parameters: Optional[list[dict[str, Any]]] = None
    ) -> Optional[Experiment]:

        if description is None:
            description = ""

        if parameters is None:
            parameters = []

        response = NetworkManager.instance().genericJSONRequest(
            f"{cls._endpoint()}/custom",
            RequestType.post,
            parameters={
                "dataset_id": datasetId,
                "sub_project_id": subProjectId,
                "service_id": serviceId,
                "name": name,
                "description": description,
                "parameters": parameters
            }
        )

        if response.hasFailed():
            return None

        return cls.decode(response.json[0])
