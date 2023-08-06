from collections import OrderedDict

from ._base import BaseSet
from ._config import ConfigSet
from ._keystores import KeystoresSet
from ._whitelist import WhitelistSet


class EntrypointSet(BaseSet):
    def _handlers(self) -> OrderedDict:
        ord_dict = OrderedDict()
        ord_dict["Keystores"] = self._handle_keystores
        ord_dict["Whitelist"] = self._handle_whitelist
        ord_dict["Config"] = self._handle_config
        ord_dict["Exit"] = self._handle_exit
        return ord_dict

    def _handle_keystores(self):
        KeystoresSet(self.ctx).show()

    def _handle_whitelist(self):
        WhitelistSet(self.ctx).show()

    def _handle_config(self):
        ConfigSet(self.ctx).show()
