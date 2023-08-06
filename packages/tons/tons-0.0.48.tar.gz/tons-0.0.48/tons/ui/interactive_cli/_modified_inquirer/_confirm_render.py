from inquirer import errors, Confirm
from inquirer.render.console import Confirm as ConfirmRender
from readchar import key


class ModifiedConfirmRender(ConfirmRender):
    def process_input(self, pressed):
        if pressed == key.CTRL_C:
            raise KeyboardInterrupt()

        if pressed.lower() == key.ENTER:
            raise errors.EndOfInput(self.question.default)

        if pressed in "yY":
            print(pressed, end='')
            raise errors.EndOfInput(True)
        if pressed in "nN":
            print(pressed, end='')
            raise errors.EndOfInput(False)


class ModifiedConfirm(Confirm):
    kind = "modified_confirm"
