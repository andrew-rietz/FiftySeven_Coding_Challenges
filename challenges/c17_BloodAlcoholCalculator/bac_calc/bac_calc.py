class BACCalculator():
    """Represents a blood alcohol calculator

    Attributes:
        gender: gender of the person
        weight: weight of the person
        drinks: number of drinks person had
        type: type of drinks the person had
        hrs_since_last_drink: elapsed time since last drink
        legal: boolean indicator of whether the person can drive
    """
    LEGAL_BAC = 0.08
    BEVERAGES = {
        "beer": {"alcohol": 5, "oz": 12},
        "wine": {"alcohol": 12, "oz": 5},
        "liquor": {"alcohol": 40, "oz": 1.5},
    }
    GENDERS = ["M", "F"]

    def __init__(
            self, gender=None, weight=None, drinks=None, type=None,
            hrs_since_last_drink=None, legal=True):
        """Initialize the class"""
        self.gender = gender
        self.weight = weight
        self.drinks = drinks
        self.type = type
        self.hrs_since_last_drink = hrs_since_last_drink
        self.legal = legal

    def set_legality(self, bac):
        """Determines whether the person can legally drive"""
        self.legal = bac < self.LEGAL_BAC

    def test_bac(self):
        """Calculates the person's blood-alcohol content

        The formula to calculate BAC is:
        `BAC = (Alcohol * 5.14 / Weight * r) - 0.015 * hrs_since_last_drink`
        where r = 0.73 for men and 0.66 for women

        Returns:
            bac: blood alcohol content of the person
        """
        beverage = self.BEVERAGES[self.type]
        r = 0.73 if self.gender.upper() == "M" else 0.66
        alcohol_volume = self.drinks * beverage["oz"] * beverage["alcohol"] / 100
        bac = (alcohol_volume * 5.14 / self.weight * r) - 0.015 * self.hrs_since_last_drink
        self.set_legality(bac)
        return bac

def get_positive_number(prompt, err_msg):
    """Prompts user for input until they enter a positive number

    Args:
        prompt: Prompt the user for input
        err_msg: Message to be displayed if user provides bad input

    Returns:
        positive_val: Positive numeric value from user
    """
    while True:
        try:
            positive_val = float(input(f"{prompt.strip()} "))
            if positive_val < 0:
                raise ValueError
            break
        except ValueError:
            print(f"{err_msg.strip()} ", end="")

    return positive_val

def get_string_in_list(prompt, err_msg, allowed_vals, case_sensitive=False):
    """Prompts user for input until they enter an allowed value

    Args:
        prompt: Prompt the user for input
        err_msg: Message to be displayed if user provides bad input
        allowed_vals: List of expected values allowed by the function
        case_sensitive: (Default = True) Tests the values in a case_sensitive manner

    Returns:
        accepted_val: User input from the given list of allowed values
    """
    if not case_sensitive:
        allowed_vals = [val.lower() for val in allowed_vals]

    while True:
        user_val = input(f"{prompt.strip()} ")
        test_val = user_val.lower() if not case_sensitive else user_val
        if test_val not in allowed_vals:
            print(err_msg.strip(), end=" ")
            continue
        return user_val

def main():
    calc = BACCalculator()
    calc.gender = get_string_in_list(
        prompt=f"What is your gender ({'/'.join(calc.GENDERS)})?",
        err_msg="Please enter a valid value.",
        allowed_vals=calc.GENDERS,
        case_sensitive=False
    )
    calc.weight = get_positive_number(
        prompt="How much do you weigh (in pounds)?",
        err_msg="Please enter a numeric value."
    )
    calc.drinks = get_positive_number(
        prompt="How many drinks have you had?",
        err_msg="Please enter a numeric value."
    )
    calc.type = get_string_in_list(
        prompt=f"Are you drinking ({', '.join(calc.BEVERAGES)})?",
        err_msg="Please enter a valid value.",
        allowed_vals=calc.BEVERAGES,
        case_sensitive=False
    )
    calc.hrs_since_last_drink = get_positive_number(
        prompt="How long ago was your last drink (in hours)?",
        err_msg="Please enter a numeric value."
    )

    bac = calc.test_bac()
    legal_illegal = "legal" if calc.legal else "illegal"
    print(
        f"Your BAC is {bac:.2f}.\n" +
        f"It is {legal_illegal} for you to drive."
    )

if __name__ == "__main__":
    main()
