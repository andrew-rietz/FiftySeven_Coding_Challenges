"""
Defines and implements a simple point of sale system
"""
class Taxes():
    """
    Represents a simple point of sale system that calculates sales tax based
    on the shopper's state of residence

    Attributes:
        taxable_states: (dict) States and their associated tax rate (i.e.,
            {ST1: tax_rate1, ST2: tax_rate2}). For this exercise, only one
            state is entered
        state: (str) State in which the customer resides
        subtotal: (float) Total purchase amount before taxes
    """

    def __init__(self):
        """Initializes the class -- prompts user for input"""
        self.taxable_states = {
            "WI": 0.055,
        }
        self.subtotal = float(input("What is the order amount? "))
        self.state = str(input("What is the state? "))

    def checkout(self):
        """Calculates the total charges for the customer

        Args:
            n/a -- uses class attributes

        Returns:
            order: (Dict) {
                tax: (Float) total taxes due
                total: (Float) order subtotal + tax
            }
        """
        tax_rate = 0
        if self.state.upper() in self.taxable_states.keys():
            tax_rate += self.taxable_states[self.state.upper()]

        tax = self.subtotal * tax_rate
        order = {
            "tax": tax,
            "total": self.subtotal + tax,
        }
        return order

def main():
    pos = Taxes()
    order = pos.checkout()
    order_summary = ""

    if pos.state == "WI":
        order_summary += (
            f"The subtotal is ${pos.subtotal:,.2f}.\n" +
            f"The tax is ${order['tax']:,.2f}.\n"
        )

    order_summary += f"The total is ${order['total']:,.2f}."

    print(order_summary)


if __name__ == "__main__":
    main()
