from typing import Dict

from .base import BaseCustomDataset
from ..network_dataset import NetworkDataset
from ...item import CustomItem
from ....codable import KeyDescriptor


class CustomDataset(BaseCustomDataset, NetworkDataset[CustomItem]):

    @classmethod
    def _keyDescriptors(cls) -> Dict[str, KeyDescriptor]:
        descriptors = super()._keyDescriptors()
        descriptors["items"] = KeyDescriptor("sessions", CustomItem, list)

        return descriptors
