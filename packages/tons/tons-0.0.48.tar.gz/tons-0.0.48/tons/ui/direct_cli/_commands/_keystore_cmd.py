import click

from tons import settings
from tons.tonclient.utils import KeyStoreAlreadyExistsError, KeyStoreInvalidPasswordError, \
    InvalidMnemonicsError
from ._base_cmd import cli
from .._utils import CustomClickException, with_keystores, with_keystore, click_echo_success
from ..._utils import new_keystore_password_is_valid, SharedObject


@cli.group()
def keystore():
    """
    Operate with keystores
    """


def __validate_password(ctx, param, value):
    if not new_keystore_password_is_valid(value):
        raise CustomClickException(
            'password need to be at least 6 characters long')
    return value


@keystore.command()
@with_keystores
@click.argument('name', required=True)
@click.password_option(default=settings.KEYSTORE_PASSWORD,
                       confirmation_prompt=False, prompt=False if settings.KEYSTORE_PASSWORD else True,
                       callback=__validate_password)
@click.pass_obj
def new(shared_object: SharedObject, name, password):
    """
    Create new .keystore file with a given name
    """
    try:
        shared_object.keystores.create_new_keystore(name, password, save=True)
    except KeyStoreAlreadyExistsError as e:
        raise CustomClickException(e)

    click_echo_success(
        f"keystore {name} has been created. To use it run 'tons config tons.keystore_name {name}'.")


@keystore.command()
@with_keystores
@click.pass_obj
def list(shared_object: SharedObject):
    """
    List all .keystore files in a current keystore workdir
    """
    for keystore in shared_object.keystores.keystore_paths.keys():
        click.echo(keystore)


@keystore.command()
@with_keystore(password_required=True)
@with_keystores
@click.argument('backup_file_path', required=True, type=click.Path(writable=True))
@click.option('--yes', '-y', 'is_sure', is_flag=True, help='Do not show the prompt')
@click.pass_obj
def backup(shared_object: SharedObject, backup_file_path: str, is_sure: bool):
    """
    Backup the keystore into a specified file
    """
    if not is_sure:
        click.confirm(
            f'Backup stores keys in UNENCRYPTED FORM. Are you sure want to export unencrypted keys to disk?',
            abort=True)
    try:
        shared_object.keystores.backup_keystore(
            shared_object.keystore, backup_file_path,
            shared_object.keystore_password)
    except (KeyStoreInvalidPasswordError, OSError) as e:
        raise CustomClickException(e)

    click_echo_success(
        f"backup {backup_file_path} has been created from the keystore {shared_object.config.tons.keystore_name}")


@keystore.command()
@with_keystores
@click.argument('name', required=True)
@click.argument('backup_file_path', required=True, type=click.Path(exists=True, readable=True))
@click.password_option(default=settings.KEYSTORE_PASSWORD,
                       confirmation_prompt=False, prompt=False if settings.KEYSTORE_PASSWORD else True,
                       callback=__validate_password)
@click.option('--from-ton-cli', 'from_ton_cli', is_flag=True, help='Restore from the ton-cli util')
@click.pass_obj
def restore(shared_object: SharedObject, name: str, backup_file_path: str, password: str,
            from_ton_cli: bool):
    """
    Restore the keystore from a specified file
    """
    try:
        if from_ton_cli:
            shared_object.keystores.restore_ton_cli_keystore(
                name, backup_file_path, password)
        else:
            shared_object.keystores.restore_tons_keystore(
                name, backup_file_path, password)
    except (InvalidMnemonicsError, KeyStoreAlreadyExistsError) as e:
        raise CustomClickException(e)

    click_echo_success(f"keystore {name} has been restored.")
