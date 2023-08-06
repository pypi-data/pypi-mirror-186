from enum import IntEnum


class ImageFormat(IntEnum):

    jpg = 0
    png = 1

    @property
    def extension(self) -> str:
        if self == ImageFormat.jpg:
            return "jpeg"

        return self.name
