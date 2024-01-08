class Account:
    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __len__(self):
        return len(self._transactions)

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.balance == other.balance
        raise TypeError("Comparing account should be done with another Account")

    def __le__(self, other):
        if isinstance(other, Account):
            return self.balance <= other.balance
        raise TypeError("Comparing account should be done with another Account")

    def __lt__(self, other):
        if isinstance(other, Account):
            return self.balance < other.balance
        raise TypeError("Comparing account should be done with another Account")

    def __ge__(self, other):
        if isinstance(other, Account):
            return self.balance >= other.balance
        raise TypeError("Comparing an account should be done with another account")

    def __gt__(self, other):
        if isinstance(other, Account):
            return self.balance > other.balance
        raise TypeError("Comparing an account should be done with another account")

    def __ne__(self, other):
        if isinstance(other, Account):
            return self.balance != other.balance
        raise TypeError("Comparing an account should be done with another account")

    def __getitem__(self, position):
        return self._transactions[position]

    def __iter__(self):
        return iter(self._transactions)

    def __add__(self, amount):
        if not isinstance(amount, int):
            raise TypeError("The given amount has to be an integer")
        self._transactions.append(amount)
        return self

    def __sub__(self, amount):
        if not isinstance(amount, int):
            raise TypeError("The given amount has to be an integer")
        self._transactions.append(-amount)
        return self

    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"
