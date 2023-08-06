from enum import Enum


class RequestType(Enum):

    get = "GET"
    post = "POST"
    put = "PUT"
    delete = 'DELETE'
