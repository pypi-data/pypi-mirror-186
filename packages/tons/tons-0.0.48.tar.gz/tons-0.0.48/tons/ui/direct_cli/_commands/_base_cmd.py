from json import JSONDecodeError

import click
from pydantic.error_wrappers import ValidationError

from tons import settings
from tons.config import Config, ConfigNotFoundError, TonsConfig, ProviderConfig
from tons.utils import storage
from tons.version import __version__
from .._utils import CustomClickException
from ..._utils import init_shared_object, setup_app


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(__version__)
@click.option("-c", "--config", 'specific_config_path', metavar='', help="Use specific config.yaml file")
@click.pass_context
def cli(ctx, specific_config_path: str):
    try:
        ctx.obj = init_shared_object(specific_config_path)

        if ctx.invoked_subcommand not in ["config", "init"]:
            setup_app(ctx.obj.config)

    except (FileNotFoundError, JSONDecodeError, ConfigNotFoundError, ValidationError) as e:
        raise CustomClickException(e)


@cli.command()
def init():
    """
    Initialize .tons workdir in a current directory
    """
    tons = TonsConfig(workdir=settings.DEFAULT_LOCAL_WORKDIR)
    provider = ProviderConfig()
    config = Config(tons=tons, provider=provider)
    setup_app(config)
    storage.save_yaml(settings.INIT_LOCAL_CONFIG_PATH, config.dict())
