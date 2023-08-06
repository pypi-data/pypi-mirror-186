from .client import TonapiClient

from .methods.account import AccountMethod
from .methods.domain_auctions import DomainAuctionsMethod
from .methods.dns import DNSMethod
from .methods.event import EventMethod
from .methods.jetton import JettonMethod
from .methods.nft import NftMethod
from .methods.raw_blockchain import RawBlockchainMethod


class Tonapi(TonapiClient):
    def __init__(self, api_key: str, testnet: bool = False):
        """
        :param api_key: Secret key from https://t.me/tonapi_bot
        :param testnet: Use true, if you want to switch to testnet
        """
        super().__init__(api_key, testnet)

    @property
    def account(self): return AccountMethod(self._api_key, self._testnet)

    @property
    def domain_auctions(self): return DomainAuctionsMethod(self._api_key, self._testnet)

    @property
    def dns(self): return DNSMethod(self._api_key, self._testnet)

    @property
    def event(self): return EventMethod(self._api_key, self._testnet)

    @property
    def jetton(self): return JettonMethod(self._api_key, self._testnet)

    @property
    def nft(self): return NftMethod(self._api_key, self._testnet)

    @property
    def raw_blockchain(self): return RawBlockchainMethod(self._api_key, self._testnet)


__all__ = (
    "Tonapi",
    "AccountMethod",
    "DNSMethod",
    "EventMethod",
    "JettonMethod",
    "NftMethod",
    "RawBlockchainMethod",
)
