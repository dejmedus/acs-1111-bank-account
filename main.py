from bank import Bank
from bank_account import BankAccount

# bank new member
bank = Bank("Super Credit Union")
bank.add_member("Bob", "77abf435")
bank.deposit("77abf435", 1200)
bank.statement("77abf435")
bank.add_interest()
bank.statement("77abf435")
bank.withdraw("77abf435", 400)
bank.statement("77abf435")


# Create a new bank account instance
mitchell_account = BankAccount("Mitchell", "31415920")

# Deposit $400,000 into "Mitchell's" account.
mitchell_account.deposit(400000)

# Print a statement
mitchell_account.print_statement()

# Add interest to the account
mitchell_account.add_interest()

# Print a statement
mitchell_account.print_statement()

# Make a withdrawl of $150 (Mitchell needs some Yeezy's)
mitchell_account.withdraw(150)

# Print a statement
mitchell_account.print_statement()
