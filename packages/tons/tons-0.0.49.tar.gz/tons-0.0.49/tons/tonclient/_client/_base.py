from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from tons.config import Config
from tons.tonsdk.contract.wallet import SendModeEnum, WalletContract
from tons.tonsdk.utils import TonCurrencyEnum


class AddressInfoResult(BaseModel):
    address: Optional[str] = None
    contract_type: Optional[str] = None
    seqno: Optional[str] = None
    state: Optional[str] = None
    balance: Optional[float] = None
    last_activity: Optional[str] = None
    code: Optional[str] = None
    data: Optional[str] = None


class BroadcastStatusEnum(str, Enum):
    broadcasted = "broadcasted"
    commited = "commited"
    failed = "failed"


class BroadcastResult(BaseModel):
    waited: bool
    status: BroadcastStatusEnum

    class Config:
        use_enum_values = True
        validate_assignment = True

    def __str__(self):
        if self.status == BroadcastStatusEnum.commited:
            return "Transaction has been commited."

        if self.status == BroadcastStatusEnum.broadcasted:
            if self.waited:
                return "Transaction has been sent but hasn't been committed into blockchain during 30 seconds."
            else:
                return "Transaction has been sent."

        return "Transaction hasn't been sent."


class TonClient(ABC):
    @abstractmethod
    def __init__(self, config: Config):
        raise NotImplementedError

    @abstractmethod
    def get_address_information(self, address: str,
                                currency_to_show: TonCurrencyEnum = TonCurrencyEnum.ton) -> AddressInfoResult:
        raise NotImplementedError

    @abstractmethod
    def get_addresses_information(self, addresses: List[str],
                                  currency_to_show: TonCurrencyEnum = TonCurrencyEnum.ton) -> List[
        AddressInfoResult]:
        raise NotImplementedError

    @abstractmethod
    def seqno(self, addr: str) -> int:
        raise NotImplementedError

    @abstractmethod
    def deploy_wallet(self, wallet: WalletContract, wait_for_result=False) -> BroadcastResult:
        raise NotImplementedError

    @abstractmethod
    def transfer(self, from_wallet: WalletContract, to_addr: str,
                 amount: TonCurrencyEnum.ton, payload=None,
                 send_mode=SendModeEnum.ignore_errors | SendModeEnum.pay_gas_separately,
                 is_bounceable=True, wait_for_result=False, state_init=None) -> BroadcastResult:
        raise NotImplementedError

    @abstractmethod
    def send_boc(self, boc: bytes, wait_for_result: bool) -> BroadcastResult:
        raise NotImplementedError
