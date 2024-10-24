from bank import Bank


class ATM():
    """
A class to represent an ATM.

...

Attributes
----------
bank : Bank
  the bank the ATM belongs to

Methods
-------
display_home_screen():
    display options to logged in users

display_welcome_screen():
    display welcome message and log in screen
"""

    def __init__(self, bank: Bank):
        self.bank = bank

    def display_home_screen(self, account_number):
        options = """Select an option:
        1. View Balance
        2. Deposit
        3. Withdraw
        4. Transfer
        5. Log out
"""

        while True:
            selection = int(input(options))
            if selection == 1:
                self.bank.statement(account_number)
            elif selection == 2:
                amount = int(input("Deposit amount: "))
                self.bank.deposit(account_number, amount)
            elif selection == 3:
                amount = int(input("Withdrawal amount: "))
                self.bank.withdraw(account_number, amount)
            elif selection == 4:
                to_account_number = input("to_account_number")
                amount = int(input("Deposit amount: "))
                self.bank.transfer(
                    account_number, to_account_number, amount)
            elif selection == 5:
                print('Thanks for banking!')
                print('Logging out...')
                quit()
            else:
                print('Selection invalid. Please try again.')

    def display_welcome_screen(self):
        print(f'\nWelcome to the {self.bank.name} ATM!\n')

        name = input('Name: ')
        account_number = input('Account #: ')

        found_account = self.bank.get_account(account_number)

        if not found_account or found_account.full_name != name:
            print("Your details were incorrect. Please try again.")
            self.display_welcome_screen()

        else:
            self.display_home_screen(account_number)
