"""
This script defines the BankAccount and Customer classes to represent bank accounts and customers.
"""

class BankAccount:
    """
    A class representing a bank account.
    """
    def __init__(self, account_number: str, balance: float, account_type: str):
        """
        Initialize a BankAccount object.

        Parameters:
        account_number (str): The account number.
        balance (float): The account balance.
        account_type (str): The type of the account (e.g., Savings, Checking).

        Returns:
        None
        """
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        """
        Destructor for the BankAccount class.

        Returns:
        None
        """
        print(f"Bank account {self.account_number} has been closed.")


class Customer:
    """
    A class representing a customer.
    """
    def __init__(self, name: str, age: int, address: str,
                 account_number: str, balance: float, account_type: str):
        """
        Initialize a Customer object.

        Parameters:
        name (str): The customer's name.
        age (int): The customer's age.
        address (str): The customer's address.
        account_number (str): The account number.
        balance (float): The account balance.
        account_type (str): The type of the account (e.g., Savings, Checking).

        Returns:
        None
        """
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = BankAccount(account_number, balance, account_type)

    def __del__(self):
        """
        Destructor for the Customer class.

        Returns:
        None
        """
        print(f"Customer {self.name} has been removed from records.")


# Creating instances
CUSTOMER1 = Customer("Sita", 30, "Sankhamul", "123456789", 50000.0, "Savings")
CUSTOMER2 = Customer("Ram", 25, "Sanepa", "987654321", 80000.0, "Checking")

# Displaying customer and account information
print("Customer 1:")
print(f"Name: {CUSTOMER1.name}")
print(f"Age: {CUSTOMER1.age}")
print(f"Address: {CUSTOMER1.address}")
print(f"Account Number: {CUSTOMER1.bank_account.account_number}")
print(f"Account Balance: {CUSTOMER1.bank_account.balance}")
print(f"Account Type: {CUSTOMER1.bank_account.account_type}")
print("\n")

print("Customer 2:")
print(f"Name: {CUSTOMER2.name}")
print(f"Age: {CUSTOMER2.age}")
print(f"Address: {CUSTOMER2.address}")
print(f"Account Number: {CUSTOMER2.bank_account.account_number}")
print(f"Account Balance: {CUSTOMER2.bank_account.balance}")
print(f"Account Type: {CUSTOMER2.bank_account.account_type}")
print("\n")

# Deleting instances
del CUSTOMER1
del CUSTOMER2
