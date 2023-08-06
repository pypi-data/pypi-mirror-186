from typing import TypeVar, Type, Optional
from pathlib import Path

from .image_item_data import AnnotatedImageItemData
from .local_image_item import LocalImageItem
from .image_format import ImageFormat
from ..network_item import NetworkItem
from ...annotation import CoretexImageAnnotation
from ....networking import NetworkManager, RequestType


T = TypeVar("T", bound = "ImageItem")


class ImageItem(NetworkItem[AnnotatedImageItemData], LocalImageItem):

    def __init__(self) -> None:
        NetworkItem.__init__(self)

    @property
    def imagePath(self) -> Path:
        path = Path(self.path)

        for format in ImageFormat:
            imagePaths = list(path.glob(f"*.{format.extension}"))
            imagePaths = [path for path in imagePaths if not "thumbnail" in str(path)]

            if len(imagePaths) > 0:
                return Path(imagePaths[0])

        raise FileNotFoundError

    @property
    def annotationPath(self) -> Path:
        return Path(self.path) / "annotations.json"

    def saveAnnotation(self, coretexAnnotation: CoretexImageAnnotation) -> bool:
        super().saveAnnotation(coretexAnnotation)

        parameters = {
            "id": self.id,
            "data": coretexAnnotation.encode()
        }

        response = NetworkManager.instance().genericJSONRequest(
            endpoint = "session/save-annotations",
            requestType = RequestType.post,
            parameters = parameters
        )

        return not response.hasFailed()

    @classmethod
    def createImageItem(cls: Type[T], datasetId: int, path: str) -> Optional[T]:
        """
            Creates a new image item with the provided dataset and path

            Parameters:
            datasetId: int -> id of dataset in which image item will be created
            path: str -> path to the image item

            Returns:
            The created image item object
        """

        parameters = {
            "dataset_id": datasetId
        }

        return cls._genericItemImport("image-import", parameters, path)
