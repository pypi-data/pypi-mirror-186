from tap import Tap
from typing import Tuple

from .base import WorkspaceCallback
from ..networking import NetworkManager


class RemoteArgumentParser(Tap):

    refreshToken: str
    experimentId: int

    def configure(self) -> None:
        self.add_argument("--refreshToken", type = str)
        self.add_argument("--experimentId", type = int)


def processRemote() -> Tuple[int, WorkspaceCallback]:
    remoteArgumentParser = RemoteArgumentParser().parse_args()

    NetworkManager.instance().authenticateWithRefreshToken(remoteArgumentParser.refreshToken)

    return remoteArgumentParser.experimentId, WorkspaceCallback.create(remoteArgumentParser.experimentId)
