import contextlib
from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from typing import Optional

import inquirer
from halo import Halo

from .._exceptions import EscButtonPressed, InvalidUsageError
from .._modified_inquirer import ModifiedConsoleRender, ModifiedTheme, modified_prompt
from .._utils import echo_error
from ..._utils import SharedObject


class BaseSet(metaclass=ABCMeta):
    MENU_KEY = "menu_option"

    def __init__(self, ctx: SharedObject) -> None:
        self.ctx = ctx
        self._exit = False
        self._spinner = Halo(text='Processing', spinner='dots')

    def show(self):
        while not self._exit:
            items = [
                inquirer.List(self.MENU_KEY, message="Pick command",
                              choices=self._handlers().keys(), carousel=True),
            ]

            try:
                item = self._prompt(items)[self.MENU_KEY]
            except (EscButtonPressed, KeyboardInterrupt) as e:
                self._handle_exit()
                continue

            try:
                self._handlers()[item]()
            except (EscButtonPressed, KeyboardInterrupt) as e:
                pass
            except Exception as e:
                if self.ctx.debug_mode:
                    raise

                echo_error(e.__repr__())

    def _prompt(self, questions):
        return modified_prompt(questions, render=ModifiedConsoleRender(theme=ModifiedTheme()),
                               raise_keyboard_interrupt=True)

    @abstractmethod
    def _handlers(self) -> OrderedDict:
        raise NotImplementedError

    def _handle_exit(self):
        self._exit = True

    def _start_loading(self):
        self._spinner.start()

    def _stop_loading(self):
        self._spinner.stop()

    @contextlib.contextmanager
    def _processing(self):
        try:
            self._start_loading()
            yield
        finally:
            self._stop_loading()

    def _select_whitelist_available_name(self, old_name: str, new_name: str = "") -> Optional[str]:
        if not hasattr(self, 'ctx') or not hasattr(self.ctx, 'whitelist'):
            raise InvalidUsageError

        while True:
            new_contact_name = self._prompt([
                inquirer.Text(
                    "new_contact_name",
                    message=f'Enter the name (old: {old_name}, enter to skip)',
                    default=new_name),
            ])["new_contact_name"]
            if new_contact_name == old_name:
                return None
            elif self.ctx.whitelist.get_contact(new_contact_name) is not None:
                echo_error(f"Contact with the name {new_contact_name} already exists")
            else:
                return new_contact_name

    def _select_wallet_available_name(self, old_name: str, new_name: str = "") -> Optional[str]:
        if not hasattr(self, 'ctx') or not hasattr(self.ctx, 'keystore'):
            raise InvalidUsageError

        while True:
            new_wallet_name = self._prompt([
                inquirer.Text(
                    "new_wallet_name",
                    message=f'Enter the name (old: {old_name}, enter to skip)',
                    default=new_name),
            ])["new_wallet_name"]
            if new_wallet_name == old_name:
                return old_name
            elif self.ctx.keystore.get_record_by_name(new_wallet_name) is not None:
                echo_error(f"Wallet with the name {new_wallet_name} already exists")
            else:
                return new_wallet_name
