class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulation: Balance is private and can only be accessed via class methods
        self._account_balance = initial_balance

    def deposit(self, amount):
        # Deposit money into the account
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        # Withdraw money from the account if enough balance is available
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        # Display the current account balance
        print(f"Current Balance: ${self._account_balance:.2f}")
