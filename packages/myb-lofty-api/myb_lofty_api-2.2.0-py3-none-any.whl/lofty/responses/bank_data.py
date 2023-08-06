class BankData:
    def __init__(self, bank_data_data: dict):
        self.account_number: str = bank_data_data.get('accountNumber')
        self.ach_routing_number: str = bank_data_data.get('achRoutingNumber')
        self.account_type: str = bank_data_data.get('accountType')
        self.paypal_account: str = bank_data_data.get('paypalAccount')


