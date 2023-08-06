# from __future__ import annotations

# import os
# import copy
# import json
# import shutil

# from numpy import ndarray
# from shapely.geometry import Polygon

# import cv2
# import numpy as np
# import skimage.transform as transform
# import skimage.measure
# import skimage.color

# from .annotated_image_dataset import AnnotatedImageDataset
# from ...annotation import CoretexSegmentationInstance, BBox
# from ...item import AnnotatedImageItem
# from ....folder_management import FolderManager


# class AugmentedImageItem(AnnotatedImageItem):

#     @property
#     def path(self) -> str:
#         return os.path.join(FolderManager.instance().getTempFolder("temp-augmented-ds"), str(self.id))

#     @classmethod
#     def createFromItem(cls, item: AnnotatedImageItem) -> AugmentedImageItem:
#         obj = AugmentedImageItem()

#         for key, value in item.__dict__.items():
#             obj.__dict__[key] = copy.deepcopy(value)

#         return obj


# class SyntheticImageGenerator:

#     def __transformImg(self, image: np.ndarray, imageMask: np.ndarray, bgImage: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
#         angle = np.random.randint(-40, 40) * (np.pi / 180.0)
#         image = transform.resize(image, bgImage.shape)

#         imageMask = transform.resize(imageMask, bgImage.shape)
#         imageMask = imageMask[:, :, :1]

#         zoom = np.random.random() * 0.35 + 0.1

#         zoomWidth = image.shape[1] * zoom
#         zoomHeight = image.shape[0] * zoom

#         transX = np.random.randint(int(zoomWidth), int(bgImage.shape[1] - zoomWidth))
#         transY = np.random.randint(int(zoomHeight), int(bgImage.shape[0] - zoomHeight))

#         transformation = transform.AffineTransform(scale=(zoom, zoom), rotation=angle, translation=(transX, transY))
#         imageMask = transform.warp(imageMask, transformation.inverse, output_shape=(imageMask.shape[0], imageMask.shape[1]))
#         image = transform.warp(image, transformation.inverse, output_shape=(image.shape[0], image.shape[1]))

#         # Random horizontal flip
#         if np.random.randint(0, 100) >= 50:
#             image = image[:, ::-1]
#             imageMask = imageMask[:, ::-1]

#         return image, imageMask

#     def __createMask(self, image: np.ndarray) -> np.ndarray:
#         mask = image.copy()
#         mask[mask > 0] = 1
#         return mask

#     def __composeImage(self, image: np.ndarray, segmentationMask: np.ndarray, background: np.ndarray) -> np.ndarray:
#         background = transform.resize(background, image.shape)

#         # Subtract the foreground area from the background
#         background = background * (1 - segmentationMask)
#         image = image * segmentationMask
#         result = background + image

#         if not isinstance(result, np.ndarray):
#             raise RuntimeError

#         return result

#     def __extractPolygons(self, maskImage: np.ndarray) -> list[list[float]]:
#         subMaskArray = np.asarray(maskImage)

#         # prevent segmented objects from being equal to image width/height
#         subMaskArray[:, 0] = 0
#         subMaskArray[0, :] = 0
#         subMaskArray[:, -1] = 0
#         subMaskArray[-1, :] = 0

#         contours = skimage.measure.find_contours(subMaskArray, 0.5)

#         segmentations: list[list[float]] = []
#         for contour in contours:
#             for i in range(len(contour)):
#                 row, col = contour[i]
#                 contour[i] = (col - 1, row - 1)

#             # Make a polygon and simplify it
#             poly = Polygon(contour).simplify(1.0, preserve_topology=True)

#             # Ignore if still not a Polygon (could be a line or point)
#             if poly.geom_type == 'Polygon': 
#                 segmentation = np.array(poly.exterior.coords).ravel().tolist()
#                 segmentations.append(segmentation)

#         # sorts polygons by size, descending
#         segmentations.sort(key=len, reverse=True)

#         return segmentations

