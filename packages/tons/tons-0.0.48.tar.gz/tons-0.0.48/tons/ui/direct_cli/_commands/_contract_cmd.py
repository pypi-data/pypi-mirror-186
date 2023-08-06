import click

from tons.tonclient import ton_exceptions_handler
from tons.tonclient.utils import RecordDoesNotExistError, WhitelistContactDoesNotExistError
from ._base_cmd import cli
from .._utils import CustomClickException, with_whitelist, with_keystore, click_ton_exception_handler
from ..._utils import SharedObject


@cli.group()
@with_whitelist
@with_keystore(password_required=False)
@click.option('--address', '-a', help='Show info by an address')
@click.option('--wallet', '-w', help='Show info by a wallet name')
@click.option('--contact', '-c', help='Show info by a whitelist contact name')
@click.pass_obj
def contract(shared_object: SharedObject, address: str, wallet: str, contact: str):
    """
    Operate with contracts
    """
    if not any([address, wallet, contact]):
        raise click.MissingParameter(
            param=click.Option(['--address', '--wallet', '--contact']))

    if address:
        shared_object.addr = address
    elif wallet:
        try:
            wallet_obj = shared_object.keystore.get_record_by_name(
                wallet, raise_none=True)
        except RecordDoesNotExistError as e:
            raise CustomClickException(e)

        shared_object.addr = wallet_obj.address
    else:
        try:
            contact_obj = shared_object.whitelist.get_contact(
                contact, raise_none=True)
        except WhitelistContactDoesNotExistError as e:
            raise CustomClickException(e)

        shared_object.addr = contact_obj.address


@contract.command()
@ton_exceptions_handler(click_ton_exception_handler)
@click.pass_obj
def info(shared_object: SharedObject):
    """
    Show TON blockchain information
    """
    addr_info = shared_object.ton_client.get_address_information(
        shared_object.addr)
    for k, v in addr_info.dict().items():
        click.echo(str(k) + ': ' + str(v))


@contract.command()
@ton_exceptions_handler(click_ton_exception_handler)
@click.pass_obj
def balance(shared_object: SharedObject):
    """
    Show the balance of a contract
    """
    addr_info = shared_object.ton_client.get_address_information(
        shared_object.addr)
    click.echo(addr_info.balance)


@contract.command()
@ton_exceptions_handler(click_ton_exception_handler)
@click.pass_obj
def seqno(shared_object: SharedObject):
    """
    Show seqno
    """
    seqno = shared_object.ton_client.seqno(shared_object.addr)
    click.echo(seqno)
