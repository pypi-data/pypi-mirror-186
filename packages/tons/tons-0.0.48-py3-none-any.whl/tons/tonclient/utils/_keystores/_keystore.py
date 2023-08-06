import json
import os
from hashlib import sha256
from typing import List, Union, Optional, Dict

from nacl.bindings import crypto_box_seed_keypair, crypto_box, crypto_box_open
from pydantic import BaseModel

from tons import settings
from tons.tonsdk.contract.wallet import WalletVersionEnum
from tons.tonsdk.crypto import generate_new_keystore, generate_keystore_key
from tons.tonsdk.utils import Address
from tons.tonsdk.utils._utils import default_subwallet_id
from tons.utils import storage
from ._record import Record
from .._exceptions import InvalidKeyStoreError, RecordAlreadyExistsError, KeyStoreInvalidPasswordError, \
    RecordDoesNotExistError


class KeyStore(BaseModel):
    filepath: str
    salt: str = ""
    public_key: str = ""
    version: int = settings.CURRENT_KEYSTORE_VERSION
    records: List[Record] = []

    class Config:
        use_enum_values = True
        validate_assignment = True

    @classmethod
    def new(cls, filepath: str, password: str) -> 'KeyStore':
        data = generate_new_keystore(password)
        data["filepath"] = filepath
        return cls.parse_obj(data)

    @classmethod
    def load(cls, filepath) -> 'KeyStore':
        raw_data = storage.read_bytes(filepath)
        if len(raw_data) < 32:
            raise InvalidKeyStoreError(f"Broken keystore: {filepath}")

        hash_data = raw_data[:32]
        data = raw_data[32:]
        if hash_data != sha256(data).digest():
            raise InvalidKeyStoreError(f"Broken keystore: {filepath}")

        json_data = json.loads(data.decode('utf-8'))
        json_data["filepath"] = filepath
        current_version = json_data["version"]
        if current_version != settings.CURRENT_KEYSTORE_VERSION:
            json_data = cls.upgrade_from_old_version(current_version, json_data)

        keystore = cls.parse_obj(json_data)
        if current_version != settings.CURRENT_KEYSTORE_VERSION:
            keystore.save()
        return keystore

    def save(self):
        self.records = sorted(self.records, key=lambda record: record.name.lower())
        json_data = json.dumps(self.dict(exclude={'filepath'})).encode('utf-8')
        hash_of_data = sha256(json_data).digest()
        storage.save_bytes(self.filepath, hash_of_data + json_data)

    @classmethod
    def upgrade_from_old_version(cls, version, json_data) -> Dict:
        if version == 1:
            for record in json_data["records"]:
                record["subwallet_id"] = None

                if record["version"] in WalletVersionEnum.with_subwallet_id():
                    record["subwallet_id"] = default_subwallet_id(record["workchain"])

            version += 1

        json_data["version"] = version
        return json_data

    def get_record_by_name(self, name: str, raise_none: bool = False):
        return self.__get_record(name=name, raise_none=raise_none)

    def get_record_by_address(self, address: Union[str, Address], raise_none: bool = False):
        return self.__get_record(address=address, raise_none=raise_none)

    def edit_record(self, name: str, new_name: str, new_comment: str, save: bool = False):
        record = self.get_record_by_name(name, raise_none=True)
        record_idx = self.records.index(record)

        if new_name:
            self.records[record_idx].name = new_name

        if new_comment:
            self.records[record_idx].comment = new_comment

        if save:
            self.save()

    def delete_record(self, name: str, save: bool = False) -> Record:
        record = self.get_record_by_name(name, raise_none=True)
        self.records.remove(record)

        if save:
            self.save()

        return record

    def add_record(self, name: str, address: Address, public_key: str,
                   mnemonics: List[str], version: WalletVersionEnum,
                   workchain: int, subwallet_id: Optional[int] = None,
                   comment: Optional[str] = None, password: Optional[str] = None, save=False):
        if self.__get_record(name=name, address=address) is not None:
            raise RecordAlreadyExistsError(
                f"Record with the name '{name}' or address: '{address.to_string(True, True, True)}' already exists")

        key = (" ".join(mnemonics)).encode('utf-8')
        sk = self.__create_record_sk(key)

        new_record = Record(name=name, address=address,
                            version=version, workchain=workchain, subwallet_id=subwallet_id,
                            comment=comment, public_key=public_key, secret_key=sk.hex())
        self.records.append(new_record)

        if save:
            self.save()

    def get_secret(self, record: Record, password: str) -> str:
        src = bytes.fromhex(record.secret_key)
        nonce, public_key, data = src[:24], src[24:24 + 32], src[24 + 32:]

        pub_k, priv_k = generate_keystore_key(
            password, bytes.fromhex(self.salt))
        if pub_k != bytes.fromhex(self.public_key):
            raise KeyStoreInvalidPasswordError("Invalid keystore password.")

        decoded_key_bytes = crypto_box_open(data, nonce, public_key, priv_k)
        if not decoded_key_bytes:
            raise KeyStoreInvalidPasswordError("Invalid keystore password.")

        return decoded_key_bytes.decode("utf-8")

    def __create_record_sk(self, key: bytes) -> bytes:
        ephemeral_key_public, ephemeral_key_secret = crypto_box_seed_keypair(
            os.urandom(32))
        nonce = os.urandom(24)
        encrypted = crypto_box(key, nonce, bytes.fromhex(
            self.public_key), ephemeral_key_secret)

        return nonce + ephemeral_key_public + encrypted

    def __get_record(self, name: Optional[str] = None, address: Union[str, Address, None] = None,
                     raise_none: bool = False) -> Optional[Record]:
        record = None

        if name:
            record = next(
                (record for record in self.records if record.name == name), record)
            if record is None and raise_none:
                raise RecordDoesNotExistError(
                    f"Record with the name {name} does not exist")

        if address:
            address = address if isinstance(
                address, str) else address.to_string(False, False, False)
            record = next(
                (record for record in self.records if record.address == address), record)
            if record is None and raise_none:
                raise RecordDoesNotExistError(
                    f"Record with the address {address} does not exist")

        return record
