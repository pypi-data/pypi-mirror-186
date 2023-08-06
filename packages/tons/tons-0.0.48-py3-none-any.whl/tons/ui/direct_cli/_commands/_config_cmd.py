import click
from pydantic import ValidationError

from tons import settings
from tons.config import update_config_field, unset_config_field, get_config, get_configs_with_origins, \
    Config, ConfigLocation, TonNetworkEnum, set_network
from tons.utils.exceptions import StorageError
from ._base_cmd import cli
from .._utils import CustomClickException
from ..._utils import SharedObject


def __list_configs(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    configs, origins = get_configs_with_origins(ctx.obj.specific_config_path)
    if configs:
        for config, origin in zip(configs, origins):
            for key, val in config.key_value(exclude_unset=True):
                click.echo(f"{origin}  {key}={val}")

    else:
        click.echo("No configs found.")

    ctx.exit()


def __current_setup(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    for key, val in ctx.obj.config.key_value():
        click.echo(f"{key}={val}")

    ctx.exit()


@cli.command()
@click.option('--list', is_flag=True, callback=__list_configs,
              expose_value=False, is_eager=True, help='Show configs values')
@click.option('--current-setup', is_flag=True, callback=__current_setup,
              expose_value=False, is_eager=True, help='Show current configuration')
@click.option('--global', '-g', 'config_location', flag_value=ConfigLocation.global_location.value,
              help='Work with a global config')
@click.option('--local', '-l', 'config_location', default=True,
              flag_value=ConfigLocation.local_location.value,
              help='Work with the config in the current workdir. [default]')
@click.option('--file', '-f', 'config_location', help='Specific config path', metavar='PATH')
@click.option('--network', help='Setup providers to a provided network',
              type=click.Choice(TonNetworkEnum))
@click.option('--unset', is_flag=True, default=False, help='Removes [NAME] from config')
@click.argument('name', required=False)
@click.argument('value', required=False)
@click.pass_obj
def config(shared_object: SharedObject, config_location: str, network: TonNetworkEnum, unset: bool,
           name: str, value: str):
    """
    Control config parameters (check README.md for all fields info)
    """
    if config_location is None:
        config_location = settings.CURRENT_CONFIG_PATH

    if network:
        set_network(shared_object.config, config_location, network)
        return
    elif name is None:
        raise click.MissingParameter(name)

    if not unset and not value:
        __show_value(shared_object.config, config_location, name)

    else:
        if unset:
            unset_config_field(config_location, name)
        else:
            try:
                update_config_field(config_location, name, value)
            except StorageError as e:
                raise CustomClickException(e)
            except ValidationError as e:
                msg = f"'{e.errors()[0]['loc'][0]}' {e.errors()[0]['msg']} "
                raise CustomClickException(msg)
            except ValueError as e:
                raise CustomClickException(
                    "Incorrect field name. Choices are: {}".format(", ".join(Config.field_names())))


def __show_value(config: Config, config_location: str, name: str):
    try:
        config_to_show = get_config(
            config_location) if config_location else config
    except StorageError as e:
        raise CustomClickException(e)

    if config_to_show:
        field_val = config_to_show.get_nondefault_value(name)
        if field_val:
            click.echo(field_val)


