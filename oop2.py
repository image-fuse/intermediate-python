class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        
    def __del__(self):
        print(f"Bank account {self.account_number} has been closed.")

class Customer:
    def __init__(self, name, age, address, account_number, balance, account_type):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = BankAccount(account_number, balance, account_type)
        
    def __del__(self):
        print(f"Customer {self.name} has been removed from records.")

# Creating instances
customer1 = Customer("Sita", 30, "Sankhamul", "123456789", 50000, "Savings")
customer2 = Customer("Ram", 25, "Sanepa", "987654321", 80000, "Checking")

# Displaying customer and account information
print("Customer 1:")
print(f"Name: {customer1.name}")
print(f"Age: {customer1.age}")
print(f"Address: {customer1.address}")
print(f"Account Number: {customer1.bank_account.account_number}")
print(f"Account Balance: {customer1.bank_account.balance}")
print(f"Account Type: {customer1.bank_account.account_type}")
print("\n")

print("Customer 2:")
print(f"Name: {customer2.name}")
print(f"Age: {customer2.age}")
print(f"Address: {customer2.address}")
print(f"Account Number: {customer2.bank_account.account_number}")
print(f"Account Balance: {customer2.bank_account.balance}")
print(f"Account Type: {customer2.bank_account.account_type}")

# Deleting instances
del customer1
del customer2
