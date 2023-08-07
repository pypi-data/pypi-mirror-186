import os

import click

from tons.tonclient import ton_exceptions_handler
from tons.tonclient.utils import RecordAlreadyExistsError, RecordDoesNotExistError, \
    WhitelistContactDoesNotExistError, KeyStoreInvalidPasswordError, InvalidMnemonicsError
from tons.tonsdk.contract.wallet import SendModeEnum, WalletVersionEnum, Wallets
from tons.tonsdk.utils import TonCurrencyEnum, Address
from tons.tonsdk.utils._utils import default_subwallet_id
from tons.utils import storage
from ._base_cmd import cli
from .._utils import CustomClickException, with_whitelist, with_keystore, click_ton_exception_handler, \
    click_echo_success, y_n_to_bool
from ..._utils import md_table, SharedObject, form_wallets_table


def __parse_subwallet_id_after_workchain(ctx, param, value):
    version = ctx.params['version'] or ctx.obj.config.tons.default_wallet_version
    if version in WalletVersionEnum.with_subwallet_id():
        return default_subwallet_id(ctx.params['workchain']) if value is None else value

    return None


@cli.group()
def wallet():
    """
    Operate with wallets
    """


@wallet.command()
@with_keystore(password_required=False)
@with_whitelist
@click.argument('name', required=True)
@click.option('--version', '-v', type=click.Choice(WalletVersionEnum))
@click.option('--workchain', '-wc', default=0, show_default=True, type=int)
@click.option('--subwallet-id', '-id', type=int, callback=__parse_subwallet_id_after_workchain,
              help="Extra field for v3 and v4 versions. "
                   "Leave empty to use default 698983191 + workchain")
@click.option('--comment', help='Extra information about the wallet')
@click.option('--save-to-whitelist', 'contact_name', help='Contact name to save', metavar='NAME')
@click.pass_obj
def create(shared_object: SharedObject, name: str, version: str, workchain: int, subwallet_id: int,
           comment: str, contact_name: str):
    """
    Create wallet data and add it to the keystore
    """
    if contact_name:
        contact = shared_object.whitelist.get_contact(contact_name)
        if contact is not None:
            raise CustomClickException(
                f"Contact with the name '{contact_name}' already exists")

    if not version:
        version = WalletVersionEnum(
            shared_object.config.tons.default_wallet_version)

    try:
        mnemonics, pub_k, _priv_k, wallet = Wallets.create(version, workchain, subwallet_id)
        shared_object.keystore.add_record(name, wallet.address,
                                          pub_k.hex(), mnemonics, version,
                                          workchain, subwallet_id, comment, save=True)
    except RecordAlreadyExistsError as e:
        raise CustomClickException(e)

    if contact_name:
        shared_object.whitelist.add_contact(
            contact_name, wallet.address.to_string(True), save=True)

    click_echo_success(f"wallet {name} has been created.")


@wallet.command()
@with_keystore(password_required=False)
@with_whitelist
@click.argument('name', required=True)
@click.option('--name', '-n', 'new_name', help='New wallet name')
@click.option('--comment', '-c', 'new_comment', help='New extra information about the wallet')
@click.pass_obj
def edit(shared_object: SharedObject, name: str, new_name: str, new_comment: str):
    """
    Edit wallet data in a keystore
    """
    try:
        shared_object.keystore.edit_record(
            name, new_name, new_comment, save=True)
    except RecordDoesNotExistError as e:
        raise CustomClickException(e)

    click_echo_success(f"wallet {name} has been edited.")


@wallet.command()
@with_keystore(password_required=False)
@with_whitelist
@click.argument('name', required=True)
@click.option('--yes', '-y', 'is_sure', is_flag=True, help='Do not show the prompt')
@click.pass_obj
def delete(shared_object: SharedObject, name: str, is_sure: bool):
    """
    Delete wallet data from a keystore
    """
    if not is_sure:
        click.confirm(
            f'Are you sure you want to delete {name} wallet?', abort=True)

    try:
        shared_object.keystore.delete_record(name, save=True)
    except RecordDoesNotExistError as e:
        raise CustomClickException(e)

    click_echo_success(f"wallet {name} has been deleted.")


