class LoginSystem():
    """A representation of a user login / authentication system

    Attributes:
        password: (String) A password previously registered by the user
    """

    def __init__(self):
        """Initializes the class"""
        self.password = "abc$123"

    def login(self, password):
        """Compares the entered password against the stored password

        Args:
            password: (String) value entered on the login screen

        Returns:
            bool: Boolean comparison of the password and self.password
        """
        if password == self.password:
            return True
        return False


def main():
    users = LoginSystem()
    password = input("What is the password? ")
    success = users.login(password)
    if success:
        print("Welcome!")
    else:
        print("I don't know you.")

if __name__ == "__main__":
    main()
