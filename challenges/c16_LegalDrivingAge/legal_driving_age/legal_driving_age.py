def check_legal_driver(age, country):
    """Asks user for their age and determines whether they are old enough to drive

    Args:
        age: age of the individual
        country: country in which they wish to drive

    Returns:
        string: If country is recognized, returns whether the individual is old
            enough to drive. Otherwise responds that the country is not recognized
    """
    valid_age_by_country = {
        "UNITED STATES": 16,
        "USA": 16,
        "US": 16,
        "MEXICO": 18,
        "MX": 18,
        "MEX": 18,
    }
    check = "aren't" if age < valid_age_by_country[country.upper()] else "are"
    return f"You {check} old enough to legally drive in {country}."

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

def main():
    age = get_positive_number(
        prompt="What is your age?",
        err_msg="Please enter a numeric value greater than or equal to zero."
    )
    print(check_legal_driver(age, "MEX"))

if __name__ == "__main__":
    main()
