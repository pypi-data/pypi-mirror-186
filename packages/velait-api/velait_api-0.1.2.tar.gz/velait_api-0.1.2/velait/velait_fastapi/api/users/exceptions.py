from velait.common.exceptions import VelaitError
from velait.velait_fastapi.connections.exceptions import RequestError


class NotAuthorizedError(RequestError):
    name = "user"
    description = "User is not authorized"
    status_code = 403


class NoPermissionError(VelaitError):
    name = "user"
    description = "User does not have enough permissions"
    status_code = 403


__all__ = ['NotAuthorizedError', 'NoPermissionError']
