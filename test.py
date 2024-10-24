from classes.bank import Bank

bank = Bank("Super Credit Union")

bob_account = bank.create_account("Bob")
bob_account_num = bob_account.account_number
bank.deposit(bob_account_num, 1200)
bank.add_interest()
bank.statement(bob_account_num)
bank.withdraw(bob_account_num, 400)
bank.statement(bob_account_num)

mitchell_account = bank.create_account("Mitchell", "savings", "31415920")
mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
mitchell_account.withdraw(150)
mitchell_account.print_statement()

bank.transfer("31415920", bob_account_num, 20)
bank.statement(bob_account_num)
