from ..client import TonapiClient
from ..types import Account, Transactions, Transaction, Block, Validators


class RawBlockchainMethod(TonapiClient):

    async def get_account(self, account: str) -> Account:
        """
        Get raw account data.

        :param account: address in raw (hex without 0x)
         or base64url format.
        :return: Account object.
        """
        params = {'account': account}
        response = await self._method('v1/blockchain/getAccount', params=params)

        return Account(**response)

    async def get_block(self, block_id: str) -> Block:
        """
        Get block by id.

        :param block_id: block id.
        :return: Block object.
        """
        params = {
            'block_id': block_id,
        }
        response = await self._method('v1/blockchain/getBlock', params=params)

        return Block(**response)

    async def get_transaction(self, hash_: str) -> Transaction:
        """
        Get transaction by hash.

        :param hash_: Transaction hash in hex (without 0x) or base64url format.
        :return: Transaction object.
        """
        params = {
            'hash': hash_,
        }
        response = await self._method('v1/blockchain/getTransaction', params=params)

        return Transaction(**response)

    async def get_transactions(self, account: str, max_lt: int = None,
                               min_lt: int = None, limit: int = 100
                               ) -> Transactions:
        """
        Get transactions.

        :param account: Address in raw (hex without 0x) or base64url format.
        :param max_lt: Omit this parameter to get last transactions.
        :param min_lt: Omit this parameter to get last transactions.
        :param limit: Default value : 100
        :return: Transactions object.
        """

        params = {
            'account': account,
            'limit': limit,
        }
        if max_lt: params['maxLt'] = max_lt
        if min_lt: params['minLt'] = min_lt

        response = await self._method('v1/blockchain/getTransactions', params=params)

        return Transactions(**response)

    async def validators(self) -> Validators:
        """
        Get validators info list.

        :return: Validators object.
        """
        response = await self._method('v1/blockchain/validators')

        return Validators(**response)
