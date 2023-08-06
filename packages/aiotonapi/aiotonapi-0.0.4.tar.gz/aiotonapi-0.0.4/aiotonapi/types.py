from __future__ import annotations

from pydantic import BaseModel, Field

from .utils import raw_to_userfriendly, userfriendly_to_raw, nano_to_amount


class Address(BaseModel):
    __root__: str

    def __str__(self):
        return self.__root__

    def to_userfriendly(self):
        return raw_to_userfriendly(self.__root__)

    def to_raw(self):
        return userfriendly_to_raw(self.__root__)


class Value(BaseModel):
    __root__: int

    def __str__(self):
        return self.__root__.__str__()

    def to_amount(self, precision: int = 2):
        """
        :param precision: Number of digits after floating point
        """
        return nano_to_amount(self.__root__, precision=precision)

    def to_nano(self):
        return self.__root__


class AccountR(BaseModel):
    bounceable: str
    non_bounceable: str
    raw: str


class AccountRepr(BaseModel):
    address: AccountR
    balance: Value
    icon: None | str
    interfaces: list[str]
    is_scam: bool
    last_update: int
    memo_required: bool
    name: None | str
    status: str


class AccountReprs(BaseModel):
    accounts: list[AccountRepr]


class Account(BaseModel):
    balance: Value
    code: None | str
    data: None | str
    status: str


class AccountAddress(BaseModel):
    address: Address
    icon: None | str
    is_scam: bool
    name: None | str


class DomainBid(BaseModel):
    bidder: AccountAddress
    success: bool
    tx_hash: str = Field(alias="txHash")
    tx_time: int = Field(alias="txTime")
    value: int


class DomainBids(BaseModel):
    data: list[DomainBid]


class Auction(BaseModel):
    bids: int
    date: int
    domain: str
    owner: str
    price: int


class Auctions(BaseModel):
    data: list[Auction]
    total: int


class NftCollection(BaseModel):
    address: Address
    metadata: None | dict
    next_item_index: int
    owner: None | AccountAddress
    raw_collection_content: str


class NftCollections(BaseModel):
    nft_collections: list[NftCollection]


class Price(BaseModel):
    token_name: str
    value: Value


class Sale(BaseModel):
    address: Address
    market: AccountAddress
    owner: None | AccountAddress
    price: Price


class ImagePreview(BaseModel):
    resolution: str
    url: str


class CollectionAddress(BaseModel):
    address: str
    name: str


class NftItem(BaseModel):
    address: str
    owner: None | AccountAddress


class NftItemRepr(BaseModel):
    address: Address
    collection: None | CollectionAddress
    dns: None | str
    index: int
    metadata: None | dict
    owner: None | AccountAddress
    previews: None | list[ImagePreview]
    sale: None | Sale
    verified: bool


class NftItemsRepr(BaseModel):
    nft_items: list[NftItemRepr]


class MsgData(BaseModel):
    __root__: str

    def __str__(self):
        return self.__root__

    def to_text(self):
        try:
            import base64
            return base64.b64decode(self.__root__).strip(b"\x00").decode('utf-8')
        except UnicodeDecodeError:
            return None


class Message(BaseModel):
    created_lt: int
    destination: None | AccountAddress
    fwd_fee: int
    ihr_fee: int
    msg_data: MsgData
    source: None | AccountAddress
    value: Value


class Transaction(BaseModel):
    account: AccountAddress
    data: str
    fee: int
    hash: str
    in_msg: None | Message
    lt: int
    other_fee: int
    out_msgs: list[Message]
    storage_fee: int
    utime: int


class Transactions(BaseModel):
    transactions: list[Transaction]


class WalletDNS(BaseModel):
    address: Address
    has_method_pubkey: bool
    has_method_seqno: bool
    is_wallet: bool
    names: None | list[str]


class DnsRecord(BaseModel):
    next_resolver: None | str
    site: None | list[str]
    wallet: None | WalletDNS


class DomainNames(BaseModel):
    names: list[str]


class DomainInfo(BaseModel):
    expiration: int
    nft_item: None | NftItem


