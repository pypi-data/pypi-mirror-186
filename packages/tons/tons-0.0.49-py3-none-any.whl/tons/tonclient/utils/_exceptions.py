class WhitelistContactAlreadyExistsError(Exception):
    pass


class WhitelistContactDoesNotExistError(Exception):
    pass


class KeyStoreAlreadyExistsError(Exception):
    pass


class KeyStoreDoesNotExistError(Exception):
    pass


class KeyStoreInvalidPasswordError(Exception):
    pass


class InvalidKeyStoreError(Exception):
    pass


class KeyStoreIsNotSpecifiedError(Exception):
    pass


class RecordAlreadyExistsError(Exception):
    pass


class RecordDoesNotExistError(Exception):
    pass


class InvalidMnemonicsError(Exception):
    pass
