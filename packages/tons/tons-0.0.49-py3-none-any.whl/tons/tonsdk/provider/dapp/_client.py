from typing import Any, List

import aiohttp
from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from gql.transport.exceptions import TransportQueryError
from graphql import DocumentNode
from pydantic import BaseModel


class ErrorMsg(BaseModel):
    message: str
    code: int


class DAppWrongResult(Exception):
    def __init__(self, errors):
        self.errors = errors

    def __str__(self):
        return ". ".join([f"{error.message}, Code: {error.code}" for
                          error in self.errors])


class BroadcastQuery(BaseModel):
    boc: str
    timeout: int


class DAppClient:
    def __init__(self, graphql_url: str, broadcast_url: str, api_key: str):
        self.api_key = api_key
        self.broadcast_url = broadcast_url
        self.transport = AIOHTTPTransport(
            url=graphql_url, headers=self.__headers(is_json=False))

    async def query(self, queries: List[DocumentNode], ignore_errors=False) -> List[Any]:
        results = []

        async with Client(
                transport=self.transport,
                fetch_schema_from_transport=False,
        ) as session:
            for query in queries:
                try:
                    result = await session.execute(query)
                    results.append(result)
                except TransportQueryError as e:
                    self.__handle_errors(e.errors, ignore_errors)

        return results

    async def broadcast(self, queries: List[BroadcastQuery], timeout=31, ignore_errors=False) -> List[
        Any]:
        results = []
        timeout = aiohttp.ClientTimeout(total=timeout)

        async with aiohttp.ClientSession(timeout=timeout) as session:
            for query in queries:
                try:
                    async with session.post(self.broadcast_url, json=query.dict(),
                                            headers=self.__headers(is_json=True)) as resp:
                        results.append(await self.__parse_broadcast_response(resp, ignore_errors))
                except TransportQueryError as e:
                    self.__handle_errors(e.errors, ignore_errors)

        return results

    def __headers(self, is_json):
        headers = {}

        if is_json:
            headers = {
                'Content-Type': 'application/json',
            }

        if self.api_key:
            headers['API-KEY'] = self.api_key

        return headers

    async def __parse_broadcast_response(self, resp, ignore_errors):
        try:
            resp = await resp.json()
        except Exception:  # TODO: catch correct exceptions
            self.__handle_errors({"message": resp.reason, "code": resp.status}, ignore_errors)
            return None

        if "errors" in resp and resp['errors']:
            if len(resp['errors']) == 1 and 'message' in resp['errors'][0] \
                    and resp['errors'][0]['message'] == 'timeout':
                # transaction may have been sent and may be commited later
                resp['data']['status'] = 0
                return resp['data']

            else:
                return self.__handle_errors(resp['errors'], ignore_errors)

        return resp['data']

    def __handle_errors(self, errors, raise_errors):
        if not raise_errors:
            errors = [ErrorMsg.parse_obj(error)
                      for error in errors]
            raise DAppWrongResult(errors)

        return
