class Payment:
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} by card"

class CashPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} by cash"

class PaymentContext:
    def __init__(self, strategy: Payment):
        self.strategy = strategy

    def execute(self, amount):
        return self.strategy.pay(amount)
