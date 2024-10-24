from classes.bank import Bank
from classes.atm import ATM


bank = Bank("Super Credit Union")
bank.create_account("Mitchell", "savings", "31415920")

atm = ATM(bank)

atm.display_welcome_screen()
