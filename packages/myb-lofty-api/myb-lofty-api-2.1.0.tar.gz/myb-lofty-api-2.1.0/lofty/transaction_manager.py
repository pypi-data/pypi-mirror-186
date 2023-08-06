from datetime import date, time, datetime, timezone
from typing import Optional

from lofty import LoftyAiApi, PaginationOptions
from lofty.pagination_options import PaginationSortOrder
from lofty.responses.transactions_by_user import Transaction


class TransactionManager:

    def __init__(self, client: LoftyAiApi, verbose: bool = False, prefetch: bool = False):
        """
        Be warn
        """
        if not client.is_authenticated:
            raise ValueError('The specified client has not been authenticated. Please login first.')

        self._client = client
        self._verbose = verbose
        self._transactions = self._get_all_transactions() if prefetch else None

    @staticmethod
    def date_to_unix_millis(d: date):
        return datetime.combine(d, time()).astimezone(timezone.utc).timestamp() * 1000

    def _get_all_transactions(
            self,
            start: Optional[date] = None,
            end: Optional[date] = None
    ) -> Optional[list[Transaction]]:
        all_transactions = []
        pagination_options = PaginationOptions(
            page_size=500,
            sort=PaginationSortOrder.Descending,
            start=None if start is None else TransactionManager.date_to_unix_millis(start),
            end=None if end is None else TransactionManager.date_to_unix_millis(end),
        )
        transactions_page = self._client.get_transactions(pagination_options)
        if transactions_page is None:
            return None

        all_transactions.extend(transactions_page.transactions)
        page_number = 1
        if self._verbose:
            print(f'Retrieved page {page_number} with {len(transactions_page.transactions)} transactions.')

        while transactions_page.meta.next is not None:
            pagination_options = PaginationOptions()
            pagination_options.next = transactions_page.meta.next
            pagination_options.sort = transactions_page.meta.sort
            pagination_options.page_size = transactions_page.meta.page_size
            transactions_page = self._client.get_transactions(pagination_options)
            all_transactions.extend(transactions_page.transactions)
            page_number += 1
            if self._verbose:
                print(f'Retrieved page {page_number} with {len(transactions_page.transactions)} transactions.')

        if self._verbose:
            print(f'Successfully retrieved {len(all_transactions)} total transactions.')

        return all_transactions

    def cache_transactions(self):
        """
        This method can be called to cache or recache transactions.
        The caching mechanism is intended to allow repeated use of the same set of transactions
        without having to refetch them all given there may be a lot of transactions.
        """
        self._transactions = self._get_all_transactions()

    def get_property_ids(self) -> set[str]:
        property_ids = set([txn.property_id for txn in self._transactions])
        return property_ids

    def get_rent_transactions(self) -> list[Transaction]:
        """
        Returns all rent transactions (received rent payments) ordered by date descending.
        """
        rent_transactions = [txn for txn in self._transactions if txn.is_rent]
        return rent_transactions

    def get_transactions_by_property(self) -> dict[str, Transaction]:
        return {txn.property_id: txn for txn in self._transactions}

    def get_transactions_by_date(self) -> dict[date, Transaction]:
        return {datetime.fromisoformat(txn.date).date(): txn for txn in self._transactions}

    def get_transactions_for_property(self, property_id: str) -> list[Transaction]:
        return [txn for txn in self._transactions if txn.property_id == property_id]