@wallet.command()
@with_keystore(password_required=False)
@with_whitelist
@click.argument('name', required=True)
@click.option('--verbose', '-v', is_flag=True, help='Load info about wallet from TON network')
@click.pass_obj
def get(shared_object: SharedObject, name: str, verbose: bool):
    """
    Get all wallet data from a keystore
    """
    try:
        wallet_record = shared_object.keystore.get_record_by_name(
            name, raise_none=True)
    except RecordDoesNotExistError as e:
        raise CustomClickException(e)

    addr = Address(wallet_record.address)
    if verbose:
        addr_info = shared_object.ton_client.get_address_information(
            wallet_record.address)

    click.echo(f"Raw address: {addr.to_string(False, False, False)}")
    click.echo(f"Nonbounceable address: {addr.to_string(True, True, False)}")
    click.echo(f"Bounceable address: {addr.to_string(True, True, True)}")
    click.echo(f"Version: {wallet_record.version}")
    click.echo(f"Workchain: {wallet_record.workchain}")
    click.echo(f"Subwallet id: {wallet_record.subwallet_id}")
    click.echo(f"Comment: {wallet_record.comment}")

    if verbose:
        click.echo("--- Verbose wallet information ---")
        for k, v in addr_info.dict().items():
            click.echo(str(k) + ': ' + str(v))


@wallet.command()
@ton_exceptions_handler(click_ton_exception_handler)
@with_keystore(password_required=False)
@click.option('--currency', '-c', default=TonCurrencyEnum.ton, show_default=True,
              type=click.Choice(TonCurrencyEnum))
@click.option('--verbose', '-v', 'verbose', is_flag=True, default=False,
              help="Extra information from TON")
@click.pass_obj
def list(shared_object: SharedObject, verbose: bool, currency: TonCurrencyEnum):
    """
    Print all wallets info as a markdown table. 
    You can output this command into .md file
    """
    wallets = shared_object.keystore.records
    wallet_infos = None
    if verbose:
        wallet_infos = shared_object.ton_client.get_addresses_information(
            [wallet.address for wallet in wallets], currency)

    table = form_wallets_table(wallets, verbose, wallet_infos, True)

    click.echo(table)


@wallet.command()
@with_keystore(password_required=False)
@with_whitelist
@click.argument('name', required=True)
@click.argument('version', type=click.Choice(WalletVersionEnum))
@click.argument('workchain', type=int)
@click.argument('mnemonics')
@click.option('--subwallet-id', '-id', type=int, callback=__parse_subwallet_id_after_workchain,
              help="Extra field for v3 and v4 versions. "
                   "Leave empty to use default 698983191 + workchain")
@click.option('--comment', help='Extra information about the wallet')
@click.option('--save-to-whitelist', 'contact_name', help='Contact name to save', metavar='NAME')
@click.pass_obj
def import_from_mnemonics(shared_object: SharedObject, name: str, version: WalletVersionEnum,
                          workchain: int, mnemonics: str, subwallet_id: int, comment: str,
                          contact_name: str):
    """
    Create wallet data from mnemonics and add it to the keystore
    """
    if contact_name:
        contact = shared_object.whitelist.get_contact(contact_name)
        if contact is not None:
            raise CustomClickException(
                f"Contact with the name '{contact_name}' already exists")

    mnemonics = mnemonics.split(" ")
    try:
        mnemonics, pub_k, _priv_k, wallet = Wallets.from_mnemonics(
            mnemonics, version, workchain, subwallet_id)
        shared_object.keystore.add_record(name, wallet.address,
                                          pub_k.hex(), mnemonics, version,
                                          workchain, subwallet_id, comment, save=True)
    except (RecordAlreadyExistsError, InvalidMnemonicsError) as e:
        raise CustomClickException(e)

    if contact_name:
        shared_object.whitelist.add_contact(
            contact_name, wallet.address.to_string(True), save=True)

    click_echo_success(f"wallet {name} has been imported.")


@wallet.command()
@with_keystore(password_required=True)
@click.argument('name', required=True)
@click.pass_obj
def reveal(shared_object: SharedObject, name: str):
    """
    Echo mnemonics of a wallet by its name
    """
    try:
        record = shared_object.keystore.get_record_by_name(
            name, raise_none=True)
        mnemonics = shared_object.keystore.get_secret(
            record, shared_object.keystore_password)
        click.echo(mnemonics)

    except (RecordDoesNotExistError, KeyStoreInvalidPasswordError) as e:
        raise CustomClickException(e)


