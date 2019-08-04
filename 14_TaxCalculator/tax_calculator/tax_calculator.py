class Taxes():
    """Represents a simple point of sale system

    Attributes:
        taxable_states: (Dict) States and their associated tax rate
            {ST: tax_rate, ST2: tax_rate2}
        state: (String) State in which the customer resides
        subtotal: (Float) Total purchase amount before taxes
    """

    def __init__(self):
        """Initializes the class -- prompts user for input"""
        self.subtotal = float(input("What is the order amount? "))
        self.taxable_states = {
            "WI": 0.055,
        }
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
