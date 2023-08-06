from __future__ import annotations

from typing import Optional

from .custom_item_data import CustomItemData
from .local_custom_item import LocalCustomItem
from ..network_item import NetworkItem


class CustomItem(NetworkItem[CustomItemData], LocalCustomItem):

    """
        Represents the custom Item object from Coretex.ai
    """

    def __init__(self) -> None:
        NetworkItem.__init__(self)

    @classmethod
    def createCustomItem(cls, name: str, datasetId: int, filePath: str) -> Optional[CustomItem]:
        """
            Creates a new item with the provided name and path

            Parameters:
            name: str -> item name
            datasetId: int -> id of dataset to which the item will be added
            filePath: str -> path to the item

            Returns:
            The created item object or None if creation failed
        """

        parameters = {
            "name": name,
            "dataset_id": datasetId
        }

        return cls._genericItemImport("custom-item-import", parameters, filePath)
