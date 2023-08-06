from ..client import TonapiClient
from ..types import JettonBalances, AccountEvents, JettonInfo


class JettonMethod(TonapiClient):

    async def get_balances(self, account: str) -> JettonBalances:
        """
        Get all Jettons balances by owner address.

        :param account: Address in raw (hex without 0x) or base64url format.
        :return: JettonBalances object.
        """
        params = {'account': account}
        response = await self._method('v1/jetton/getBalances', params=params)

        return JettonBalances(**response)

    async def get_history(self, account: str, jetton_master: str,
                          limit: int = 1000) -> AccountEvents:
        """
        Get all Jetton transfers for account.

        :param account: Address in raw (hex without 0x) or base64url format.
        :param jetton_master: Address in raw (hex without 0x) or base64url format.
        :param limit: Default value 1000
        :return: AccountEvents object.
        """
        params = {
            'account': account,
            'jetton_master': jetton_master,
            'limit': limit,
        }
        response = await self._method('v1/jetton/getHistory', params=params)

        return AccountEvents(**response)

    async def get_info(self, account: str) -> JettonInfo:
        """
        Get jetton metadata by jetton master address.

        :param account: Address in raw (hex without 0x) or base64url format.
        :return: JettonInfo object.
        """
        params = {
            'account': account,
        }
        response = await self._method('v1/jetton/getInfo', params=params)

        return JettonInfo(**response)
