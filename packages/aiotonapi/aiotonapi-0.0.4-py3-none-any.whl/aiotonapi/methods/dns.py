from ..client import TonapiClient
from ..types import DnsRecord, DomainNames, DomainInfo


class DNSMethod(TonapiClient):

    async def backresolve(self, account: str) -> DomainNames:
        """
        DNS back resolve for wallet address.

        :param account: Address in raw (hex without 0x) or base64url format.
        :return:
        """
        params = {'account': account}
        response = await self._method('v1/dns/backresolve', params=params)

        return DomainNames(**response)

    async def domains_search(self, domain: str) -> DomainNames:
        """
        Search domains by the first letters.

        :param domain:
        :return: DomainNames object.
        """
        params = {'domain': domain}
        response = await self._method('v1/dns/domains/search', params=params)

        return DomainNames(**response)

    async def get_info(self, name: str) -> DomainInfo:
        """
        Domain info.

        :param name: Domain name with .ton or .t.me
        :return:
        """
        params = {'name': name}
        response = await self._method('v1/dns/getInfo', params=params)

        return DomainInfo(**response)

    async def resolve(self, name: str) -> DnsRecord:
        """
        DNS resolve for domain name.

        :param name: domain name with .ton
        :return:
        """
        params = {'name': name}
        response = await self._method('v1/dns/resolve', params=params)

        return DnsRecord(**response)
