from tons.tonsdk.crypto import mnemonic_is_valid


def number_bigger_than_zero(answers, current):
    return float(current) >= 0


def valid_mnemonics(answers, current):
    return mnemonic_is_valid(current.split(" "))


def ignore_if_transfer_all(answers):
    return answers["transfer_all"]
