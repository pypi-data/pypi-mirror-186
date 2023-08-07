from collections import OrderedDict

import inquirer

from tons.tonclient.utils import KeyStores
from ._base import BaseSet
from ._keystore import KeystoreSet
from .._utils import echo_success, echo_error
from ..._utils import SharedObject, new_keystore_password_is_valid


class KeystoresSet(BaseSet):
    def __init__(self, ctx: SharedObject) -> None:
        super().__init__(ctx)
        self.ctx.keystores = KeyStores(
            self.ctx.config.tons.keystores_path)

    def _handlers(self) -> OrderedDict:
        ord_dict = OrderedDict()
        ord_dict["Open keystore"] = self._handle_open_keystore
        ord_dict["Create keystore"] = self._handle_create_keystore
        ord_dict["Restore keystore"] = self._handle_restore_keystore
        ord_dict["Back"] = self._handle_exit
        return ord_dict

    def _handle_open_keystore(self):
        if self.ctx.keystores.keystore_paths:
            keystore_name = self._prompt([
                inquirer.List("keystore_name", message="Choose keystore to use",
                              choices=self.ctx.keystores.keystore_paths, carousel=True),
            ])["keystore_name"]
            KeystoreSet(self.ctx, keystore_name).show()
        else:
            echo_success("You do not have any keystores yet.")

    def _handle_create_keystore(self):
        questions = [
            inquirer.Text(
                "name", message='Enter the name'),
            inquirer.Password(
                "password1", message='Enter the password (at least 6 symbols)'),
            inquirer.Password(
                "password2", message='Re-enter the password'),
        ]
        ans = self._prompt(questions)
        name = ans["name"]
        pass1 = ans["password1"]
        pass2 = ans["password2"]

        if self.__validate_passwords(pass1, pass2):
            self.ctx.keystores.create_new_keystore(name, pass1, save=True)
            echo_success()

    def _handle_restore_keystore(self):
        questions = [
            inquirer.List("restore_from", message='Restore from',
                          choices=["tons backup", "ton-cli backup"]),
            inquirer.Text(
                "backup_file_path", message='Enter the path to backup file'),
            inquirer.Text(
                "name", message="Enter new name"),
            inquirer.Password(
                "password1", message='Enter the password (at least 6 symbols)'),
            inquirer.Password(
                "password2", message='Re-enter the password'),
        ]
        ans = self._prompt(questions)
        name = ans["name"]
        restore_from = ans["restore_from"]
        backup_file_path = ans["backup_file_path"]
        pass1 = ans["password1"]
        pass2 = ans["password2"]

        if self.__validate_passwords(pass1, pass2):
            if restore_from == "ton-cli backup":
                self.ctx.keystores.restore_ton_cli_keystore(
                    name, backup_file_path, pass1)
            else:
                self.ctx.keystores.restore_tons_keystore(
                    name, backup_file_path, pass1)
            echo_success()

    def __validate_passwords(self, pass1, pass2):
        if pass1 != pass2:
            echo_error("Passwords do not match.")
            return False

        if not new_keystore_password_is_valid(pass1):
            echo_error("Password must be at least 6 symbols long.")
            return False

        return True
