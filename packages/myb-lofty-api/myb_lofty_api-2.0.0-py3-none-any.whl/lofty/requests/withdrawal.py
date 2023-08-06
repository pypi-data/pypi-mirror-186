class Withdrawal:
    def __init__(self, amount: float, method: str):
        if amount < 1.0:
            raise ValueError('amount must be >= 1.0')

        self.amount = amount

        # One of WithdrawalMethod
        self.method = method

    def to_dict(self) -> dict:
        return {
            'withdrawalAmount': self.amount,
            'method': self.method
        }