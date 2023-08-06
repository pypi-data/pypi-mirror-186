"""
https://ton-blockchain.github.io/docs/tvm.pdf
4.5.7. List of predefined exceptions
"""
import functools


class TonError(Exception):
    """
    Base class for ton exceptions.
    Subclasses should provide `.status_code` and `.default_detail` properties.
    """
    default_detail = 'TON error.'
    default_code = 500

    def __init__(self, detail=None, code=None):
        self.code = self.default_code if code is None else code
        self.detail = self.default_detail if detail is None else detail

        error_msg = "TON error."
        if self.code:
            error_msg += f" Code: {self.code}."
        if self.detail:
            error_msg += f" {self.detail}"
        self.error_msg = error_msg

    def __str__(self):
        return self.error_msg


class TonContractUninitializedError(TonError):
    default_detail = "Contract is not initialized."
    default_code = -13


class TonStackUnderflowError(TonError):
    default_detail = "Not enough arguments in the stack for a primitive."
    default_code = 2


class TonStackOverflowError(TonError):
    default_detail = "More values have been stored on a stack than allowed by this version of TVM."
    default_code = 3


class TonIntegerOverflowError(TonError):
    default_detail = "Integer does not fit into -(2^256) ≤ x < 2^256, or a division by zero has occurred."
    default_code = 4


class TonRangeCheckError(TonError):
    default_detail = "Integer out of expected range."
    default_code = 5


class TonInvalidOpcodeError(TonError):
    default_detail = "Instruction or its immediate arguments cannot be decoded."
    default_code = 6


class TonTypeCheckError(TonError):
    default_detail = "An argument to a primitive is of incorrect value type."
    default_code = 7


class TonCellOverflowError(TonError):
    default_detail = "Error in one of the serialization primitives."
    default_code = 8


class TonCellUnderflowError(TonError):
    default_detail = "Deserialization error."
    default_code = 9


class TonDictionaryError(TonError):
    default_detail = "Error while deserializing a dictionary object."
    default_code = 10


class TonUnknownError(TonError):
    default_detail = "Unknown error, may be thrown by user programs."
    default_code = 11


class TonFatalError(TonError):
    default_detail = "Thrown by TVM in situations deemed impossible."
    default_code = 12


class TonOutOfGasError(TonError):
    default_detail = "Thrown by TVM when the remaining gas (gr) becomes negative. This exception usually cannot be caught and leads to an immediate termination of TVM."
    default_code = 13


class TonNetworkError(TonError):
    default_detail = "Network problems. It may be caused by TON itself (e.g. testnet update). Make sure you have an internet connection and TON config is correct."
    default_code = 500


class TonTooManyQueriesError(TonError):
    default_detail = "Requests limit reached. Obtain key or increase limit " \
                     "via a telegram bot: @tontech_dapp_bot (or @tontech_dapp_testnet_bot for testnet)"
    default_code = 429


class TonUndocumentedError(TonError):
    default_detail = "Undocumented TON error. tons does not know what it is."
    default_code = None


class TonTimeoutError(TonError):
    default_detail = "TON request timeout error."
    default_code = None


class TonDappError(TonError):
    default_detail = "TON Dapp error."
    default_code = None


def ton_exceptions_handler(callback_by_exception):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except tuple(exc for exc in TON_EXCEPTION_BY_CODE.values()) as e:
                callback_by_exception(e)
            except (TonTimeoutError, TonUndocumentedError, TonDappError) as e:
                callback_by_exception(e)

        return wrapper

    return decorator


TON_EXCEPTION_BY_CODE = {
    -13: TonContractUninitializedError,
    2: TonStackUnderflowError,
    3: TonStackOverflowError,
    4: TonIntegerOverflowError,
    5: TonRangeCheckError,
    6: TonInvalidOpcodeError,
    7: TonTypeCheckError,
    8: TonCellOverflowError,
    9: TonCellUnderflowError,
    10: TonDictionaryError,
    11: TonUnknownError,
    12: TonFatalError,
    13: TonOutOfGasError,
    429: TonTooManyQueriesError,
    # TODO: 500 looks like "cannot apply external message to current state : Failed to unpack account state"
    500: TonNetworkError,
}

PROVIDER_EXCEPTION_BY_CODE = {
    429: TonTooManyQueriesError,
}
