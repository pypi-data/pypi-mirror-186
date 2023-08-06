from __future__ import annotations

from enum import IntEnum
from typing import Optional
from pathlib import Path

import os

from ...codable import Codable, KeyDescriptor
from ...networking import NetworkManager, RequestType
from ...folder_management import FolderManager
from ...utils import guessMimeType


class ArtifactType(IntEnum):

    directory = 1
    file      = 2

    @staticmethod
    def typeForPath(path: str) -> ArtifactType:
        if os.path.isdir(path):
            return ArtifactType.directory

        if os.path.isfile(path):
            return ArtifactType.file

        raise RuntimeError(">> [Coretex] Unreachable")


class Artifact(Codable):

    artifactType: ArtifactType
    remoteFilePath: str
    size: Optional[int]
    mimeType: str
    timestamp: int
    experimentId: int

    @property
    def localFilePath(self) -> Path:
        return FolderManager.instance().getArtifactsFolder(self.experimentId) / self.remoteFilePath

    @property
    def isDirectory(self) -> bool:
        return self.artifactType == ArtifactType.directory

    @property
    def isFile(self) -> bool:
        return self.artifactType == ArtifactType.file

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()

        descriptors["artifactType"] = KeyDescriptor("type", ArtifactType)
        descriptors["remoteFilePath"] = KeyDescriptor("path")
        descriptors["timestamp"] = KeyDescriptor("ts")
        descriptors["experimentId"] = KeyDescriptor(isEncodable = False)

        return descriptors

    @classmethod
    def create(cls, experimentId: int, localFilePath: str, remoteFilePath: str, mimeType: Optional[str] = None) -> Optional[Artifact]:
        if mimeType is None:
            # If guessing fails, fallback to binary type
            try:
                mimeType = guessMimeType(localFilePath)
            except:
                mimeType = "application/octet-stream"

        files = [
            ("file", ("file", open(localFilePath, "rb"), mimeType))
        ]

        parameters = {
            "model_queue_id": experimentId,
            "path": remoteFilePath
        }

        response = NetworkManager.instance().genericUpload("artifact/upload-file", files, parameters)
        if response.hasFailed():
            return None

        artifact = Artifact.decode(response.json)
        artifact.experimentId = experimentId

        return artifact

    def download(self) -> bool:
        artifactsFolder = FolderManager.instance().getArtifactsFolder(self.experimentId)
        if not artifactsFolder.exists():
            artifactsFolder.mkdir(parents = True, exist_ok = True)

        return not NetworkManager.instance().genericDownload(
            f"artifact/download-file?path={self.remoteFilePath}&model_queue_id={self.experimentId}",
            str(self.localFilePath)
        ).hasFailed()

    @classmethod
    def fetchAll(cls, experimentId: int, path: Optional[str] = None, recursive: bool = False) -> list[Artifact]:
        queryParameters = [
            f"model_queue_id={experimentId}"
        ]

        if path is not None:
            queryParameters.append(f"path={path}")

        parameters = "&".join(queryParameters)
        response = NetworkManager.instance().genericJSONRequest(
            f"artifact/list-contents?{parameters}",
            RequestType.get
        )

        if response.hasFailed():
            return []

        artifacts = [Artifact.decode(element) for element in response.json]

        for artifact in artifacts:
            artifact.experimentId = experimentId

            if recursive and artifact.isDirectory:
                artifacts.extend(
                    cls.fetchAll(experimentId, artifact.remoteFilePath)
                )

        return artifacts
