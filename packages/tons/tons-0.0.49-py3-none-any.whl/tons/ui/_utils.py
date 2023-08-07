import dataclasses
import math
from typing import Optional
from xmlrpc.client import Boolean

from prettytable import MARKDOWN, PrettyTable

from tons.config import init_config, Config, TonProviderEnum
from tons.tonclient import TonClient, DAppTonClient
from tons.tonclient.utils import KeyStores, Whitelist, KeyStore
from tons.utils import storage
from tons.utils.versioning import tons_is_outdated


@dataclasses.dataclass
class SharedObject:
    config: Config
    ton_client: TonClient
    specific_config_path: Optional[str]
    keystores: Optional[KeyStores] = None
    keystore: Optional[KeyStore] = None
    keystore_password: Optional[str] = None
    whitelist: Optional[Whitelist] = None
    debug_mode: Boolean = False


def init_shared_object(specific_config_path: str = None) -> SharedObject:
    config = init_config(specific_config_path)
    ton_client = get_ton_client(config)

    return SharedObject(
        config=config, specific_config_path=specific_config_path, ton_client=ton_client)


def setup_app(config: Config):
    if config.tons.warn_if_outdated and tons_is_outdated():
        print("\033[93mWarning: tons version is outdated! "
              "Please, update it via 'pip3 install --upgrade tons'\033[0m")

    for default_dir_path in [config.tons.workdir,
                             config.tons.keystores_path]:
        storage.ensure_dir_exists(default_dir_path)


def get_ton_client(config: Config):
    if config.tons.provider == TonProviderEnum.dapp:
        return DAppTonClient(config)
    else:
        raise NotImplementedError


def new_keystore_password_is_valid(password: str):
    if len(password) < 6:
        return False

    return True


class CustomPrettyTable(PrettyTable):
    def get_string(self, **kwargs):
        if "Name" in self._align:
            self._align["Name"] = 'l'
        if "Comment" in self._align:
            self._align["Comment"] = 'l'
        if "Balance" in self._align:
            self._align["Balance"] = 'r'

        return super().get_string()


def md_table() -> CustomPrettyTable:
    table = CustomPrettyTable()
    table.set_style(MARKDOWN)
    return table


def form_wallets_table(wallets_info, verbose, wallets_verbose_info=None, total_required=False):
    # wallet list, whitelist list
    field_names = ['Name', 'Version', 'WC', 'Address', 'Comment']
    if verbose:
        field_names += ['State', 'Balance']

    table = md_table()
    table.field_names = field_names
    if verbose:
        total = 0
        for wallet, wallet_info in zip(wallets_info, wallets_verbose_info):
            total += wallet_info.balance
            table.add_row([wallet.name, wallet.version, wallet.workchain,
                           wallet.address_to_show, wallet.comment,
                           wallet_info.state, __format_float(wallet_info.balance)])
        if wallets_info and total_required:
            table.add_row(["Total", "", "", "", "", "", __format_float(total)])
    else:
        for wallet in wallets_info:
            table.add_row([wallet.name, wallet.version, wallet.workchain,
                           wallet.address_to_show, wallet.comment])

    return table


def form_whitelist_table(contacts, verbose, contact_infos=None):
    field_names = ["Name", "Address"]
    if verbose:
        field_names += ['State', 'Balance']

    table = md_table()
    table.field_names = field_names
    if verbose:
        for contact, contact_info in zip(contacts, contact_infos):
            table.add_row([contact.name, contact.address,
                           contact_info.state, __format_float(contact_info.balance)])

    else:
        for contact in contacts:
            table.add_row([contact.name, contact.address])

    return table


def __format_float(fl_number):
    if fl_number != 0:
        digits_after_comma = math.log10(fl_number)
        if digits_after_comma < -4:
            digits = math.ceil(abs(digits_after_comma))
            return f"{fl_number:.{digits}f}"

    return str(fl_number)
