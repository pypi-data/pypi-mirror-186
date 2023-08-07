import sys

from setuptools import setup


interactive_entrypoint = 'tons/ui/interactive_cli/__init__.py'

if "py2app" in sys.argv:
    extra_options = dict(
        name='tons-interactive',
        setup_requires=['py2app'],
        app=[interactive_entrypoint],
        options=dict(py2app=dict(argv_emulation=False, site_packages=True,
                                 plist={'CFBundleName': 'tons-interactive'})),
    )

elif "py2exe" in sys.argv:
    extra_options = dict(
        name='tons-interactive',
        setup_requires=['py2exe'],
        app=[interactive_entrypoint],
    )

elif "py2linux" in sys.argv:  # fixme
    extra_options = dict(
        scripts=[interactive_entrypoint],
    )
else:
    extra_options = {}

setup(
    **extra_options
)
