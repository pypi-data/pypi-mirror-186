from enum import Enum
from typing import Optional

from pydantic import BaseModel

from tons import settings


class TonNetworkEnum(str, Enum):
    mainnet = 'mainnet'
    testnet = 'testnet'


class DAppConfig(BaseModel):
    api_key: Optional[str] = None
    network: TonNetworkEnum = TonNetworkEnum.mainnet

    class Config:
        use_enum_values = True
        validate_assignment = True

    @property
    def graphql_url(self):
        if self.network == TonNetworkEnum.mainnet:
            return settings.DAPP_MAINNET_GRAPHQL_URL
        else:
            return settings.DAPP_TESTNET_GRAPHQL_URL

    @property
    def broadcast_url(self):
        if self.network == TonNetworkEnum.mainnet:
            return settings.DAPP_MAINNET_BROADCAST_URL
        else:
            return settings.DAPP_TESTNET_BROADCAST_URL
