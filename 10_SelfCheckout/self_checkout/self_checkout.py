class Shopper():
    """
    Representation of a shopper or shopping cart
    Attributes:
    cart                (dictionary)

    Constants:
    TAX_RATE            (float)
    """
    TAX_RATE = 0.055

    def __init__(self):
        self.cart = {}

    def add_item(self, price, qty):
        item_number = 1 if not self.cart else max(self.cart.keys())+1
        self.cart[item_number] = {
            "price": price,
            "quantity": qty,
        }
        return self.cart[item_number]

    def checkout(self):
        order = {"subtotal": 0, "tax": 0, "total": 0}
        for item, price_quantity in self.cart.items():
            order["subtotal"] += price_quantity["price"] * price_quantity["quantity"]

        order["tax"] = order["subtotal"] * self.TAX_RATE
        order["total"] = order["subtotal"] + order["tax"]

        return order

def main():
    a_shopper = Shopper()

    while True:
        print("\nEnter a blank line to exit.")
        price = input("Enter the price of an item: ")
        if not price:
            break
        quantity = input("Enter the quantity of an item: ")
        a_shopper.add_item(float(price), float(quantity))

    order_total = a_shopper.checkout()
    print(
        f"Subtotal: ${order_total['subtotal']:,.2f}\n" +
        f"Tax: ${order_total['tax']:,.2f}\n" +
        f"Total: ${order_total['total']:,.2f}\n\n"
    )

if __name__ == "__main__":
    main()
