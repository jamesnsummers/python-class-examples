""" this is my bank file """
class BankAccount():
    """ this is the BankAccount class """
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0

    def deposit(self, amount):
        """ this is the deposit function """
        self.balance += amount

    def withdraw(self, amount):
        """ this is the withdraw function """
        self.balance -= amount
        if self.balance < 0:
            self.overdraft_fees += 20
        return amount

SAVINGS = BankAccount("SAVINGS")
CHECKING = BankAccount("CHECKING")

print("My new {} account has ${}.".format(SAVINGS.kind, SAVINGS.balance))
print("My new {} account has ${}.".format(CHECKING.kind, CHECKING.balance))
print()

WAGES = 800
SAVINGS.deposit(WAGES)


CASH = SAVINGS.withdraw(150)
CHECKING.deposit(CASH)

print("I deposited ${} into my {} account.".format(WAGES, SAVINGS.kind))
print("I transferred ${} from {} to {}.".format(CASH, SAVINGS.kind, CHECKING.kind))
print()

print("My {} account now has ${}.".format(SAVINGS.kind, SAVINGS.balance))
print("My {} account now has ${}.".format(CHECKING.kind, CHECKING.balance))
