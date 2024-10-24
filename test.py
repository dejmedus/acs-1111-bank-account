from bank import Bank
from bank_account import BankAccount

bank = Bank("Super Credit Union")
bank.create_account("Bob", "77abf435")
bank.deposit("77abf435", 1200)
bank.statement("77abf435")
bank.add_interest()
bank.statement("77abf435")
bank.withdraw("77abf435", 400)
bank.statement("77abf435")

mitchell_account = BankAccount("Mitchell", "31415920")
mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
mitchell_account.withdraw(150)
mitchell_account.print_statement()

flower_account = BankAccount("Flower",)
flower_account.deposit(40)
flower_account.print_statement()
flower_account.transfer(20, "31415920")
flower_account.print_statement()
