class PaymentGateway:
  def make_payment(self, amount, currency):
    # Payment gateway specific logic
    pass

class LegacyPaymentProcessor:
  def process_payment(self, amount):
    # Legacy system specific logic
    pass

class PaymentGatewayAdapter(PaymentGateway):
  def __init__(self, legacy_processor):
    self.legacy_processor = legacy_processor

  def make_payment(self, amount, currency):
    # Convert currency if needed
    converted_amount = convert_currency(amount, currency)
    self.legacy_processor.process_payment(converted_amount)

# Usage
gateway = PaymentGateway()  # Incompatible with application logic
legacy_processor = LegacyPaymentProcessor()
adapter = PaymentGatewayAdapter(legacy_processor)

# Use the adapter to make payments through the legacy system
adapter.make_payment(100, "USD")
