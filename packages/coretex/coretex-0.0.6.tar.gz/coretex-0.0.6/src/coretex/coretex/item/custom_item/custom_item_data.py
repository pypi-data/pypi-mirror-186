from pathlib import Path


class CustomItemData:

    def __init__(self, path: Path) -> None:
        self.folderContent = path.glob("*")
