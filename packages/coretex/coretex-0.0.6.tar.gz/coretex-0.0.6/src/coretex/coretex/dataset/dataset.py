from typing import Optional, TypeVar, Generic, List
from abc import ABC, abstractmethod
from pathlib import Path

from ..item import Item


ItemType = TypeVar("ItemType", bound = "Item")


class Dataset(ABC, Generic[ItemType]):

    name: str
    items: List[ItemType]

    @property
    def count(self) -> int:
        """
            Returns:
            Number of items in this dataset
        """

        return len(self.items)

    @property
    @abstractmethod
    def path(self) -> Path:
        pass

    @abstractmethod
    def download(self, ignoreCache: bool = False) -> None:
        pass

    def add(self, item: ItemType) -> bool:
        """
            Adds the specified item into the dataset, only
            if the dataset is not locked or deleted and if the item
            is not deleted

            Parameters:
            item: Item -> item which should be added into the dataset

            Returns:
            True if item was added, False if item was not added
        """

        self.items.append(item)
        return True

    def rename(self, name: str) -> bool:
        """
            Renames the dataset, only if the dataset
            is not locked, or if the provided name is
            different from the current name

            Parameters:
            name: str -> new dataset name

            Returns:
            True if dataset was renamed, False if dataset was not renamed
        """

        if self.name == name:
            return False

        self.name = name
        return True

    def getItem(self, name: str) -> Optional[ItemType]:
        for item in self.items:
            if item.name == name:
                return item

        return None
