from __future__ import annotations

from typing import Optional

from .base import ProjectBase
from ...codable import KeyDescriptor


class Workspace(ProjectBase):
    """
        Represents the Workspace object from Coretex.ai
    """

    isDefault: bool
    projectId: int

    @classmethod
    def _keyDescriptors(cls) -> dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["projectId"] = KeyDescriptor("parentId")

        return descriptors

    @classmethod
    def createWorkspace(cls, name: str, projectId: int, description: Optional[str]=None) -> Optional[Workspace]:
        """
            Creates a new workspace with the provided name and description
            Workspace is added to project with provided project id

            Parameters:
            name: str -> workspace name
            projectId: int -> project id the workspace belongs to
            description: Optional[str] -> workspace name

            Returns:
            The created workspace object
        """

        return cls.create(parameters={
            "name": name,
            "parent_id": projectId,
            "description": description
        })
