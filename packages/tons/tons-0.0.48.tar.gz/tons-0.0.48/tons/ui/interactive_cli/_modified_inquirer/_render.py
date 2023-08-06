from inquirer import events, errors
from inquirer.render.console import ConsoleRender
from inquirer.render.console import List

from ._confirm_render import ModifiedConfirmRender
from ._text_render import ModifiedTextRender, TempTextRender
from .._exceptions import EscButtonPressed

ESC_BUTTONS = {"\x1b", "\x1b\x1b"}


class ModifiedConsoleRender(ConsoleRender):
    def render(self, question, question_idx, questions_num, answers=None):
        question.answers = answers or {}

        if question.ignore:
            return question.default

        clazz = self.render_factory(question.kind)
        render = clazz(question, terminal=self.terminal,
                       theme=self._theme, show_default=question.show_default)

        self.clear_eos()

        is_success = True

        try:
            ans = self._event_loop(render)
            return ans

        except EscButtonPressed:
            raise

        except Exception:
            is_success = False

        finally:
            # if question is a list and it's the last one then we should delete +1
            # if question is a list and it's not the last one then we should NOT delete +1
            if type(render) in [List, TempTextRender]:
                if type(render) is List:
                    self._position = len(list(render.get_options()))
                    if question_idx == questions_num - 1:
                        self._position += 1
                elif type(render) is TempTextRender:
                    self._position += 1

                self._relocate()
                self.clear_eos()
                self._print_header(render, self._get_msg_mark(is_success))
            else:
                print("")

    def _print_header(self, render, specific_msg_mark=None):
        base = render.get_header()

        header = base[: self.width - 9] + \
                 "..." if len(base) > self.width - 6 else base
        default_value = " ({color}{default}{normal})".format(
            default=render.question.default, color=self._theme.Question.default_color,
            normal=self.terminal.normal
        )
        show_default = render.question.default and render.show_default
        header += default_value if show_default else ""

        msg_mark = "?" if specific_msg_mark is None else specific_msg_mark
        msg_template = (
                "{t.move_up}{t.clear_eol}{tq.brackets_color}[" "{tq.mark_color}" +
                msg_mark + "{tq.brackets_color}]{t.normal} {msg}"
        )

        # ensure any user input with { or } will not cause a formatting error
        escaped_current_value = str(render.get_current_value()).replace(
            "{", "{{").replace("}", "}}")
        self.print_str(
            f"\n{msg_template}: {escaped_current_value}",
            msg=header,
            lf=not render.title_inline,
            tq=self._theme.Question,
        )

    def _process_input(self, render):
        try:
            ev = self._event_gen.next()
            if isinstance(ev, events.KeyPressed):
                if ev.value in ESC_BUTTONS:
                    raise EscButtonPressed()

                render.process_input(ev.value)
        except errors.ValidationError as e:
            self._previous_error = e.value
        except errors.EndOfInput as e:
            try:
                render.question.validate(e.selection)
                raise
            except errors.ValidationError as e:
                self._previous_error = render.handle_validation_error(e)

    def _get_msg_mark(self, is_success):
        return "✓" if is_success else "✕"

    def render_factory(self, question_type):
        if question_type == "text":
            return ModifiedTextRender
        if question_type == 'temp_text':
            return TempTextRender
        if question_type == 'modified_confirm':
            return ModifiedConfirmRender

        return super().render_factory(question_type)
