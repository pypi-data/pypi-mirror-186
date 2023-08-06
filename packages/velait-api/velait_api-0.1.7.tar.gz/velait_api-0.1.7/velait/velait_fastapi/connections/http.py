import aiohttp
from aiohttp import ClientError

from velait.velait_fastapi.connections.exceptions import RequestError


class HTTPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def request(self, url, method, headers=None):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.request(method, f"{self.base_url}{url}", headers=headers) as response:
                    if not response.ok:
                        raise RequestError(name="request", description=response.reason, status_code=response.status)

                    return await response.json()
            except ClientError:
                raise RequestError(name="request", description="Unknown request error")


__all__ = [
    'HTTPClient',
    'RequestError',
]
