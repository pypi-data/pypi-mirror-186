from typing import Type, TypeVar, Optional, Any, Dict, List

import inflection

from .request_type import RequestType
from .network_manager import NetworkManager
from ..codable import Codable


T = TypeVar("T", bound="NetworkObject")

DEFAULT_PAGE_SIZE = 100


class NetworkObject(Codable):
    """
        Base class for every Coretex object representation in python
    """

    id: int
    isDeleted: bool

    # Required init
    def __init__(self) -> None:
        pass

    @classmethod
    def _endpoint(cls) -> str:
        """
            Returns:
            Coretex.ai object endpoint for a given class
        """

        return inflection.underscore(cls.__name__)

    def __eq__(self, __o: object) -> bool:
        """
            Checks if the NetworkObjects which have id property
            defined are equal

            Parameter:
            __o: object -> object to which we are comparing self

            Returns:
            True if ids are present and equal, False in any other case
        """

        # check if object parent class matches
        if isinstance(__o, NetworkObject):
            return self.id == __o.id

        return NotImplemented

    def __hash__(self) -> int:
        """
            Returns:
            hash of all the items defined on the self.__dict__ object
        """

        return hash(tuple(sorted(self.__dict__.items())))

    def refresh(self, jsonObject: Optional[Dict[str, Any]] = None) -> bool:
        """
            Updates objects fields to a provided value if set, otherwise
            fetches the object from the API and updates the values
            using the fetched object

            Parameters:
            jsonObject: Optional[dict[str, Any]] -> A serialized json object to
            which the values should be updated, if provided

            Returns:
            True if the update was successful, False otherwise
        """

        # Update from json if it exists
        if jsonObject is not None:
            self._updateFields(jsonObject)
            return True

        # Fetch from server otherwise
        obj = self.__class__.fetchById(self.id)
        if obj is None:
            return False

        for key, value in obj.__dict__.items():
            self.__dict__[key] = value

        return True

    def update(self, parameters: Dict[str, Any]) -> bool:
        if self.isDeleted:
            return False

        return not NetworkManager.instance().genericJSONRequest(
            endpoint=f"{self.__class__._endpoint()}/{self.id}",
            requestType=RequestType.put,
            parameters=parameters
        ).hasFailed()

    def delete(self) -> bool:
        if self.isDeleted:
            return False

        return not NetworkManager.instance().genericDelete(
            f"{self.__class__._endpoint()}/{self.id}"
        ).hasFailed()

    @classmethod
    def create(cls: Type[T], parameters: Dict[str, Any]) -> Optional[T]:
        response = NetworkManager.instance().genericJSONRequest(
            endpoint=cls._endpoint(),
            requestType=RequestType.post,
            parameters=parameters
        )

        if response.hasFailed():
            return None

        return cls.decode(response.json)

    @classmethod
    def fetchAll(cls: Type[T], queryParameters: Optional[List[str]]=None, pageSize: int=DEFAULT_PAGE_SIZE) -> List[T]:
        if queryParameters is None:
            queryParameters = [f"page_size={pageSize}"]
        else:
            queryParameters.append(f"page_size={pageSize}")

        formattedQueryParameters = "&".join(queryParameters)
        endpoint = f"{cls._endpoint()}?{formattedQueryParameters}"

        response = NetworkManager.instance().genericJSONRequest(endpoint, RequestType.get)

        if response.hasFailed():
            return []

        objects: list[T] = []

        for obj in response.json:
            objects.append(cls.decode(obj))

        return objects

    @classmethod
    def fetchById(cls: Type[T], objectId: int, queryParameters: Optional[List[str]]=None) -> Optional[T]:
        endpoint = f"{cls._endpoint()}/{objectId}"
        if queryParameters is not None:
            formattedQueryParameters = "&".join(queryParameters)
            endpoint = f"{endpoint}?{formattedQueryParameters}"

        response = NetworkManager.instance().genericJSONRequest(endpoint, RequestType.get)

        if response.hasFailed():
            return None

        return cls.decode(response.json)
