import os
from enum import Enum
from typing import Optional

from pydantic import BaseModel, validator

from tons import settings
from tons.tonsdk.contract.wallet import WalletVersionEnum


class TonProviderEnum(str, Enum):
    dapp = "dapp"


class TonsConfig(BaseModel):
    workdir: Optional[str]
    whitelist_path: Optional[str]
    keystore_name: Optional[str] = None
    provider: TonProviderEnum = TonProviderEnum.dapp
    default_wallet_version: WalletVersionEnum = WalletVersionEnum.v3r2
    warn_if_outdated: bool = True

    class Config:
        use_enum_values = True
        validate_assignment = True

    @validator("workdir", always=True)
    def __validate_workdir(cls, v, values):
        if v:
            return v

        return settings.CURRENT_WORKDIR

    @validator("keystore_name", always=True)
    def __validate_keystore_name(cls, v, values):
        if v:
            if not v.endswith(".keystore"):
                v += ".keystore"

        return v

    @property
    def whitelist_path(self):
        return os.path.join(self.workdir, "whitelist.json")

    @property
    def keystores_path(self):
        return os.path.join(self.workdir, "keystores")
