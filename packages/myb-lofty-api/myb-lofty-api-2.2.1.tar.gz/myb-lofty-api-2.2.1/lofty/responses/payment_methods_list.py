class PaymentMethods:
    def __init__(self, payment_methods_data: dict):
        self.type: str = payment_methods_data.get('type')
        self.id: str = payment_methods_data.get('id')
        self.country: str = payment_methods_data.get('country')
        self.bank_name: str = payment_methods_data.get('bankName')
        self.routing_number: str = payment_methods_data.get('routingNumber')
        self.last4: str = payment_methods_data.get('last4')


class PaymentMethodsList:
    def __init__(self, payment_methods_list_data: list):
        self.payment_methods: list[PaymentMethods] = [PaymentMethods(item) for item in payment_methods_list_data]


