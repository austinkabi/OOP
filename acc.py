class account:
    def __init__(self):
        self.balance=0
        print("hello,welcome to deposit and withdrawal machine")
        
    def deposit (self):
        print("enter amt to deposit")
        amount=float(input())
        self.balance+=amount
        print("you have succesfully deposited ksh {} ".format(amount))

    def withdrawal(self):
        amount=float(input("Enter amount to withdraw"))
        self.balance-=amount
        print("you have succesfully withdrawn ksh{}".format(amount))


account1=account0
account1.deposit()
account1.withdraw()
print(account1.deposit())
