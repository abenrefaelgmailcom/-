
# Homework - TDD Practice
# BankAccount implementation


class BankAccount:
    """A simple bank account with deposit and withdrawal operations."""

    def __init__(self):
        # A new account starts with zero balance.
        self.balance = 0

    def deposit(self, amount):
        """Add money to the account."""
        self.balance += amount

    def withdraw(self, amount):
        """Remove money from the account."""
        self.balance -= amount

    def get_balance(self):
        """Return the current account balance."""
        return self.balance

    def is_empty(self):
        """Return True if the balance is zero."""
        return self.balance == 0