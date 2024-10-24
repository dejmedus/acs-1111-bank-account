import uuid
from bank_account import BankAccount


class Bank():
    """
A class to represent a bank account.

...

Attributes
----------
name : str
  name of the bank
accounts : list of accounts
   all bank member accounts

Methods
-------
add_member():
    add new member bank account

add_interest():
    add interest to all account balances

transfer(from_account_number, to_account_number, amount):
    transfer amount from account to another

deposit(account_number, amount):
    add amount to account balance

withdraw(account_number, amount):
    subtract amount from account balance
"""

    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_member(self, full_name, account_number=str(uuid.uuid4())[:8]):

        if len(full_name.strip()) == 0:
            raise Exception("Please enter a full name")

        new_member = BankAccount(full_name, account_number, 0)
        self.accounts[account_number] = new_member
        print(
            f"New Account: {new_member.full_name} {new_member.account_number} added\n")

    def add_interest(self):
        for account_number, account in self.accounts.items():
            account.add_interest()

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        from_account.withdraw(amount)
        to_account.deposit(amount)

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        account.withdraw(amount)

    def statement(self, account_number):
        account = self.get_account(account_number)
        account.print_statement()

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise Exception(f"No account number {account_number}")
        else:
            return self.accounts[account_number]
