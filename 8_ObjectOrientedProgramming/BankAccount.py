class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} owns this Account with current Balance {self.balance} !"

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted!!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw Accepted!!")
        else:
            print("Fund Unavailable!!")


ac1 = Account(owner="Jose", balance=500)
ac1.deposit(200)
print(ac1.balance)

ac1.withdraw(400)
print(ac1.balance)

ac1.withdraw(1000)
print(ac1)
