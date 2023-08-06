from ..client import TonapiClient
from ..types import AccountRepr, AccountReprs


class AccountMethod(TonapiClient):

    async def get_bulk_info(self, addresses: list[str]) -> AccountReprs:
        """
        Get info about few accounts account by one request.

        :param addresses: Account addresses in
         raw (hex without 0x) or base64url format.
        :return: AccountReprs object.
        """
        params = {'addresses': ','.join(map(str, addresses))}
        response = await self._method('v1/account/getInfo', params=params)

        return AccountReprs(**response)

    async def get_info(self, account: str) -> AccountRepr:
        """
        Get info about account.

        :param account: address in raw (hex without 0x)
         or base64url format.
        :return: AccountRepr object.
        """
        params = {'account': account}
        response = await self._method('v1/account/getInfo', params=params)

        return AccountRepr(**response)
