"""
Defines and implements a login / authentication class
"""
class LoginSystem():
    """
    A representation of a user login / authentication system

    Attributes:
        password: (str) A password previously registered by the user
    """

    def __init__(self):
        """Initializes the class"""
        self._password = "abc$123"

    def login(self, password):
        """Compares the entered password against the stored password

        Args:
            password: (String) value entered on the login screen

        Returns:
            bool: Boolean comparison of the password and self.password
        """
        return password == self._password


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
