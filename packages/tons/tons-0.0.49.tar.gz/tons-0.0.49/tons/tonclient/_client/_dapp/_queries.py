from typing import List

from gql import gql
from graphql import DocumentNode


class DAppQueries:
    @classmethod
    def accounts(cls, account_ids: List[str], ) -> DocumentNode:
        return gql(
            """
        query {
            accounts(
                filter: {
                    id: {
                        in: [%s]
                    }
                }
            ) {
                id
                address
                acc_type_name
                state_hash
    			last_paid
    			balance
                last_trans_lt
    			code
                data
            }
        }
        """ % ", ".join([f"\"{acc_id}\"" for acc_id in account_ids]))
