import sys


class Customer:
    bankname = "NileshBank"

    def __int__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Balance after the amount deposit", self.balance)

    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient balance")
            sys.exit(0)
        self.balance = self.balance-amt
        print("balance after the withdraw", self.balance)


print("Welcome to my bank:--",Customer.bankname)

name=input("Enter your name:")
c= Customer()

while True:
    print("d-Deposit\n w-withdraw\n e-Exit")
    option=input("enter a option")
    if option=='d' or option=='D':
        amt=float(input("Enter the amount to be deposited"))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input("Enter the amount to be withdrawed"))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("THANKS FOR BANKING WITH US... LATERS GATERS!!")
        sys.exit()
    else:
        print("Invalid option")
