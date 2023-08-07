import json

import requests

from tons import settings
from tons.version import __version__


def tons_is_outdated():
    from pkg_resources import parse_version

    parsed_version = parse_version(__version__)
    try:
        response = requests.get(settings.PYPI_PACKAGE_URL).text
        latest_version = json.loads(response)['info']['version']
    except Exception:  # FIXME
        return False

    parsed_latest = parse_version(latest_version)

    return parsed_latest > parsed_version
