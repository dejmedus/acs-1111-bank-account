from bank import Bank
from atm import ATM


bank = Bank("Super Credit Union")
bank.create_account("Mitchell", "31415920")

atm = ATM(bank)

atm.display_welcome_screen()
