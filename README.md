### Bank Account

A Python program that simulates a bank account, using object-oriented programming concepts.

#### Run Commands

- `python3 main.py` => the application & prompts for user input
- `python3 test.py` => the manually created Bank and BankAccount instances & methods

#### Resources
- [Python class docstrings](https://www.programiz.com/python-programming/docstrings)
- [UUIDs](https://docs.python.org/3/library/uuid.html)
- [Faux UUID](https://stackoverflow.com/questions/13484726/safe-enough-8-character-short-unique-random-string) `str(uuid.uuid4())[:8]`
- [Round to 2 decimal places](https://stackoverflow.com/questions/5202233/how-to-change-39-54484700000000-to-39-54-and-using-python)

#### Stretch Goals
- [ ] Add account type attribute (checking/savings)
- [x] Function loops over all accounts and calls `add_interest`
- [x] Create an "application" that prompts for an action (atm.py)
   - [ ] Create account
   - [x] Statement
   - [x] Deposit
   - [x] Withdraw
   - [x] Transfer
- [x] Create `Bank` class to store `BankAccounts` list
  - [x] `create_account()`
  - [x] `deposit()`
  - [x] `withdraw()`
  - [x] `transfer()`
  - [x] `statement()`

<!-- - [ ] Documented code with doc strings
- [x] README includes project title, description, and programming language
- [x] Created attribute for `full_name`
- [x] Created attribute for `balance` (starts at 0)
- [x] Created account number (8 digits, random)
- [x] Deposit function 
  - [x] Updates balance
  - [x] Prints message
- [x] Withdraw function
  - [x] Updates balance
  - [x] Prints message
  - [x] Handles insufficient funds
- [x] Balance function
  - [x] Returns balance
- [x] Interest function
  - [x] Calculates and adds interest correctly
- [x] Print Statement function (name, account number, balance)
  - [x] Account number is masked
  - [x] Balance is formatted as currency 
- [ ] Showed 3 working examples -->
