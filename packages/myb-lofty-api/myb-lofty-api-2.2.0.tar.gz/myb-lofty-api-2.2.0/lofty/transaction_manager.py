from datetime import date, time, datetime, timezone, timedelta
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

    def get_rent_transactions(self, num_days=None) -> list[Transaction]:
        """
        Returns all rent transactions (received rent payments) ordered by date descending when num_days is not specified.
        To limit the number of days back of transactions, specify a number of days to use.
        Note that num_days of 1 means that only today's transactions will be returned.
        """
        rent_transactions = [txn for txn in self._transactions if txn.is_rent]
        if num_days:
            now_date = datetime.utcnow().date()
            exclusive_end_date = now_date - timedelta(days=num_days)
            rent_transactions = [txn for txn in rent_transactions if
                                 datetime.fromisoformat(txn.date).date() > exclusive_end_date]

        return rent_transactions

    def get_properties_not_paying_rent_currently(self) -> set[str]:
        """
        Analyzes the past three days and make sure no payments were made for both days
        This also covers the case where rent for the day hasn't happened yet - we'll check two days in that case.
        """
        rent_transactions = self.get_rent_transactions(num_days=3)
        transaction_totals_by_property: dict[str, int] = {}
        for transaction in rent_transactions:
            transaction_totals_by_property.setdefault(transaction.property_id, 0)
            transaction_totals_by_property[transaction.property_id] += transaction.amount

        return set(
            [property_id for property_id, rent_total in transaction_totals_by_property.items() if rent_total == 0]
        )

    def get_transactions_by_property(self) -> dict[str, Transaction]:
        return {txn.property_id: txn for txn in self._transactions}

    def get_transactions_by_date(self) -> dict[date, Transaction]:
        return {datetime.fromisoformat(txn.date).date(): txn for txn in self._transactions}

    def get_transactions_for_property(self, property_id: str) -> list[Transaction]:
        return [txn for txn in self._transactions if txn.property_id == property_id]