@wallet.command()
@with_keystore(password_required=True)
@click.argument('name', required=True)
@click.argument('destination_dir', default=".", required=False, metavar='DESTINATION_DIR')
@click.pass_obj
def to_addr_pk(shared_object: SharedObject, name: str, destination_dir: str):
    """
    Export wallet to .pk and .addr file into a specified directory
    """
    try:
        record = shared_object.keystore.get_record_by_name(
            name, raise_none=True)
        mnemonics = shared_object.keystore.get_secret(
            record, shared_object.keystore_password).split(" ")
        addr, pk = Wallets.to_addr_pk(mnemonics, record.version,
                                      record.workchain, record.subwallet_id)

        addr_path = os.path.join(
            destination_dir, record.name + ".addr")
        pk_path = os.path.join(destination_dir, record.name + ".pk")
        storage.save_bytes(addr_path, addr)
        storage.save_bytes(pk_path, pk)

    except (RecordDoesNotExistError, KeyStoreInvalidPasswordError, OSError) as e:
        raise CustomClickException(e)


@wallet.command()
@ton_exceptions_handler(click_ton_exception_handler)
@with_whitelist
@with_keystore(password_required=True)
@click.argument('name', required=True)
@click.pass_obj
def init(shared_object: SharedObject, name: str):
    """
    Initialize address as a wallet
    """
    try:
        record = shared_object.keystore.get_record_by_name(
            name, raise_none=True)
        mnemonics = shared_object.keystore.get_secret(
            record, shared_object.keystore_password).split(" ")
    except (RecordDoesNotExistError, KeyStoreInvalidPasswordError) as e:
        raise CustomClickException(e)

    _mnemonics, _pub_k, _priv_k, wallet = Wallets.from_mnemonics(mnemonics, record.version,
                                                                 record.workchain, record.subwallet_id)

    result = shared_object.ton_client.deploy_wallet(wallet)

    click_echo_success(result)


@wallet.command()
@ton_exceptions_handler(click_ton_exception_handler)
@with_whitelist
@with_keystore(password_required=True)
@click.argument('from_wallet', required=True, metavar='WALLET_NAME')
@click.argument('to_contact', required=True, metavar='CONTACT_NAME')
@click.argument('amount', required=False, metavar='TON_COINS_NUM')
@click.option('--message', '-m', help='Attach message to the transfer')
@click.option('--wait', '-w', is_flag=True, help='Wait until transaction is committed', default=False)
@click.option('--bounceable', default="y", type=click.Choice(["y", "n"]),
              show_default=True, callback=y_n_to_bool,
              help="Bounce message back on errors. Should be 'n' to send money to an empty address")
@click.option('--pay-gas-separately', default="y", type=click.Choice(["y", "n"]),
              show_default=True, callback=y_n_to_bool)
@click.option('--ignore-errors', default="n", type=click.Choice(["y", "n"]), show_default=True,
              help='Bounce back if error occurs', callback=y_n_to_bool)
@click.option('--destroy-if-zero', default="n", type=click.Choice(["y", "n"]),
              show_default=True, callback=y_n_to_bool)
@click.option('--transfer-all', default="n", type=click.Choice(["y", "n"]),
              show_default=True, callback=y_n_to_bool)
@click.pass_obj
def transfer(shared_object: SharedObject, from_wallet, to_contact, amount, message, wait, bounceable,
             pay_gas_separately, ignore_errors, destroy_if_zero, transfer_all):
    """
    Transfer coins from your wallet to any address
    """
    if amount is None and not transfer_all:
        raise CustomClickException(
            "You must specify amount when you do not use --transfer-all flag.")

    try:
        record = shared_object.keystore.get_record_by_name(
            from_wallet, raise_none=True)
        mnemonics = shared_object.keystore.get_secret(
            record, shared_object.keystore_password).split(" ")
        contact = shared_object.whitelist.get_contact(
            to_contact, raise_none=True)
    except (
            WhitelistContactDoesNotExistError, RecordDoesNotExistError,
            KeyStoreInvalidPasswordError) as e:
        raise CustomClickException(e)

    send_mode = 0
    if ignore_errors:
        send_mode |= SendModeEnum.ignore_errors
    if pay_gas_separately:
        send_mode |= SendModeEnum.pay_gas_separately
    if destroy_if_zero:
        send_mode |= SendModeEnum.destroy_account_if_zero
    if transfer_all:
        send_mode |= SendModeEnum.carry_all_remaining_balance
        amount = 0

    _mnemonics, _pub_k, _priv_k, wallet = Wallets.from_mnemonics(mnemonics, record.version,
                                                                 record.workchain, record.subwallet_id)
    result = shared_object.ton_client.transfer(
        wallet, contact.address, amount, message, send_mode, bounceable, wait)

    click_echo_success(result)
