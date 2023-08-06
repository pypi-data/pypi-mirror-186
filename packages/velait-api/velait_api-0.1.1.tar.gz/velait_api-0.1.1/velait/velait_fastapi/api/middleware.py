from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from assimilator.core.database.exceptions import InvalidQueryError, NotFoundError

from velait.common.services.search import SearchError
from velait.velait_fastapi.api.responses import APIResponse, ResponseErrorItem
from velait.velait_fastapi.api.users.exceptions import NotAuthorizedError
from velait.velait_fastapi.api.users.permissions import NoPermissionError
from velait.common.exceptions import AlreadyDeletedError


class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
        except NotFoundError:
            return APIResponse(status_code=404, errors=[
                ResponseErrorItem(name="obj", description="Not found")
            ])
        except InvalidQueryError:
            return APIResponse(status_code=400, errors=[
                ResponseErrorItem(name="obj", description="Invalid request data")
            ])
        except (NotAuthorizedError, NoPermissionError, SearchError, AlreadyDeletedError) as exc:
            return APIResponse(status_code=exc.status_code, errors=[
                ResponseErrorItem(name=exc.name, description=exc.description)
            ])

        return response


__all__ = [
    'ExceptionHandlerMiddleware',
]
