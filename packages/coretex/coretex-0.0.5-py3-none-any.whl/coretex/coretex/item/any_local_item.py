from typing import TypeVar

from .local_item import LocalItem


ItemDataType = TypeVar("ItemDataType")


class AnyLocalItem(LocalItem[ItemDataType]):

    @property
    def path(self) -> str:
        return str(self._path)

    @property
    def zipPath(self) -> str:
        return str(self._path)
