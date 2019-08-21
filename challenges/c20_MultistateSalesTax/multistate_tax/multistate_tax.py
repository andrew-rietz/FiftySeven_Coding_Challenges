"""
Class and functions for calculating sales tax. Incorporates state- and
county-level tax rates
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from util_functions.utils import user_inputs


class MultistateTaxes():
    """Represents a simple point of sale system

    Attributes:
        STATES: (List) Constant defining the abbreviations for each of the 50 states
        STATE_TAX: (Dictionary) Base tax rate for each state
        COUNTY_TAX: (Dictionary) Incremental tax rate for each county, by state

        subtotal: (Float) Total purchase amount before taxes
        state: (String) State in which the customer resides
        county: (String) County in which the customer resides
    """

    STATES = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL",
        "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME",
        "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH",
        "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
        "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI",
        "WY"
    ]
    STATE_TAX = {
        "WI": 0.05,
        "IL": 0.08,
    }
    COUNTY_TAX = {
        "WI": {
            "EAU CLAIRE": 0.005,
            "DUNN": 0.004,
        }
    }

    def __init__(self, subtotal=None, state=None, county=None):
        """Initializes the class -- prompts user for input"""
        self.subtotal = subtotal
        self.state = state
        self.county = county

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
        tax_rate = (
            self.STATE_TAX.get(self.state, 0) +
            self.COUNTY_TAX.get(self.state, {}).get(self.county, 0)
        )

        tax = self.subtotal * tax_rate
        order = {
            "tax": float(tax),
            "total": float(self.subtotal + tax),
        }
        return order

def main():
    cart = MultistateTaxes()
    cart.subtotal = user_inputs.get_positive_number(
        prompt="What is the order amount?",
        err_msg="Please enter a valid number."
    )
    cart.state = user_inputs.get_string_in_list(
        prompt="What state do you live in? (Enter the abbreviation):",
        err_msg="Please enter a valid state abbreviation.",
        allowed_vals=cart.STATES,
        case_sensitive=False
    ).upper()
    cart.county = input(
        "What county do you live in? (Don't include the word 'county' in your answer): "
    ).upper()

    order = cart.checkout()

    order_summary = ""
    if order["tax"] != 0:
        order_summary += f"The tax is ${order['tax']:,.2f}.\n"
    order_summary += f"The total is ${order['total']:,.2f}."
    print(order_summary)


if __name__ == "__main__":
    main()
