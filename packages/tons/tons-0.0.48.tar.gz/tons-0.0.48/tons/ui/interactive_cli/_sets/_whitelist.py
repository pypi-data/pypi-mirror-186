from collections import OrderedDict

import inquirer

from tons.tonclient.utils import Whitelist
from tons.tonsdk.utils import Address
from ._base import BaseSet
from .._modified_inquirer import ModifiedConfirm
from .._utils import echo_success
from ..._utils import SharedObject, md_table, form_whitelist_table


class WhitelistSet(BaseSet):
    def __init__(self, ctx: SharedObject) -> None:
        super().__init__(ctx)
        ctx.whitelist = Whitelist(
            ctx.config.tons.whitelist_path)

    def _handlers(self) -> OrderedDict:
        ord_dict = OrderedDict()
        ord_dict["List contacts"] = self._handle_list
        ord_dict["Add contact"] = self._handle_add
        ord_dict["Get contact"] = self._handle_get
        ord_dict["Edit contact"] = self._handle_edit
        ord_dict["Delete contact"] = self._handle_delete
        ord_dict["Back"] = self._handle_exit
        return ord_dict

    def _handle_list(self):
        questions = [
            ModifiedConfirm(
                "verbose", message='Show balances?', default=True),
        ]
        verbose = self._prompt(questions)["verbose"]

        with self._processing():
            contacts = self.ctx.whitelist.contacts
            contact_infos = None
            if verbose:
                contact_infos = self.ctx.ton_client.get_addresses_information(
                    [contact.address for contact in contacts])

            table = form_whitelist_table(contacts, verbose, contact_infos)

        echo_success(table, only_msg=True)

    def _handle_add(self):
        questions = [
            inquirer.Text(
                "name", message='Enter the name'),
            inquirer.Text(
                "address", message='Enter the address'),
        ]
        ans = self._prompt(questions)
        name = ans["name"]
        address = ans["address"]
        self.ctx.whitelist.add_contact(name, address, save=True)

        echo_success()

    def _handle_get(self):
        name = self.__select_contact_or_false('Contact to edit')
        if name == False:
            return

        contact = self.ctx.whitelist.get_contact(name, raise_none=True)

        addr = Address(contact.address)
        echo_success(
            f"Raw address: {addr.to_string(False, False, False)}", True)
        echo_success(
            f"Nonbounceable address: {addr.to_string(True, True, False)}", True)
        echo_success(
            f"Bounceable address: {addr.to_string(True, True, True)}", True)

    def _handle_edit(self):
        name = self.__select_contact_or_false('Contact to edit')
        if name == False:
            return

        new_name = self._select_whitelist_available_name(name)
        new_address = self._prompt([
            inquirer.Text(
                "address", message='Enter the address (enter to skip)'),
        ])["address"]

        self.ctx.whitelist.edit_contact(
            name, new_name, new_address, save=True)

        echo_success()

    def _handle_delete(self):
        name = self.__select_contact_or_false('Contact to edit')
        if name == False:
            return

        self.ctx.whitelist.delete_contact_by_name(name, save=True)

        echo_success()

    def __select_contact_or_false(self, message):
        if self.ctx.whitelist.contacts:
            questions = [
                inquirer.List(
                    "contact",
                    message=message,
                    choices=[
                        record.name for record in self.ctx.whitelist.contacts],
                    carousel=True
                )
            ]
            return self._prompt(questions)["contact"]

        echo_success("You do not have any contacts yet.")
        return False
