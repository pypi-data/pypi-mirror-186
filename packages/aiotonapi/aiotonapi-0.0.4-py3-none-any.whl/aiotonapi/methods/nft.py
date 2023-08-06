from ..client import TonapiClient
from ..types import NftItemsRepr, NftCollection, NftCollections


class NftMethod(TonapiClient):

    async def get_collection(self, account: str) -> NftCollection:
        """
        Get NFT collection by collection address.

        :param account: Address in raw (hex without 0x) or base64url format.
        :return: NftCollection object.
        """
        params = {'account': account}
        response = await self._method('/v1/nft/getCollection', params=params)

        return NftCollection(**response)

    async def get_collections(self, limit: int = 15, offset: int = 0) -> NftCollections:
        """
        Get all NFT collections.

        :param limit: Default value : 15
        :param offset: Default value : 0
        :return: NftCollections object.
        """
        params = {
            'limit': limit,
            'offset': offset
        }
        response = await self._method('/v1/nft/getCollections', params=params)

        return NftCollections(**response)

    async def get_items(self, addresses: list[str]) -> NftItemsRepr:
        """
        Get NFT items by addresses.

        :param addresses: NFT items addresses in raw
         (hex without 0x) or base64url format.
        :return: NftItemsRepr object.
        """
        params = {'addresses': ','.join(map(str, addresses))}
        response = await self._method('v1/nft/getItems', params=params)

        return NftItemsRepr(**response)

    async def search_items(self, owner: str = None, collection: str = None,
                           include_on_sale: bool = False, limit: int = 100,
                           offset: int = 0) -> NftItemsRepr:
        """
        Search NFT items using filters.

        :param owner: address in raw (hex without 0x) or base64url
         format or word 'no' for items without owner.
        :param collection: address in raw (hex without 0x)
         or base64url format or word 'no' for items without collection.
        :param include_on_sale: Default value false. Include nft items which
         are currently are on market.
        :param limit: Default value 100. Maximum qty of items.
        :param offset: Default value 0. Offset for pagination.
        :return: NftItemsRepr object.
        """
        params = {
            'include_on_sale': 'true' if include_on_sale else 'false',
            'limit': limit,
            'offset': offset
        }
        if owner: params['owner'] = owner
        if collection: params['collection'] = collection

        response = await self._method('v1/nft/searchItems', params=params)

        return NftItemsRepr(**response)
