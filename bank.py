from dbconnect import banking


class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number

    def deposit(self, amount, account_number):
        banking.deposit(amount, account_number)
        print("your balance is: " + str(banking.check_balance(account_number)))

    def withdraw(self, amount, account_number):
        banking.withdraw(amount, account_number)
        print("your balance is: " + str(banking.check_balance(account_number)))

    def AccountStatement(self, account_number):
        balance = banking.check_balance(account_number)
        print("your bank account balance is: " + str(balance))
        print("your bankaccount is: " + str(account_number))

        