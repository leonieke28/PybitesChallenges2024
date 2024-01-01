def greeting(name):
    """Return a greeting for given name."""
    return "Hello " + name


def headline(text, centered=False, symbol="o"):
    """Return the text in title case and with additional markup.

    If centered is True, use symbol to fill spaces.
    If centered is False, title will have a line of "-" under it.
    """
    if not centered:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, symbol)


class BankAccount:
    """Simple class to handle a bank account. Can only deal with integer amounts."""

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def overdrawn(self):
        return self.balance < 0