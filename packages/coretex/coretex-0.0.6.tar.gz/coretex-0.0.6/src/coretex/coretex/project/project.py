from __future__ import annotations

from typing import Optional, Any

from .base import ProjectBase
from .workspace import Workspace
from .project_task import ProjectTask


class Project(ProjectBase):
    """
        Represents the Project object from Coretex.ai
    """

    workspaces: list[Workspace]

    @classmethod
    def createProject(cls, name: str, projectTask: ProjectTask, description: Optional[str] = None) -> Optional[Project]:
        """
            Creates a new project with the provided name and description

            Parameters:
            name: str -> project name
            description: Optional[str] -> project name

            Returns:
            The created project object
        """

        return cls.create(parameters={
            "name": name,
            "project_task": projectTask.value,
            "description": description
        })

    @classmethod
    def decode(cls, encodedObject: dict[str, Any]) -> Project:
        obj = super().decode(encodedObject)
        obj.workspaces = Workspace.fetchAll(queryParameters=[
            f"parentId={obj.id}"
        ])

        return obj

    def addWorkspace(self, name: str, description: Optional[str]) -> bool:
        """
            Adds new workspace to the project

            Parameters:
            name: str -> workspace name
            description: Optional[str] -> workspace description

            Returns:
            True if the workspace was added. False if the workspace was not added
        """

        workspace = Workspace.createWorkspace(name, self.id, description)
        if workspace is None:
            return False

        self.workspaces.append(workspace)
        return True
