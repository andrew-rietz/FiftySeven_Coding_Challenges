"""

Pulling data from a file into a complex data
structure makes parsing much simpler. Many
programming languages support the JSON format, a
popular way of representing data. Create a program
that takes a product name as input and retrieves
the current price and quantity for that product.
The product data is in a data file in the JSON
format and looks like this:

{
    "products" : [
        {"name": "Widget", "price": 25.00, "quantity": 5 },
        {"name": "Thing", "price": 15.00, "quantity": 5 },
        {"name": "Doodad", "price": 5.00, "quantity": 10 },
    ]
}

Print out the product name, price, and the quantity
if the product is found. If no product matches
the search, state that no product was found and
start over.

___________________
Example Output
___________________
What is the product name? iPad
Sorry, that product was not found in our inventory.
What is the product name? Widget
Name: Widget
Price: $25.00
Quantity on hand: 5

___________________
Constraints
___________________
- The file is in the JSON format. Use a JSON parser
to pull the values out of the file.
- If no record is found, prompt again.

"""


def createDummyJSON():
    jsonText = """\
    {
        "products" : [
            {"name": "Widget", "price": 25.00, "quantity": 5 },
            {"name": "Thing", "price": 15.00, "quantity": 5 },
            {"name": "Doodad", "price": 5.00, "quantity": 10 }
        ]
    }\
    """
    with open("./44_ProductSearch/44_dummyJSON.json", "w") as writer:
        writer.write(jsonText)

    return "JSON file created"


"""
def selectProduct(products, userProduct):
    productInfo =
    return productInfo
"""


def main():
    import json

    createDummyJSON()
    with open("./44_ProductSearch/44_dummyJSON.json", "r") as reader:
        jsonData = json.load(reader)

    products = jsonData["products"]
    store = {}
    for product in products:
        store[product["name"].upper()] = product

    while True:
        userSearch = input("What is the product name? ")
        if userSearch.upper() in store.keys():
            print(
                f"Name: {store[userSearch.upper()]['name']}"
                + f"\nPrice: ${store[userSearch.upper()]['price']:.2f}"
                + f"\nQuantity on hand: {store[userSearch.upper()]['quantity']}"
            )
            break
        else:
            print("Sorry, that product was not found in our inventory.")


main()
