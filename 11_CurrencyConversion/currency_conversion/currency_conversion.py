class CurrencyConverter():
    """
    A representation of a currency conversion service
    Attributes:
    amount_from         (float)
    rate_from           (float)
    rate_to             (float)
    """

    def __init__(self):
        self.amount_from = float(input("How many euros are you exchanging? "))
        self.rate_from = float(input("What is the exchange rate? "))
        # By default, the exchange rate of any currency with itself is 1.00
        self.rate_to = 100

    def convert(self):
        return (self.amount_from * self.rate_from / self.rate_to)

def main():
    exchanger = CurrencyConverter()
    converted_value = exchanger.convert()
    print(
        f"{exchanger.amount_from} euros at an exchange rate of " +
        f"{exchanger.rate_from} is {converted_value:,.2f} U.S. dollars."
    )

if __name__ == "__main__":
    main()