class Block(BaseModel):
    end_lt: int
    file_hash: str
    root_hash: str
    seqno: int
    shard: str
    start_lt: int
    workchain_id: int


class Validator(BaseModel):
    address: str
    adnl_address: str = Field(alias="adnlAddress")
    max_factor: int = Field(alias="maxFactor")
    stake: int


class Validators(BaseModel):
    elect_at: int = Field(alias="electAt")
    elect_close: int = Field(alias="electClose")
    min_stake: int = Field(alias="minStake")
    total_stake: int = Field(alias="totalStake")
    validators: list[Validator]


class Jetton(BaseModel):
    address: str
    decimals: int
    image: None | str
    name: str
    symbol: str


class JettonBalance(BaseModel):
    balance: str
    jetton_address: str
    metadata: None | Jetton
    wallet_address: AccountAddress


class JettonBalances(BaseModel):
    balances: list[JettonBalance]


class JettonMetadata(BaseModel):
    address: str
    catalogs: None | list[str]
    decimals: int
    description: None | str
    image: None | str
    name: str
    social: None | list[str]
    symbol: str
    websites: None | list[str]


class JettonInfo(BaseModel):
    metadata: JettonMetadata
    mintable: bool
    total_supply: str


class Fee(BaseModel):
    account: AccountAddress
    deposit: int
    gas: int
    refund: int
    rent: int
    total: int


class Refund(BaseModel):
    origin: str
    type: str


class ActionSimplePreview(BaseModel):
    full_description: str
    image: None | str
    name: str
    short_description: str


class UnSubscriptionAction(BaseModel):
    beneficiary: AccountAddress
    subscriber: AccountAddress
    subscription: str


class TonTransferAction(BaseModel):
    amount: int
    comment: None | str
    payload: None | str
    recipient: AccountAddress
    refund: None | Refund
    sender: AccountAddress


class SubscriptionAction(BaseModel):
    amount: int
    beneficiary: AccountAddress
    initial: bool
    subscriber: AccountAddress
    subscription: str


class NftPurchase(BaseModel):
    amount: Price
    buyer: AccountAddress
    nft: NftItemRepr
    purchase_type: None | str
    seller: AccountAddress


class NftItemTransferAction(BaseModel):
    comment: None | str
    nft: str
    payload: None | str
    recipient: None | AccountAddress
    refund: None | Refund
    sender: None | AccountAddress


class JettonTransferAction(BaseModel):
    amount: str
    comment: None | str
    jetton: Jetton
    recipient: None | AccountAddress
    recipients_wallet: str
    refund: None | Refund
    sender: None | AccountAddress
    senders_wallet: str


class ContractDeployAction(BaseModel):
    address: str
    deployer: AccountAddress
    interfaces: list[str]


class AuctionBidAction(BaseModel):
    amount: Price
    auction_type: str
    beneficiary: AccountAddress
    bidder: AccountAddress
    nft: None | NftItemRepr


class Action(BaseModel):
    auction_bid: None | AuctionBidAction = Field(alias="AuctionBid")
    contract_deploy: None | ContractDeployAction = Field(alias="ContractDeploy")
    jetton_transfer: None | JettonTransferAction = Field(alias="JettonTransfer")
    nft_item_transfer: None | NftItemTransferAction = Field(alias="NftItemTransfer")
    nft_purchase: None | NftPurchase = Field(alias="NftPurchase")
    subscribe: None | SubscriptionAction = Field(alias="Subscribe")
    ton_transfer: None | TonTransferAction = Field(alias="TonTransfer")
    un_subscribe: None | UnSubscriptionAction = Field(alias="UnSubscribe")
    simple_preview: None | ActionSimplePreview
    status: str
    type: str


class AccountEvent(BaseModel):
    account: AccountAddress
    action: list[Action]
    event_id: str
    fee: Fee
    in_progress: bool
    is_scam: bool
    lt: int
    timestamp: int


class AccountEvents(BaseModel):
    events: list[AccountEvent]
    next_from: int


class Event(BaseModel):
    actions: list[Action]
    event_id: str
    fees: list[Fee]
    in_progress: bool
    is_scam: bool
    lt: int
    timestamp: int
