class Transactions:
    def __init__(self, transactions_data: dict):
        self.quantity: int = transactions_data.get('quantity')
        self.data_type: str = transactions_data.get('dataType')
        self.property_id: str = transactions_data.get('propertyId')
        self.status: str = transactions_data.get('status')
        self.created_at: int = transactions_data.get('createdAt')
        self.payment_currency: str = transactions_data.get('paymentCurrency')
        self.txn_id: str = transactions_data.get('txnId')
        self.user_sub: str = transactions_data.get('userSub')
        self.date: str = transactions_data.get('date')
        self.user_id: str = transactions_data.get('userId')
        self.updated_at: int = transactions_data.get('updatedAt')
        self.units: int = transactions_data.get('units')
        self.amount: int = transactions_data.get('amount')
        self.tokens: int = transactions_data.get('tokens')
        self.type: str = transactions_data.get('type')
        self.sk_1: str = transactions_data.get('SK_1')


class Meta:
    def __init__(self, meta_data: dict):
        self.next: str = meta_data.get('next')
        self.sort: str = meta_data.get('sort')
        self.page_size: int = meta_data.get('pageSize')


class TransactionsByUser:
    def __init__(self, transactions_by_user_data: dict):
        self.transactions: list[Transactions] = [Transactions(item) for item in transactions_by_user_data.get('transactions')]
        meta_data: dict = transactions_by_user_data.get('meta')
        self.meta: Meta = Meta(meta_data) if meta_data is not None else None


