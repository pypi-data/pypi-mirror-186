import json
import os
from typing import Optional, Tuple

from tons.tonsdk.contract.wallet import Wallets
from tons.utils import storage
from ._backup import KeystoreBackup, RecordBackup, TonCliRecordBackup
from ._keystore import KeyStore
from .._exceptions import KeyStoreAlreadyExistsError, \
    KeyStoreDoesNotExistError, InvalidKeyStoreError, \
    KeyStoreIsNotSpecifiedError


class KeyStores:
    def __init__(self, keystores_workdir: str):
        self.keystores_workdir = keystores_workdir

        paths = storage.get_filenames_by_ptrn(
            keystores_workdir, "*.keystore")
        self.keystore_paths = {os.path.basename(path): path for path in paths}
        self._keystore_path = None

    def create_new_keystore(self, name: str, password: Optional[str] = None, save: bool = False) \
            -> Tuple[KeyStore, str]:
        name = self.__keystore_name(name)

        if name in self.keystore_paths:
            raise KeyStoreAlreadyExistsError(
                f"Keystore with the name '{name}' already exists")

        if password is None:
            # TODO: generate password
            raise NotImplemented("Empty password is not supported")

        filepath = os.path.join(self.keystores_workdir, name)
        keystore = KeyStore.new(filepath=filepath, password=password)
        if save:
            keystore.save()

        self.keystore_paths[name] = keystore.filepath

        return keystore, password

    def get_keystore(self, keystore_name: Optional[str], raise_none: bool = False) -> Optional[KeyStore]:
        if keystore_name is None:
            raise KeyStoreIsNotSpecifiedError(
                "tons.keystore_name is not specified.")

        keystore_path = os.path.join(self.keystores_workdir, keystore_name)
        try:
            return KeyStore.load(keystore_path)

        except FileNotFoundError:
            if raise_none:
                raise KeyStoreDoesNotExistError(
                    f"Keystore with the name '{keystore_name}' does not exist.")

            return None

        except json.JSONDecodeError as e:
            raise InvalidKeyStoreError("Invalid keystore file. " + str(e))

    def backup_keystore(self, keystore: KeyStore, filepath: str, password: str):
        storage.save_json(filepath, KeystoreBackup.backup_json(keystore, filepath, password))

    def restore_tons_keystore(self, name: str, filepath: str, password: Optional[str] = None):
        json_data = storage.read_json(filepath)
        self.__restore_keystore(name, filepath, password,
                                KeystoreBackup.restore_from_tons(json_data))

    def restore_ton_cli_keystore(self, name: str, filepath: str, password: Optional[str] = None):
        json_data = storage.read_json(filepath)
        self.__restore_keystore(name, filepath, password,
                                KeystoreBackup.restore_from_ton_cli(json_data))

    def __restore_keystore(self, name: str, filepath: str, password: str,
                           keystore_backup: KeystoreBackup):
        name = self.__keystore_name(name)

        keystore, _password = self.create_new_keystore(
            name, password, save=False)

        for backup_record in keystore_backup.records:
            mnemonics, pub_k, _priv_k, wallet = Wallets.from_mnemonics(
                backup_record.mnemonics.split(" "), backup_record.version,
                backup_record.workchain, backup_record.subwallet_id)

            keystore.add_record(backup_record.name, wallet.address,
                                pub_k.hex(), mnemonics, backup_record.version,
                                backup_record.workchain, backup_record.subwallet_id,
                                backup_record.comment, save=False)
        keystore.save()

        self.keystore_paths[name] = keystore.filepath

    def __keystore_name(self, name):
        if not name.endswith(".keystore"):
            name += ".keystore"
        return name


__all__ = [
    "KeyStores",
    "KeyStore",
]
