import asyncio
from datetime import datetime
from typing import List

from tons.config import Config
from tons.tonsdk.boc import Cell
from tons.tonsdk.contract.wallet import SendModeEnum, WalletContract
from tons.tonsdk.provider.dapp import DAppClient, DAppWrongResult, BroadcastQuery
from tons.tonsdk.utils import to_nano, TonCurrencyEnum, from_nano, Address, b64str_to_bytes, \
    bytes_to_b64str
from ._queries import DAppQueries
from .._base import TonClient, AddressInfoResult, BroadcastResult, BroadcastStatusEnum
from ..._exceptions import TonDappError, TON_EXCEPTION_BY_CODE


class DAppTonClient(TonClient):
    RECORDS_LIMIT = 50

    def __init__(self, config: Config):
        self.config = config
        self.loop = asyncio.get_event_loop()
        self._provider: DAppClient = None

    @property
    def provider(self):
        if self._provider is None:
            self._provider = DAppClient(graphql_url=self.config.provider.dapp.graphql_url,
                                        broadcast_url=self.config.provider.dapp.broadcast_url,
                                        api_key=self.config.provider.dapp.api_key)

        return self._provider

    def get_address_information(self, address: str,
                                currency_to_show: TonCurrencyEnum = TonCurrencyEnum.ton):
        return self.get_addresses_information([address], currency_to_show)[0]

    def get_addresses_information(self, addresses: List[str],
                                  currency_to_show: TonCurrencyEnum = TonCurrencyEnum.ton):
        if not addresses:
            return []

        address_ids = [Address(addr).to_string(
            False, False, False) for addr in addresses]

        queries = [DAppQueries.accounts(address_ids[i:i + self.RECORDS_LIMIT])
                   for i in range(0, len(address_ids), self.RECORDS_LIMIT)]
        results = self._run(self.provider.query(
            queries), single_query=False)

        accounts = []
        for result in results:
            accounts += result['accounts']

        address_infos = [None] * len(address_ids)
        for account in accounts:
            idx = address_ids.index(account['id'])
            address_infos[idx] = self._parse_addr_info(account, currency_to_show)
        for i in range(len(address_infos)):
            if address_infos[i] is None:
                address_infos[i] = AddressInfoResult(
                    address=addresses[i], state="Uninit", balance=0)

        return address_infos

    def seqno(self, addr: str):
        if self.get_address_information(addr).seqno:
            return int(self.get_address_information(addr).seqno)

        return 0

    def deploy_wallet(self, wallet: WalletContract, wait_for_result=False):
        timeout = 30 if wait_for_result else 0
        query = wallet.create_init_external_message()
        base64_boc = bytes_to_b64str(query["message"].to_boc(False))
        result = self._run(self.provider.broadcast(
            [BroadcastQuery(boc=base64_boc, timeout=timeout)]))

        return self._parse_broadcast_result(result, wait_for_result)

    def transfer(self, from_wallet: WalletContract, to_addr: str,
                 amount: TonCurrencyEnum.ton, payload=None,
                 send_mode=SendModeEnum.ignore_errors | SendModeEnum.pay_gas_separately,
                 is_bounceable=True, wait_for_result=False, state_init=None):
        timeout = 30 if wait_for_result else 0
        seqno = self.seqno(from_wallet.address.to_string())
        query = from_wallet.create_transfer_message(
            to_addr=Address(to_addr).to_string(True, False, is_bounceable),
            amount=to_nano(amount, TonCurrencyEnum.ton),
            seqno=seqno,
            payload=payload,
            send_mode=send_mode,
            state_init=state_init,
        )
        msg_boc = query["message"].to_boc(False)
        base64_boc = bytes_to_b64str(msg_boc)
        result = self._run(self.provider.broadcast(
            [BroadcastQuery(boc=base64_boc, timeout=timeout)]))

        return self._parse_broadcast_result(result, wait_for_result)

    def send_boc(self, boc: bytes, wait_for_result: bool):
        timeout = 30 if wait_for_result else 0
        base64_boc = bytes_to_b64str(boc)
        result = self._run(self.provider.broadcast(
            [BroadcastQuery(boc=base64_boc, timeout=timeout)]))

        return self._parse_broadcast_result(result, wait_for_result)

    def _run(self, to_run, *, single_query=True):
        try:
            results = self.loop.run_until_complete(to_run)
        except DAppWrongResult as e:
            if len(e.errors) == 1 and e.errors[0].code in TON_EXCEPTION_BY_CODE:
                raise TON_EXCEPTION_BY_CODE[e.errors[0].code]

            raise TonDappError(str(e))

        except Exception as e:  # ClientConnectorError, ...?
            raise TonDappError(str(e))

        if single_query:
            return results[0]

        return results

    def _parse_addr_info(self, result: dict, currency_to_show: TonCurrencyEnum = TonCurrencyEnum.ton):
        return AddressInfoResult(
            address=result['address'],
            # contract_type='wallet v3r2',  # FIXME
            seqno=self._get_seqno(result),
            state=result['acc_type_name'],
            balance=self._get_balance(result, currency_to_show),
            last_activity=self._get_last_paid(result),
            code=result['code'],
            data=result['data'],
        )

    def _get_seqno(self, result):
        if result['acc_type_name'] in ["Active", "Frozen"]:
            # TODO: check contract type and version
            data_cell = Cell.one_from_boc(b64str_to_bytes(result["data"]))
            if len(data_cell.bits) > 32:
                seqno = 0
                for bit in data_cell.bits[:32]:
                    seqno = (seqno << 1) | bit
                return seqno

        return 0

    def _get_balance(self, result: dict, currency_to_show):
        if "balance" in result and result["balance"]:
            if int(result["balance"]) < 0:
                balance = 0
            else:
                balance = from_nano(int(result["balance"]), currency_to_show)
        else:
            balance = 0

        return float(balance)

    def _get_last_paid(self, result: dict):
        if "last_paid" in result and result["last_paid"]:
            return str(datetime.utcfromtimestamp(
                result['last_paid']).strftime('%Y-%m-%d %H:%M:%S'))

    def _parse_broadcast_result(self, result, waited) -> BroadcastResult:
        if "status" in result:
            if result["status"] == 1 and waited:
                status = BroadcastStatusEnum.commited
            else:
                status = BroadcastStatusEnum.broadcasted
        else:
            status = BroadcastStatusEnum.failed

        return BroadcastResult(waited=waited, status=status)
