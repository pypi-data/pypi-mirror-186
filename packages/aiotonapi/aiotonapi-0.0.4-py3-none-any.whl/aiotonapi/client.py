import aiohttp

from .exceptions import TonapiError, TonapiUnauthorized, TonapiException

BASE_URL = "https://tonapi.io/{method}"
TESTNET_BASE_URL = "https://testnet.tonapi.io/{method}"


class TonapiClient:
    __slots__ = ("_api_key", "_testnet", "__headers", "__base_url")

    def __init__(self, api_key: str, testnet: bool = False):
        self._api_key = api_key
        self._testnet = testnet

        self.__headers = {'Authorization': 'Bearer ' + api_key}
        self.__base_url = TESTNET_BASE_URL if testnet else BASE_URL

    async def _method(self, method: str, params: dict = None):
        params = params.copy() if params is not None else {}

        async with aiohttp.ClientSession(headers=self.__headers) as session:
            response = await session.get(url=self.__base_url.format(
                method=method), params=params)
            json_response = await response.json()

            match response.status:
                case 200:
                    return json_response
                case 400:
                    error = json_response.get("error")
                    raise TonapiError(error)
                case 401:
                    raise TonapiUnauthorized
                case _:
                    raise TonapiException(json_response)
