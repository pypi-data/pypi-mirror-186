from pathlib import Path

from .custom_item_data import CustomItemData
from ..local_item import LocalItem


class LocalCustomItem(LocalItem[CustomItemData]):

    def load(self) -> CustomItemData:
        return CustomItemData(Path(self.path))
