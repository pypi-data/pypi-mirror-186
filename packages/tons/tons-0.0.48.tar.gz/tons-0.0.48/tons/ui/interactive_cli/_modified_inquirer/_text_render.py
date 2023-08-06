from inquirer import errors, Text
from inquirer.render.console.base import BaseConsoleRender
from readchar import key


class ModifiedTextRender(BaseConsoleRender):
    title_inline = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current = self.question.default or ""
        self.cursor_offset = 0

    def get_current_value(self):
        current = self.current
        extra_len = len(self.question._message) + len("[?]  :")
        diff = (extra_len + len(self.current)) - self.terminal.width
        max_cursor_offset = self.terminal.width - extra_len
        if diff > 0:
            to_hide = diff
            cursor_offset_from_beginning = len(self.current) - self.cursor_offset
            if cursor_offset_from_beginning != 0:
                to_replace = min(diff, cursor_offset_from_beginning)
                current = current[to_replace:]
                to_hide -= to_replace

            if to_hide > 0:
                current = current[:-to_hide]
                diff -= to_hide

        if diff >= 0 and self.cursor_offset > max_cursor_offset:
            cursor_offset = max_cursor_offset
            # if self.cursor_offset == 0:
            #     cursor_offset = 0
            # else:
            #     cursor_offset = self.cursor_offset - diff if diff > 0 else self.cursor_offset
        else:
            cursor_offset = self.cursor_offset

        return current + (self.terminal.move_left * cursor_offset)
        # return self.current + (self.terminal.move_left * self.cursor_offset)

    def process_input(self, pressed):
        if pressed == key.CTRL_C:
            raise KeyboardInterrupt()

        if pressed in (key.CR, key.LF, key.ENTER):
            raise errors.EndOfInput(self.current)

        if pressed == key.BACKSPACE:
            if self.current and self.cursor_offset != len(self.current):
                if self.cursor_offset > 0:
                    n = -self.cursor_offset
                    self.current = self.current[: n - 1] + self.current[n:]
                else:
                    self.current = self.current[:-1]
        elif pressed == key.LEFT:
            if self.cursor_offset < len(self.current):
                self.cursor_offset += 1
        elif pressed == key.RIGHT:
            self.cursor_offset = max(self.cursor_offset - 1, 0)
        elif len(pressed) != 1:
            return
        else:
            if self.cursor_offset == 0:
                self.current += pressed
            else:
                n = -self.cursor_offset
                self.current = "".join((self.current[:n], pressed, self.current[n:]))


class TempTextRender(ModifiedTextRender):
    pass


class TempText(Text):
    kind = "temp_text"
