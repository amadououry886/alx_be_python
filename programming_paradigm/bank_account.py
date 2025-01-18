import os

class BankAccount:
    def __init__(self, initial_balance=100, file_path="account_balance.txt"):
        """
        Initialize a new BankAccount instance.

        :param initial_balance: Optional; The starting balance for the account. Defaults to 0.
        :param file_path: Optional; The file path where the balance will be stored. Defaults to 'account_balance.txt'.
        """
        self.__account_balance = initial_balance
        self.file_path = file_path

        # If the file exists, load the balance; otherwise, save the initial balance
        if os.path.exists(self.file_path):
            self.__load_balance()
        else:
            self.__save_balance()

    def deposit(self, amount):
        """
        Deposit money into the account.

        :param amount: The amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount
            self.__save_balance()

    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.

        :param amount: The amount to withdraw.
        :return: True if withdrawal was successful, False otherwise.
        """
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            self.__save_balance()
            
            return True
        return False

    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

    def __save_balance(self):
        """
        Save the current account balance to a file.
        """
        try:
            with open(self.file_path, "w") as file:
                file.write(str(self.__account_balance))
        except OSError as e:
            print(f"Error saving balance: {e}")

    def __load_balance(self):
        """
        Load the account balance from a file.
        """
        try:
            with open(self.file_path, "r") as file:
                self.__account_balance = float(file.read())
        except (OSError, ValueError) as e:
            print(f"Error loading balance: {e}")
            self.__account_balance = 0
