class Account:
    """Represent a type of bank account."""
    instance_count = 0
    digits = 7

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1

    def __init__(self, name, type_of_account, initial_balance=0):
        Account.increment_instance_count()
        self.account_number = Account.instance_count
        self.__name__= name
        self.__balance__ = initial_balance
        self.type_of_account = type_of_account


    def __str__(self):
        account_number_string = max(Account.digits - len(str(self.account_number)), 0) * "0" + str(self.account_number)
        return "Type of account: " + self.type_of_account + " account. " + "Account number: " + account_number_string

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.__balance__

    initial_balance = property(get_balance, doc="An account property")

    @property
    def name(self):
        """ The docstring for the account property """
        print('In account method')
        return self.__name__

    @property
    def type_of_account(self):
        """ The docstring for the account property """
        print('In account method')
        return self.type_of_account



    def deposit(self, amount):
        self.__balance__ += amount

    def withdraw(self, amount):
        if amount <= self.__balance__ + self.limit:
            self.__balance__ -= amount
            print("Current balance:" + str(self.__balance__))
        else:
            print("Current balance:" + str(self.__balance__) + " Withdraw: " + str(amount) + ". Withdrawal would exceed your overdraft limit ")

    def __str__(self):
        return 'Account[' + str(self.__name__) + str(self.account_number) + str(self.initial_balance) + str(self.limit) + str(self.risk)

class Current(Account):
    def __init__(self, name, initial_balance=500, overdraft_limit=0):
        super().__init__(name, "Current", initial_balance)
        self.limit = overdraft_limit


class Saving(Account):
    def __init__(self, name):
        super().__init__(name, "Saving")

    def deposit(self, amount):
        print('Deposit is not allowed for Saving accounts!')

    def withdraw(self, amount):
        print('Withdraw is not allowed for Saving accounts!')

class Deposit(Account):
    def __init__(self, name, interest_rate=0):
        super().__init__(name, "Saving")
        self.interest_rate = interest_rate


    def deposit(self, amount):
        print('Deposit is not allowed for Saving accounts!')

    def withdraw(self, amount):
        print('Withdraw is not allowed for Saving accounts!')

class Investment(Account):
    def __init__(self, name, risk = ""):
        super().__init__(name, "Investment")
        self.risk = risk



print(Account.__doc__)

acc1 = Current('John Smith', 1000, 2000)
acc2 = Saving('John Smith')
acc3 = Deposit('John Connor', 0.5)
acc4 = Investment('Phoebe', "high risk")


print('Number of Account instances created:', Account.instance_count)

print(acc1)
print(acc2)
print(acc3)
print(acc4)

acc1.deposit(2000)
print('Current balance: ',acc1.get_balance())
acc1.withdraw(4000)


##
'''''
acc2.deposit(1000)
acc2.withdraw(2000)
print(acc2.get_balance())

acc3.deposit(1000)
acc3.withdraw(2000)
print(acc3.get_balance())
'''''
##


