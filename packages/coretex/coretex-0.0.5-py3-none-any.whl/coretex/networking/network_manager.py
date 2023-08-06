from __future__ import annotations
from pathlib import Path

from typing import Optional, Any
from threading import Lock

import os
import json

from .requests_manager import RequestsManager
from .request_type import RequestType
from .network_response import HttpCode, NetworkResponse


class NetworkManager:

    __instanceLock = Lock()
    __instance: Optional[NetworkManager] = None

    @classmethod
    def instance(cls) -> NetworkManager:
        if cls.__instance is None:
            with cls.__instanceLock:
                if cls.__instance is None:
                    cls.__instance = cls()

        return cls.__instance

    def __init__(self) -> None:
        self.__requestManager = RequestsManager(
            baseURL = "{0}api/v1/".format(os.environ["SERVER_IP"]),
            connectionTimeout = 20,
            readTimeout = 30
        )

        self.__apiToken: Optional[str] = None
        self.__refreshToken: Optional[str] = None
        self.__agentID: Optional[int] = None

        # Override NetworkManager to update values
        self.loginEndpoint: str = "user/login"
        self.refreshEndpoint: str = "user/refresh"

        self.apiTokenHeaderField: str = "api-token"
        self.agentIDHeaderField: str = "User-Agent"

        self.apiTokenKey: str = "token"
        self.refreshTokenKey: str = "refresh_token"

    @property
    def agentID(self) -> Optional[int]:
        return self.__agentID

    @agentID.setter
    def agentID(self, agentID: int) -> None:
        self.__agentID = agentID

    def __requestHeader(self) -> dict[str, str]:
        header = {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Accept-Encoding": "gzip, deflate",
            "Content-Length": "0",
            "Connection": "keep-alive",
            "cache-control": "no-cache"
        }

        if self.__apiToken is not None:
            header[self.apiTokenHeaderField] = self.__apiToken

        if self.__agentID is not None:
            header[self.agentIDHeaderField] = str(self.__agentID)

        return header

    def genericDownload(
        self,
        endpoint: str,
        destination: str,
        parameters: Optional[dict[str, Any]] = None,
        retryCount: int = 0
    ) -> NetworkResponse:
        """
            Downloads file to the given destination

            Parameters:
            endpoint: str -> API endpoint
            destination: str -> path to save file
            parameters: Optional[dict[str, Any]] -> request parameters (not required)
            retryCount: int -> number of function calls if request has failed

            Returns:
            NetworkResponse as response content to request
        """

        headers = self.__requestHeader()

        if parameters is None:
            parameters = {}

        response = self.__requestManager.get(
            endpoint = endpoint,
            headers = headers,
            jsonObject = parameters
        )

        if self.shouldRetry(retryCount, response):
            print(">> [MLService] Retry count: {0}".format(retryCount))

            if self.__apiToken is not None:
                headers[self.apiTokenHeaderField] = self.__apiToken

            return self.genericDownload(
                endpoint = endpoint,
                destination = destination,
                parameters = parameters,
                retryCount = retryCount + 1
            )

        if response.raw.ok:
            destinationPath = Path(destination)
            if destinationPath.is_dir():
                raise RuntimeError(">> [Coretex] Destination is a directory not a file")

            if destinationPath.exists():
                destinationPath.unlink(missing_ok = True)

            destinationPath.parent.mkdir(parents = True, exist_ok = True)

            with open(destination, "wb") as downloadedFile:
                downloadedFile.write(response.raw.content)

        return response

    def genericUpload(
        self,
        endpoint: str,
        files: Any,
        parameters: Optional[dict[str, Any]] = None,
        retryCount: int = 0
    ) -> NetworkResponse:
        """
            Uploads files to Cortex.ai

            Parameters:
            endpoint: str -> API endpoint
            files: Any -> files
            parameters: Optional[dict[str, Any]] -> request parameters (not required)
            retryCount: int -> number of function calls if request has failed

            Returns:
            NetworkResponse as response content to request
        """

        headers = self.__requestHeader()
        del headers['Content-Type']

        if parameters is None:
            parameters = {}

        networkResponse = self.__requestManager.genericRequest(
            requestType = RequestType.post,
            endpoint = endpoint,
            headers = headers,
            data = parameters,
            files = files
        )

        if self.shouldRetry(retryCount, networkResponse):
            print(">> [MLService] Retry count: {0}".format(retryCount))

            if self.__apiToken is not None:
                headers[self.apiTokenHeaderField] = self.__apiToken

            return self.genericUpload(
                endpoint = endpoint,
                files = files,
                parameters = parameters,
                retryCount = retryCount + 1
            )

        return networkResponse

    def genericDelete(
        self,
        endpoint: str
    ) -> NetworkResponse:
        """
            Deletes Cortex.ai objects

            Parameters:
            endpoint: str -> API endpoint

            Returns:
            NetworkResponse as response content to request
        """

        headers = self.__requestHeader()

        return self.__requestManager.genericRequest(
            requestType = RequestType.delete,
            endpoint = endpoint,
            headers = headers
        )

    def genericJSONRequest(
        self,
        endpoint: str,
        requestType: RequestType,
        parameters: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
        retryCount: int = 0
    ) -> NetworkResponse:
        """
            Sends generic http request with specified parameters

            Parameters:
            endpoint: str -> API endpoint
            requestType: RequestType -> request type
            parameters: Optional[dict[str, Any]] -> request parameters (not required)
            headers: Optional[dict[str, str]] -> headers (not required)
            retryCount: int -> number of function calls if request has failed

            Returns:
            NetworkResponse as response content to request
        """

        if headers is None:
            headers = self.__requestHeader()

        if parameters is None:
            parameters = {}

        networkResponse = self.__requestManager.genericRequest(
            requestType = requestType,
            endpoint = endpoint,
            headers = headers,
            data = json.dumps(parameters)
        )

        if self.shouldRetry(retryCount, networkResponse):
            print(">> [MLService] Retry count: {0}".format(retryCount))

            if self.__apiToken is not None:
                headers[self.apiTokenHeaderField] = self.__apiToken

            return self.genericJSONRequest(
                endpoint,
                requestType,
                parameters,
                headers,
                retryCount + 1
            )

        return networkResponse

    def __authenticate(self) -> NetworkResponse:
        # authenticate using credentials stored in requests.Session.auth

        response = self.__requestManager.post(
            endpoint = self.loginEndpoint,
            headers = self.__requestHeader()
        )

        if self.apiTokenKey in response.json:
            self.__apiToken = response.json[self.apiTokenKey]

        if self.refreshTokenKey in response.json:
            self.__refreshToken = response.json[self.refreshTokenKey]

        if not response.hasFailed():
            print(">> [MLService] Login successful")

        return response

    def authenticate(self, username: str, password: str) -> NetworkResponse:
        self.__requestManager.setAuth(username, password)

        # authenticate using credentials stored in requests.Session.auth
        return self.__authenticate()

    def authenticateWithRefreshToken(self, token: str) -> None:
        """
            Authenticates user with provided refresh token
        """

        self.__refreshToken = token
        self.refreshToken()

    def refreshToken(self) -> None:
        """
            Uses refresh token functionality to fetch new API access token
        """

        headers = self.__requestHeader()

        if self.__refreshToken is not None:
            headers[self.apiTokenHeaderField] = self.__refreshToken

        networkResponse = self.__requestManager.genericRequest(
            requestType = RequestType.post,
            endpoint = self.refreshEndpoint,
            headers = headers
        )

        if networkResponse.hasFailed():
            # the following logic should be removed as part of CTX-1659
            # it is needed for node authentication when refresh token issued on startup expires

            # if refresh failed try to login again
            # authResponse = self.authenticate(username = "agent1", password = "Qwebnm11.")
            if not self.__requestManager.isAuthSet:
                raise RuntimeError(">> [Coretex] Cannot login on user/refresh failure. Credentials not available")

            authResponse = self.__authenticate()
            if authResponse.hasFailed():
                # if both login and refresh failed, something is seriously wrong
                raise RuntimeError(">> [Coretex] Failed to login during on user/refresh failure")

            # the following line should be commented out as part of CTX-1659
            # as both node and workspace will use the same refresh token which duration will be enough to cover long running experiments
            # raise RuntimeError(">> [MLService] Failed to do API token refresh")
        elif self.apiTokenKey in networkResponse.json:
            self.__apiToken = networkResponse.json[self.apiTokenKey]
            print(">> [Coretex] API token refresh was successful. API token updated")

    def shouldRetry(self, retryCount: int, response: NetworkResponse) -> bool:
        """
            Checks if network request should be repeated based on the number of repetitions
            as well as the response from previous repetition

            Parameters:
            retryCount: int -> number of repeated function calls
            response: NetworkResponse -> generated response after sending the request

            Returns:
            True if the function call needs to be repeated, False if function was called 3 times or if request has not failed
        """

        # Limit retry count to 3 times
        if retryCount == 3:
            return False

        # If we get unauthorized maybe API token is expired
        if response.isUnauthorized():
            self.refreshToken()
            return True

        return (
            response.statusCode == HttpCode.internalServerError or
            response.statusCode == HttpCode.serviceUnavailable
        )
