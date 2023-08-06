from ..client import TonapiClient
from ..types import DomainBids, Auctions


class DomainAuctionsMethod(TonapiClient):

    async def get_bids(self, domain: str) -> DomainBids:
        """
        Get domain bids.

        :param domain: domain names with .ton
        :return: DomainBids object.
        """
        params = {'domain': domain}
        response = await self._method('v1/auction/getBids', params=params)

        return DomainBids(**response)

    async def get_current(self, tld: str) -> Auctions:
        """
        Get all auctions.

        :param tld: Domain filter for current auctions "ton" or "t.me".
        :return: Auctions object.
        """
        params = {'tld': tld}
        response = await self._method('v1/auction/getCurrent', params=params)

        return Auctions(**response)
