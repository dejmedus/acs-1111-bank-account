
class BankAccount:
    """
   A class to represent a bank account.

   ...

   Attributes
   ----------
   full_name : str
      full name of the bank account owner
   account_number : int
       8-digit bank account number
   balance : float
       current balance

   Methods
   -------
    deposit(amount=0):
        add amount to balance and display new balance

    withdraw(amount=0):
        subtract amount from the balance and display new balance

    get_balance(amount=0):
        display current balance

        Returns
        -------
        balance : float

    add_interest(interest=0.00083):
        add interest to the balance

    print_statement():
        display account name, account number, and balance
   """

    def __init__(self, full_name, account_number, balance=0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount withdrawn: ${amount} new balance: ${self.balance}")

    def get_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

    def add_interest(self, interest=0.00083):
        pass

    def print_statement(self):
        print(f"""
{self.full_name}
Account No.: ****{str(self.account_number)[3:]}
Balance: ${self.balance}
""")
