from decimal import Decimal
from typing import Optional


class Prices:
    def __init__(self, prices_data: dict):
        self.purchase_price: int = prices_data.get('purchasePrice')
        self.tokens: int = prices_data.get('tokens')
        self.total_tokens: int = prices_data.get('totalTokens')


class Dates:
    def __init__(self, dates_data: dict):
        self.date: str = dates_data.get('date')
        self.quantity: int = dates_data.get('quantity')


class WalletStatus:
    def __init__(self, wallet_status_data: dict):
        self.opted_in_wallet: str = wallet_status_data.get('optedInWallet')
        self.received: int = wallet_status_data.get('received')
        self.returned: int = wallet_status_data.get('returned')


class PropertyStatus:
    def __init__(self, property_status_data: dict):
        self.received: int = property_status_data.get('received')
        self.returned: int = property_status_data.get('returned')
        self.wallet_status: list[WalletStatus] = [WalletStatus(item) for item in
                                                  property_status_data.get('walletStatus')]


class Property:
    def __init__(self, property_data: dict):
        self.tokens_purchased: int = property_data.get('tokensPurchased')
        self.current_tokens: int = property_data.get('currentTokens')
        self.pending_tokens: int = property_data.get('pendingTokens')
        self.transferred_tokens: int = property_data.get('transferredTokens')
        self.received_tokens: int = property_data.get('receivedTokens')
        self.current_value: int = property_data.get('currentValue')
        self.total_spent: int = property_data.get('totalSpent')
        self.cost_basis: int = property_data.get('costBasis')
        self.entry_basis: int = property_data.get('entryBasis')
        self.start_price: int = property_data.get('startPrice')
        self.current_price: int = property_data.get('currentPrice')
        self.prices: list[Prices] = [Prices(item) for item in property_data.get('prices')]
        self.dates: list[Dates] = [Dates(item) for item in property_data.get('dates')]
        self.property_id: str = property_data.get('propertyId')
        self.rent_balance: int = property_data.get('rentBalance')
        self.total_rent_earned: int = property_data.get('totalRentEarned')
        self.latest_dividends_date: str = property_data.get('latestDividendsDate')
        self.latest_pending_dividends_date: str = property_data.get('latestPendingDividendsDate')
        coc: float = property_data.get('coc')
        self.coc: Optional[Decimal] = Decimal(str(coc)) if coc is not None else None
        irr: float = property_data.get('irr')
        self.irr: Optional[Decimal] = Decimal(str(irr)) if irr is not None else None
        property_status_data: dict = property_data.get('propertyStatus')
        self.property_status: PropertyStatus = PropertyStatus(
            property_status_data) if property_status_data is not None else None


class Summaries:
    def __init__(self, summaries_data: dict):
        # This is a weird part of their API - rather than having a list of properties, they
        # have this as a dictionary with each property's ID used as a key
        # So we manipulate that here to make it more sane.
        self.properties: list[Property] = [Property(property) for _, property in summaries_data.items()]


class Totals:
    def __init__(self, totals_data: dict):
        self.current_value: int = totals_data.get('currentValue')
        self.total_spent: int = totals_data.get('totalSpent')
        self.tokens: int = totals_data.get('tokens')
        self.total_withheld_amount: int = totals_data.get('totalWithheldAmount')
        self.tokens_purchased: int = totals_data.get('tokensPurchased')
        self.pending_tokens: int = totals_data.get('pendingTokens')
        total_cost_basis: float = totals_data.get('totalCostBasis')
        self.total_cost_basis: Optional[Decimal] = Decimal(
            str(total_cost_basis)) if total_cost_basis is not None else None
        self.total_entry_basis: int = totals_data.get('totalEntryBasis')
        self.total_rent: int = totals_data.get('totalRent')
        self.available_rent: int = totals_data.get('availableRent')


class Gift:
    def __init__(self, gift_data: dict):
        self.total: int = gift_data.get('total')
        self.spent: int = gift_data.get('spent')
        self.balance: int = gift_data.get('balance')
        self.currency: str = gift_data.get('currency')


class Balances:
    def __init__(self, balances_data: dict):
        gift_data: dict = balances_data.get('gift')
        self.gift: Gift = Gift(gift_data) if gift_data is not None else None


class UserStatusSummary:
    def __init__(self, user_status_summary_data: dict):
        summaries_data: dict = user_status_summary_data.get('summaries')
        self.summaries: Summaries = Summaries(summaries_data) if summaries_data is not None else None
        totals_data: dict = user_status_summary_data.get('totals')
        self.totals: Totals = Totals(totals_data) if totals_data is not None else None
        balances_data: dict = user_status_summary_data.get('balances')
        self.balances: Balances = Balances(balances_data) if balances_data is not None else None
