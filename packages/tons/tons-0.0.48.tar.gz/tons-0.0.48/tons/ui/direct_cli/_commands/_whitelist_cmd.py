import click

from tons.tonclient import ton_exceptions_handler
from tons.tonclient.utils import WhitelistContactAlreadyExistsError, WhitelistContactDoesNotExistError
from tons.tonsdk.utils import InvalidAddressError, TonCurrencyEnum, Address
from ._base_cmd import cli
from .._utils import CustomClickException, with_whitelist, click_ton_exception_handler, click_echo_success
from ..._utils import md_table, SharedObject, form_whitelist_table


@cli.group()
def whitelist():
    """
    Operate with whitelist contacts
    """


@whitelist.command()
@with_whitelist
@click.argument('name', required=True)
@click.argument('address', required=True)
@click.pass_obj
def add(shared_object: SharedObject, name, address):
    """
    Add a contact to the whitelist
    """
    try:
        shared_object.whitelist.add_contact(name, address, save=True)
    except (
            PermissionError, FileNotFoundError, WhitelistContactAlreadyExistsError,
            InvalidAddressError) as e:
        raise CustomClickException(e)

    click_echo_success(f"contact {name} has been added to the whitelist.")


@whitelist.command()
@with_whitelist
@click.argument('name', required=True)
@click.pass_obj
def get(shared_object: SharedObject, name):
    """
    Get a contact address by its name
    """
    try:
        contact = shared_object.whitelist.get_contact(name, raise_none=True)
    except WhitelistContactDoesNotExistError as e:
        raise CustomClickException(e)

    addr = Address(contact.address)
    click.echo(f"Raw address: {addr.to_string(False, False, False)}")
    click.echo(f"Nonbounceable address: {addr.to_string(True, True, False)}")
    click.echo(f"Bounceable address: {addr.to_string(True, True, True)}")


@whitelist.command()
@with_whitelist
@click.argument('name', required=True, metavar="EXISTING_CONTACT_NAME")
@click.option('--name', '-n', 'new_name', help="Set a new name")
@click.option('--address', '-a', 'new_address', help="Set a new address")
@click.pass_obj
def edit(shared_object: SharedObject, name: str, new_name: str, new_address: str):
    """
    Edit contact in a whitelist
    """
    try:
        shared_object.whitelist.edit_contact(
            name, new_name, new_address, save=True)
    except (WhitelistContactDoesNotExistError, ValueError) as e:
        raise CustomClickException(e)

    click_echo_success(f"contact {name} has been edited.")


@whitelist.command()
@with_whitelist
@click.argument('name', required=True)
@click.pass_obj
def delete(shared_object: SharedObject, name: str):
    """
    Delete contact from a whitelist
    """
    try:
        shared_object.whitelist.delete_contact_by_name(name, save=True)
    except WhitelistContactDoesNotExistError as e:
        raise CustomClickException(e)

    click_echo_success(f"contact {name} has been deleted.")


@whitelist.command()
@ton_exceptions_handler(click_ton_exception_handler)
@with_whitelist
@click.option('--currency', '-c', default=TonCurrencyEnum.ton, show_default=True,
              type=click.Choice(TonCurrencyEnum))
@click.option('--verbose', '-v', 'verbose', is_flag=True, default=False,
              help="Extra information from TON")
@click.pass_obj
def list(shared_object: SharedObject, verbose: bool, currency: TonCurrencyEnum):
    """
    Print all contacts as a markdown table.
    You can output this command into .md file
    """
    contacts = shared_object.whitelist.contacts
    contact_infos = None
    if verbose:
        contact_infos = shared_object.ton_client.get_addresses_information(
            [contact.address for contact in contacts], currency)

    table = form_whitelist_table(contacts, verbose, contact_infos)

    click.echo(table)