#     def __processInstance(
#         self,
#         instance: CoretexSegmentationInstance,
#         item: AnnotatedImageItem,
#         background: AnnotatedImageItem,
#         augmentedItem: AnnotatedImageItem,
#         tempAugmentedImage: ndarray
#     ) -> ndarray:

#         if item.imageData is None:
#             raise RuntimeError("CTX image is missing")

#         segmentationMask = instance.extractSegmentationMask(item.imageData.shape[0], item.imageData.shape[1])

#         newImArray = item.imageData
#         newImArray = segmentationMask

#         if background.imageData is None:
#             raise RuntimeError("CTX background image doesn't exist")

#         transformedImage, transformedMask = self.__transformImg(item.imageData, newImArray, background.imageData)
#         foregroundMask = self.__createMask(transformedMask)
#         polygonMask = self.__extractPolygons(foregroundMask.reshape((foregroundMask.shape[0], foregroundMask.shape[1])))

#         augmentedInstance = copy.deepcopy(instance)
#         augmentedInstance.segmentations = polygonMask
#         if augmentedItem.coretexAnnotation is None:
#             raise RuntimeError

#         augmentedItem.coretexAnnotation.instances.append(augmentedInstance)

#         polygonMaskNp = np.array(polygonMask, dtype=np.float32)
#         flattenPoly = polygonMaskNp.flatten()
#         augmentedInstance.bbox = BBox.fromPoly(flattenPoly.tolist())
#         composedImage = self.__composeImage(transformedImage, foregroundMask, tempAugmentedImage)

#         return composedImage

#     def __processItem(self, item: AnnotatedImageItem, background: AnnotatedImageItem) -> AnnotatedImageItem:
#         augmentedItem = AugmentedImageItem.createFromItem(item)
#         augmentedItem.id = item.id + background.id

#         if background.imageData is None:
#             raise RuntimeError("CTX background image doesn't exist")

#         tempAugmentedImage = background.imageData

#         if item.coretexAnnotation is None:
#             raise RuntimeError

#         for instance in item.coretexAnnotation.instances:
#             composedImage = self.__processInstance(instance, item, background, augmentedItem, tempAugmentedImage)
#             tempAugmentedImage = composedImage
#             augmentedItem.imageData = composedImage

#         return augmentedItem

#     def __storeFiles(self, augmentedItem: AnnotatedImageItem) -> None:
#         dirPath = FolderManager.instance().getTempFolder("temp-augmented-ds")

#         if augmentedItem.imageData is None:
#             raise RuntimeError
#         if augmentedItem.coretexAnnotation is None:
#             raise RuntimeError

#         savedImage = (augmentedItem.imageData * 255.0).astype(np.uint8)
#         savedImage = cv2.cvtColor(savedImage, cv2.COLOR_BGR2RGB)

#         cv2.imwrite(os.path.join(dirPath, f"{augmentedItem.name}.jpeg"), savedImage)

#         with open(os.path.join(dirPath, "annotations.json"), 'w') as annotationfile:
#             jsonObject = json.dumps(augmentedItem.coretexAnnotation.encode())
#             annotationfile.write(jsonObject)

#         shutil.make_archive(os.path.join(dirPath, f"{augmentedItem.id}"), 'zip', dirPath)

#     def augmentDataset(self, normalDataset: AnnotatedImageDataset, backgroundDataset: AnnotatedImageDataset) -> None:
#         FolderManager.instance().createTempFolder("temp-augmented-ds")
#         augmentedItems: list[AnnotatedImageItem] = []

#         for background in backgroundDataset.items:
#             background.unzip()
#             background.load()

#             for item in normalDataset.items:
#                 item.unzip()
#                 item.load()
#                 augmentedItem = self.__processItem(item, background)
#                 self.__storeFiles(augmentedItem)
#                 augmentedItems.append(augmentedItem)

#         for item in augmentedItems:
#             normalDataset.items.append(item)


from .base import BaseImageDataset


class SyntheticImageGenerator:

    def augmentDataset(self, normalDataset: BaseImageDataset, backgroundDataset: BaseImageDataset) -> None:
        pass
