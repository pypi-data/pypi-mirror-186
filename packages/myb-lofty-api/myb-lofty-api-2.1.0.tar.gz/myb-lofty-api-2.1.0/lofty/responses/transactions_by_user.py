class Transaction:
    def __init__(self, transactions_data: dict):
        self.quantity: int = transactions_data.get('quantity')
        # Example: 'DIVIDEND', 'WITHDRAWAL_REQUEST'
        self.data_type: str = transactions_data.get('dataType')
        # Some (withdrawal) transactions have the property id under just 'id'
        self.property_id: str = transactions_data.get('propertyId') or transactions_data.get('id')
        # Example: 'success'
        self.status: str = transactions_data.get('status')
        self.created_at: int = transactions_data.get('createdAt')
        # Example: 'usd'
        self.payment_currency: str = transactions_data.get('paymentCurrency')
        self.txn_id: str = transactions_data.get('txnId')
        self.user_sub: str = transactions_data.get('userSub')
        self.date: str = transactions_data.get('date')
        self.user_id: str = transactions_data.get('userId')
        self.updated_at: int = transactions_data.get('updatedAt')
        self.units: int = transactions_data.get('units')
        # Note that amounts come in 100000x higher than real values to avoid decimals
        self.amount: int = transactions_data.get('amount')
        self.tokens: int = transactions_data.get('tokens')
        # Example: 'rent' or 'withdrawal'
        self.type: str = transactions_data.get('type')
        self.sk_1: str = transactions_data.get('SK_1')

        # These properties are only found when the type is 'withdrawal'
        self.withdrawal_request_id = transactions_data.get('withdrawalRequestId')
        # Example: 'bank_transfer'
        self.payment_method = transactions_data.get('paymentMethod')

        # There are some other withdrawal transactions that have the following fields
        # Example: 'BREX'
        self.payment_provider = transactions_data.get('paymentProvider')
        # Example: 'ACH'
        self.payment_subtype = transactions_data.get('paymentSubtype')
        self.email = transactions_data.get('email')
        self.provider_transfer_id = transactions_data.get('providerTransferId')
        # Example: 'pending'
        self.lofty_status = transactions_data.get('loftyStatus')
        # Example: 'Brex ACH Withdrawal ID#01xyz'
        self.provider_message = transactions_data.get('providerMessage')
        # Example: 'SCHEDULED
        self.provider_status = transactions_data.get('providerStatus')
        # Example: 'fiat'
        self.payment_type = transactions_data.get('paymentType')
        # Example: 'SAVINGS/012345678/0123456789012'
        self.target_account = transactions_data.get('targetAccount')

    @property
    def is_rent(self):
        return self.type == 'rent'


class Meta:
    def __init__(self, meta_data: dict):
        self.next: str = meta_data.get('next')
        self.sort: str = meta_data.get('sort')
        self.page_size: int = meta_data.get('pageSize')


class TransactionsByUser:
    def __init__(self, transactions_by_user_data: dict):
        self.transactions: list[Transaction] = [Transaction(item) for item in
                                                transactions_by_user_data.get('transactions')]
        meta_data: dict = transactions_by_user_data.get('meta')
        self.meta: Meta = Meta(meta_data) if meta_data is not None else None
