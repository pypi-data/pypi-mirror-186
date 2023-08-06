from typing import Optional, Dict
from datetime import datetime

from .project_task import ProjectTask
from ...codable import KeyDescriptor
from ...networking import NetworkObject


class ProjectBase(NetworkObject):
    """
        Represents the base class for Project/Experiment objects from Coretex.ai
    """

    name: str
    description: Optional[str]
    createdOn: datetime
    createdById: str
    projectTask: ProjectTask

    @classmethod
    def _endpoint(cls) -> str:
        return "project"

    @classmethod
    def _keyDescriptors(cls) -> Dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["projectTask"] = KeyDescriptor("project_task", ProjectTask)

        return descriptors

    def rename(self, name: str) -> bool:
        """
            Renames the project/experiment

            Parameters:
            name: str -> new name

            Returns:
            True if project/experiment was renamed, False if project/experiment was not renamed
        """

        if self.name == name:
            return False

        success = self.update(
            parameters = {
                "name": name
            }
        )

        if success:
            self.name = name

        return success

    def updateDescription(self, description: str) -> bool:
        """
            Updates the project/experiment's description

            Parameters:
            description: str -> new description

            Returns:
            True if project/experiment's description was updated, False if project/experiment's description was not updated
        """

        if self.description == description:
            return False

        success = self.update(
            parameters = {
                "description": description
            }
        )

        if success:
            self.description = description

        return success
