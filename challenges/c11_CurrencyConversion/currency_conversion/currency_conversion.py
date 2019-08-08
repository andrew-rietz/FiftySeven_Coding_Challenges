"""
Defines and implements a CurrencyConverter calculator
"""
class CurrencyConverter():
    """
    A representation of a currency conversion service that takes some amount of money
    in a base currency and a conversion rate. Then converts to a new currency.

    Attributes:
        amount_from: A float indicating the amount of money in the base currency
        rate_from: A float representing the conversion rate from base currency to
            desired currency. Given as (desired currency per 100 base currency).
            (i.e., If desired currency is worth twice as much as base currency,
            then `rate_from` would be 200)
        rate_to: Constant integer of 100
    """

    def __init__(self):
        self.amount_from = float(input("How many euros are you exchanging? "))
        self.rate_from = float(input("What is the exchange rate? "))
        # By default, the exchange rate of any currency with itself is 1.00
        self.rate_to = 100

    def convert(self):
        return self.amount_from * self.rate_from / self.rate_to

def main():
    exchanger = CurrencyConverter()
    converted_value = exchanger.convert()
    print(
        f"{exchanger.amount_from} euros at an exchange rate of " +
        f"{exchanger.rate_from} is {converted_value:,.2f} U.S. dollars."
    )

if __name__ == "__main__":
    main()
