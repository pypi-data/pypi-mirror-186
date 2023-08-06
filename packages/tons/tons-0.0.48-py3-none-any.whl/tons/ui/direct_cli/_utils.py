import typing as t
from functools import wraps
from gettext import gettext as _
from json import JSONDecodeError

import click
from click import ClickException
from click._compat import get_text_stderr

from tons import settings
from tons.tonclient import TonError
from tons.tonclient.utils import Whitelist, KeyStores, \
    KeyStoreDoesNotExistError, InvalidKeyStoreError, KeyStoreIsNotSpecifiedError


class CustomClickException(ClickException):
    def show(self, file: t.Optional[t.IO] = None) -> None:
        if file is None:
            file = get_text_stderr()

        click.echo(_("{error}: {message}").format(
            error=click.style('Error', fg='red'),
            message=self.format_message()), file=file)


def click_echo_success(msg):
    click.echo("{success}: {message}".format(
        success=click.style('Success', fg='green'),
        message=msg
    ))


def with_whitelist(func):
    @click.pass_obj
    @wraps(func)
    def wrapper(shared_object, *args, **kwargs):
        try:
            shared_object.whitelist = Whitelist(
                shared_object.config.tons.whitelist_path)
        except JSONDecodeError:
            raise CustomClickException(
                f"Invalid json in the whitelist file: {shared_object.config.tons.whitelist_path}")

        return func(*args, **kwargs)

    return wrapper


def with_keystores(func):
    @click.pass_obj
    @wraps(func)
    def wrapper(shared_object, *args, **kwargs):
        shared_object.keystores = KeyStores(
            shared_object.config.tons.keystores_path)

        return func(*args, **kwargs)

    return wrapper


def with_keystore(password_required: bool):
    def without_password(func):
        @click.pass_obj
        @wraps(func)
        def without_password_wrapper(shared_object, *args, **kwargs):
            keystores = KeyStores(
                shared_object.config.tons.keystores_path)

            try:
                shared_object.keystore = keystores.get_keystore(
                    shared_object.config.tons.keystore_name, raise_none=True)
            except (KeyStoreDoesNotExistError, InvalidKeyStoreError, KeyStoreIsNotSpecifiedError) as e:
                raise CustomClickException(e)

            return func(*args, **kwargs)

        return without_password_wrapper

    def with_password(func):
        @click.pass_obj
        @click.password_option(default=settings.KEYSTORE_PASSWORD,
                               confirmation_prompt=False,
                               prompt=False if settings.KEYSTORE_PASSWORD else True)
        @wraps(func)
        def with_password_wrapper(shared_object, password, *args, **kwargs):
            keystores = KeyStores(
                shared_object.config.tons.keystores_path)

            try:
                shared_object.keystore = keystores.get_keystore(
                    shared_object.config.tons.keystore_name, raise_none=True)
                shared_object.keystore_password = password
            except (KeyStoreDoesNotExistError, InvalidKeyStoreError, KeyStoreIsNotSpecifiedError) as e:
                raise CustomClickException(e)

            return func(*args, **kwargs)

        return with_password_wrapper

    return with_password if password_required else without_password


def click_ton_exception_handler(exception: TonError):
    raise CustomClickException(exception)


class HiddenPassword(object):
    def __init__(self, password=''):
        self.password = password

    def __str__(self):
        return '*' * len(self.password)


def y_n_to_bool(ctx, param, value):
    return value == "y"
