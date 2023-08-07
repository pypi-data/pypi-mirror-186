import os
import sys
from json import JSONDecodeError

from pydantic import ValidationError

from tons.config import ConfigNotFoundError
from tons.ui._utils import init_shared_object, setup_app
from tons.ui.interactive_cli._exceptions import EscButtonPressed
from tons.ui.interactive_cli._sets import EntrypointSet
from tons.ui.interactive_cli._utils import echo_error


def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        context = init_shared_object()
        setup_app(context.config)

    except (FileNotFoundError, JSONDecodeError, ConfigNotFoundError, ValidationError) as e:
        echo_error(e)
        return

    if len(sys.argv) == 2 and sys.argv[1] == "--debug":
        context.debug_mode = True

    try:
        EntrypointSet(context).show()
    except (EscButtonPressed, KeyboardInterrupt):
        pass


if __name__ == '__main__':
    main()
