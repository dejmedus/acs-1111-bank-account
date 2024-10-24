import uuid
from bank_account import BankAccount, AccountType


class Bank():
    """
A class to represent a bank.

...

Attributes
----------
name : str
  name of the bank
accounts : dict of accounts
   all bank member accounts

Methods
-------
create_account():
    add new member account

add_interest():
    add interest to all account balances

transfer(from_account_number, to_account_number, amount):
    transfer amount from account to another

deposit(account_number, amount):
    add amount to account balance

withdraw(account_number, amount):
    subtract amount from account balance

statement(account_number):
    displays account statement

get_account(account_number):
    if account of account number exists, returns the account

    returns account instance or None

account_action(account_number, function):
    if account of account number exists, completes account action
"""

    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, full_name, account_type=AccountType.DAILY, account_number=str(uuid.uuid4())[:8]):
        if len(full_name.strip()) == 0:
            print("Please enter a full name")
            return None

        new_member = BankAccount(full_name, account_type, account_number, 0)
        self.accounts[account_number] = new_member
        return new_member

    def add_interest(self):
        for account_number, account in self.accounts.items():
            account.add_interest()

    def transfer(self, from_account_number, to_account_number, amount):
        withdraw_complete = self.account_action(
            from_account_number, lambda account: account.withdraw(amount))

        if withdraw_complete == False:
            print("Transfer cancelled")
            return

        self.account_action(
            to_account_number, lambda account: account.deposit(amount, True))

    def deposit(self, account_number, amount):
        self.account_action(
            account_number, lambda account: account.deposit(amount))

    def withdraw(self, account_number, amount):
        self.account_action(
            account_number, lambda account: account.withdraw(amount))

    def statement(self, account_number):
        self.account_action(
            account_number, lambda account: account.print_statement())

    def get_account(self, account_number):
        if account_number not in self.accounts:
            print(f"No account number {account_number}")
            return None
        else:
            return self.accounts[account_number]

    def account_action(self, account_number, function):
        account = self.get_account(account_number)

        if account is None:
            return

        return function(account)
