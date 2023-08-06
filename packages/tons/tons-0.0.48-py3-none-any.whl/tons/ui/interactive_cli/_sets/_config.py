from collections import OrderedDict

import inquirer

from tons import settings
from tons.config import TonNetworkEnum, set_network, update_config_field
from ._base import BaseSet
from .._utils import echo_success
from ..._utils import SharedObject, get_ton_client


class ConfigSet(BaseSet):
    def __init__(self, ctx: SharedObject) -> None:
        super().__init__(ctx)
        self.config_path = settings.CURRENT_CONFIG_PATH

    def _handlers(self) -> OrderedDict:
        ord_dict = OrderedDict()
        ord_dict["API key"] = self._handle_api_key
        ord_dict["Network"] = self._handle_network
        ord_dict["Current setup"] = self._handle_current_setup
        ord_dict["Back"] = self._handle_exit
        return ord_dict

    def _handle_api_key(self):
        questions = [
            inquirer.Text(
                "api_key", message='API key to access dapp',
                default=self.ctx.config.provider.dapp.api_key),
        ]
        api_key = self._prompt(questions)["api_key"]
        update_config_field(self.config_path, "provider.dapp.api_key", api_key)
        self.ctx.config.provider.dapp.api_key = api_key
        self.ctx.ton_client = get_ton_client(self.ctx.config)

    def _handle_network(self):
        questions = [
            inquirer.List(
                "network", message='TON network to use', choices=[e.value for e in TonNetworkEnum],
                carousel=True, default=self.ctx.config.provider.dapp.network),
        ]
        network = TonNetworkEnum(self._prompt(questions)["network"])
        set_network(self.ctx.config, self.config_path, network)
        self.ctx.config.provider.dapp.network = network
        self.ctx.ton_client = get_ton_client(self.ctx.config)

    def _handle_current_setup(self):
        for key, val in self.ctx.config.key_value():
            echo_success(f"{key}={val}", True)
