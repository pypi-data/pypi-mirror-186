from typing import Optional
from decimal import Decimal


class Transaction:
    def __init__(self, transaction_data: dict):
        self.property_id: str = transaction_data.get('propertyId')
        self.direction: str = transaction_data.get('direction')
        total: float = transaction_data.get('total')
        self.total: Optional[Decimal] = Decimal(str(total)) if total is not None else None
        self.created_at: int = transaction_data.get('createdAt')
        self.quantity: int = transaction_data.get('quantity')
        self.payment_currency: str = transaction_data.get('paymentCurrency')
        price: float = transaction_data.get('price')
        self.price: Optional[Decimal] = Decimal(str(price)) if price is not None else None


