from typing import Optional
from decimal import Decimal


class Summaries:
    def __init__(self, summaries_data: dict):
        self.rent_pending: int = summaries_data.get('rentPending')
        self.data_type: str = summaries_data.get('dataType')
        self.property_id: str = summaries_data.get('propertyId')
        cost_per_token: float = summaries_data.get('costPerToken')
        self.cost_per_token: Optional[Decimal] = Decimal(str(cost_per_token)) if cost_per_token is not None else None
        self.pending_tokens: int = summaries_data.get('pendingTokens')
        self.total_spent: int = summaries_data.get('totalSpent')
        self.latest_dividends_date: str = summaries_data.get('latestDividendsDate')
        self.rent_spent: int = summaries_data.get('rentSpent')
        self.current_tokens: int = summaries_data.get('currentTokens')
        self.user_sub: str = summaries_data.get('userSub')
        current_value: float = summaries_data.get('currentValue')
        self.current_value: Optional[Decimal] = Decimal(str(current_value)) if current_value is not None else None
        self.balance: int = summaries_data.get('balance')
        self.latest_pending_dividends_date: str = summaries_data.get('latestPendingDividendsDate')
        self.updated_at: int = summaries_data.get('updatedAt')
        self.user_id: str = summaries_data.get('userId')
        self.sk: str = summaries_data.get('SK')
        self.pk: str = summaries_data.get('PK')
        self.dividends: int = summaries_data.get('dividends')


class Totals:
    def __init__(self, totals_data: dict):
        self.data_type: str = totals_data.get('dataType')
        self.total_rent: int = totals_data.get('totalRent')
        self.total_available_rent: int = totals_data.get('totalAvailableRent')
        self.total_properties: int = totals_data.get('totalProperties')
        self.snapshot_processed: int = totals_data.get('snapshotProcessed')
        self.snapshot_status: str = totals_data.get('snapshotStatus')
        self.user_sub: str = totals_data.get('userSub')
        self.rent_status: str = totals_data.get('rentStatus')
        total_available_value: float = totals_data.get('totalAvailableValue')
        self.total_available_value: Optional[Decimal] = Decimal(str(total_available_value)) if total_available_value is not None else None
        self.updated_at: int = totals_data.get('updatedAt')
        self.user_id: str = totals_data.get('userId')
        self.sk: str = totals_data.get('SK')
        self.total_withheld_amount: int = totals_data.get('totalWithheldAmount')
        self.pk: str = totals_data.get('PK')
        self.rent_processed: str = totals_data.get('rentProcessed')


class TransactionSummary:
    def __init__(self, transaction_summary_data: dict):
        self.summaries: list[Summaries] = [Summaries(item) for item in transaction_summary_data.get('summaries')]


