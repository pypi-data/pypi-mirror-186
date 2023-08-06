from typing import Optional, Union, List, Dict

from pydantic import BaseModel

from tons import settings
from tons.tonsdk.contract.wallet import WalletVersionEnum
from tons.tonsdk.utils import Address
from ._keystore import KeyStore
from ._record import Record


class TonCliRecordBackup(BaseModel):
    name: str
    comment: Optional[str] = ""
    config: str
    kind: str
    address: Union[str, Address]
    mnemonics: List[str]

    class Config:
        use_enum_values = True
        validate_assignment = True
        arbitrary_types_allowed = True

    def to_backup_record(self) -> Optional["RecordBackup"]:
        if not self.__supported_wallet():
            return None

        return RecordBackup(name=self.name, address=self.address,
                            version=self.__map_kind_to_version(),
                            workchain=int(self.__map_config_to_workchain()),
                            subwallet_id=int(self.__map_config_to_subwallet_id()),
                            mnemonics=" ".join(self.mnemonics), comment=self.comment)

    def __supported_wallet(self):
        return self.kind in self.kind_version_map.keys()

    def __map_kind_to_version(self):
        return self.kind_version_map[self.kind]

    def __map_config_to_workchain(self):
        # "wc=0,walletId=698983191,pk=qweqweqwe"
        return self.config.split(",")[0].split("=")[1]

    def __map_config_to_subwallet_id(self):
        return self.config.split(",")[1].split("=")[1]

    @property
    def kind_version_map(self) -> Dict:
        return {
            "org.ton.wallets.v2": WalletVersionEnum.v2r1,
            "org.ton.wallets.v2.r2": WalletVersionEnum.v2r2,
            "org.ton.wallets.v3": WalletVersionEnum.v3r1,
            "org.ton.wallets.v3.r2": WalletVersionEnum.v3r2,
        }


class RecordBackup(BaseModel):
    name: str
    address: Union[str, Address]
    version: WalletVersionEnum
    workchain: int
    subwallet_id: Optional[int]
    mnemonics: str
    comment: Optional[str] = ""

    class Config:
        use_enum_values = True
        validate_assignment = True
        arbitrary_types_allowed = True

    @classmethod
    def from_record(cls, record: "Record", mnemonics: str) -> "RecordBackup":
        return cls(
            name=record.name,
            address=record.address,
            version=record.version,
            workchain=record.workchain,
            subwallet_id=record.subwallet_id,
            mnemonics=mnemonics,
            comment=record.comment,
        )


class KeystoreBackup(BaseModel):
    version: int = settings.CURRENT_KEYSTORE_VERSION
    records: List[RecordBackup]

    @classmethod
    def backup_json(cls, keystore: KeyStore, filepath: str, password: str) -> Dict:
        records: List[RecordBackup] = []
        for record in keystore.records:
            mnemonics = keystore.get_secret(record, password)
            records.append(RecordBackup.from_record(record, mnemonics))

        return cls(records=records).dict()

    @classmethod
    def restore_from_tons(cls, json_data: Dict) -> 'KeystoreBackup':
        records: List[RecordBackup] = []
        # todo: check version and update records if required

        version = 1 if "version" not in json_data else json_data["version"]

        if version == 1:
            version += 1
            raw_records = json_data
        else:
            raw_records = json_data['records']

        for raw_record in raw_records:
            records.append(RecordBackup.parse_obj(raw_record))

        assert version == settings.CURRENT_KEYSTORE_VERSION
        return cls(records=records)

    @classmethod
    def restore_from_ton_cli(cls, json_data: Dict) -> 'KeystoreBackup':
        records: List[RecordBackup] = []
        for raw_record in json_data:
            backup_record = TonCliRecordBackup.parse_obj(
                raw_record).to_backup_record()
            if backup_record:
                records.append(backup_record)

        return cls(records=records)
