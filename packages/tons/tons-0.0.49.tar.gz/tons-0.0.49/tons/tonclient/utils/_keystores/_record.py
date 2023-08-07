from typing import Union, Optional

from pydantic import BaseModel, validator

from tons.tonsdk.contract.wallet import WalletVersionEnum
from tons.tonsdk.utils import Address, InvalidAddressError


class Record(BaseModel):
    name: str
    address: Union[str, Address]
    version: WalletVersionEnum
    workchain: int
    subwallet_id: Optional[int]
    public_key: str
    secret_key: str
    comment: Optional[str] = ""

    class Config:
        use_enum_values = True
        validate_assignment = True
        arbitrary_types_allowed = True

    @validator('address')
    def validate_address(cls, v, values, **kwargs):
        if v:
            if isinstance(v, Address):
                return v.to_string(False, False, False)

            try:
                addr = Address(v)
                return addr.to_string(False, False, False)

            except InvalidAddressError as e:
                raise ValueError(e)

    @property
    def address_to_show(self):
        return Address(self.address).to_string(True, True, True)
