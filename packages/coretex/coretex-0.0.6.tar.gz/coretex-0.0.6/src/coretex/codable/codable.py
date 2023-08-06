from datetime import datetime
from enum import Enum
from typing import Any, Optional, TypeVar, Type, Dict, Tuple
from uuid import UUID

import inflection

from .descriptor import KeyDescriptor
from ..utils.date import DATE_FORMAT


T = TypeVar("T", bound="Codable")


def processDate(value: str, datetimeType: Type[datetime]) -> datetime:
    try:
        return datetimeType.strptime(value, DATE_FORMAT)
    except:
        # Python's datetime library requires UTC minutes to always
        # be present in the date in either of those 2 formats:
        # - +HHMM
        # - +HH:MM
        # BUT coretex API sends it in one of those formats:
        # - +HH
        # - +HH:MM (only if the minutes have actual value)
        # so we need to handle the first case where minutes
        # are not present by adding them manually
        return datetimeType.strptime(f"{value}00", DATE_FORMAT)


class Codable:

    @classmethod
    def _keyDescriptors(cls) -> Dict[str, KeyDescriptor]:
        """
            Defines how to translate json key names and json values to python
            and vice versa

            Returns:
            list[KeyDescriptor] -> List of objects describing translation
        """
        return {}

    @classmethod
    def __keyDescriptorByJsonName(cls, jsonName: str) -> Tuple[Optional[str], Optional[KeyDescriptor]]:
        for key, value in cls._keyDescriptors().items():
            if value.jsonName == jsonName:
                return key, value

        return None, None

    @classmethod
    def __keyDescriptorByPythonName(cls, pythonName: str) -> Optional[KeyDescriptor]:
        if not pythonName in cls._keyDescriptors().keys():
            return None

        return cls._keyDescriptors()[pythonName]

    # - Encoding

    def __encodeKey(self, key: str) -> str:
        descriptor = self.__class__.__keyDescriptorByPythonName(key)

        if descriptor is None or descriptor.jsonName is None:
            return inflection.underscore(key)

        return descriptor.jsonName

    def _encodeValue(self, key: str, value: Any) -> Any:
        """
            Used to change json field value

            Parameters:
            key: str -> python object variable name
            value: Any -> json object represented as an object from standard python library
        """

        descriptor = self.__class__.__keyDescriptorByPythonName(key)

        if descriptor is None or descriptor.pythonType is None:
            return value

        if issubclass(descriptor.pythonType, Enum):
            if descriptor.isList():
                return [element.value for element in value]

            return value.value

        if issubclass(descriptor.pythonType, UUID):
            if descriptor.isList():
                return [str(element) for element in value]

            return str(value)

        if issubclass(descriptor.pythonType, Codable):
            if descriptor.isList():
                return [descriptor.pythonType.encode(element) for element in value]

            return descriptor.pythonType.encode(value)

        if issubclass(descriptor.pythonType, datetime):
            if descriptor.isList():
                return [element.strftime(DATE_FORMAT) for element in value]

            return value.strftime(DATE_FORMAT)

        return value

    def encode(self) -> Dict[str, Any]:
        """
            Encodes python object into dictionary which contains
            only values representable by standard python library
        """

        encodedObject: dict[str, Any] = {}

        for key, value in self.__dict__.items():
            descriptor = self.__class__.__keyDescriptorByPythonName(key)

            # skip ignored fields for encoding
            if descriptor is not None and not descriptor.isEncodable:
                # print(f">> [Coretex] Skipping encoding for field: {key}")
                continue

            encodedKey = self.__encodeKey(key)
            encodedValue = self._encodeValue(key, value)

            encodedObject[encodedKey] = encodedValue

        return encodedObject

    # - Decoding

    @classmethod
    def __decodeKey(cls, key: str) -> str:
        descriptorKey, _ = cls.__keyDescriptorByJsonName(key)

        if descriptorKey is None:
            return inflection.camelize(key, False)

        return descriptorKey

    @classmethod
    def _decodeValue(cls, key: str, value: Any) -> Any:
        _, descriptor = cls.__keyDescriptorByJsonName(key)

        if descriptor is None or descriptor.pythonType is None:
            return value

        if issubclass(descriptor.pythonType, Enum):
            if descriptor.isList() and descriptor.collectionType is not None:
                return descriptor.collectionType([descriptor.pythonType(element) for element in value])

            return descriptor.pythonType(value)

        if issubclass(descriptor.pythonType, UUID):
            if descriptor.isList() and descriptor.collectionType is not None:
                return descriptor.collectionType([descriptor.pythonType(element) for element in value])

            return descriptor.pythonType(value)

        if issubclass(descriptor.pythonType, Codable):
            if descriptor.isList() and descriptor.collectionType is not None:
                return descriptor.collectionType([descriptor.pythonType.decode(element) for element in value])

            return descriptor.pythonType.decode(value)

        if issubclass(descriptor.pythonType, datetime):
            if descriptor.isList() and descriptor.collectionType is not None:
                return descriptor.collectionType([processDate(element, descriptor.pythonType) for element in value])

            return processDate(value, descriptor.pythonType)

        return value

    def _updateFields(self, encodedObject: Dict[str, Any]) -> None:
        for key, value in encodedObject.items():
            _, descriptor = self.__class__.__keyDescriptorByJsonName(key)

            # skip ignored fields for deserialization
            if descriptor is not None and not descriptor.isDecodable:
                # print(f">> [Coretex] Skipping decoding for field: {key}")
                continue

            decodedKey = self.__decodeKey(key)
            self.__dict__[decodedKey] = self._decodeValue(key, value)

    def onDecode(self) -> None:
        pass

    @classmethod
    def decode(cls: Type[T], encodedObject: Dict[str, Any]) -> T:
        obj = cls()

        obj._updateFields(encodedObject)
        obj.onDecode()

        return obj
