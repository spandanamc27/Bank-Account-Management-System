from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self, name, initialDeposit):
        pass

    @abstractmethod
    def authenticate(self, name, accountNumber):
        pass

    @abstractmethod
    def withdraw(self, withdrawalAmount):
        pass

    @abstractmethod
    def deposit(self, depositAmount):
        pass

    @abstractmethod
    def displayBalance(self):
        pass


class SavingsAccount(Account):
    def __init__(self):
        # Dictionary to hold account info: [accountNumber] = [name, balance]
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        print()
        self.accountNumber = randint(10000, 99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("Account creation has been successful. Your account number is", self.accountNumber)
        print()

    def authenticate(self, name, accountNumber):
        print()
        if accountNumber in self.savingsAccounts:
            if self.savingsAccounts[accountNumber][0] == name:
                print("Authentication Successful")
                self.accountNumber = accountNumber
                print()
                return True
            else:
                print("Authentication Failed: Name mismatch")
        else:
            print("Authentication Failed: Invalid account number")
        print()
        return False

    def withdraw(self, withdrawalAmount):
        print()
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal was successful.")
            self.displayBalance()
        print()

    def deposit(self, depositAmount):
        print()
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Deposit was successful.")
        self.displayBalance()
        print()

    def displayBalance(self):
        print("Available balance:", self.savingsAccounts[self.accountNumber][1])


# Driver Code
savingsAccount = SavingsAccount()

while True:
    print()
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    userChoice = int(input("Your choice: "))
    print()

    if userChoice == 1:
        print("Enter your name: ")
        name = input()
        print("Enter the initial deposit: ")
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)

    elif userChoice == 2:
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authenticated = savingsAccount.authenticate(name, accountNumber)

        if authenticated:
            while True:
                print()
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to the previous menu")
                userChoice = int(input("Your choice: "))

                if userChoice == 1:
                    print("Enter a withdrawal amount:")
                    amount = int(input())
                    savingsAccount.withdraw(amount)

                elif userChoice == 2:
                    print("Enter an amount to deposit:")
                    amount = int(input())
                    savingsAccount.deposit(amount)

                elif userChoice == 3:
                    savingsAccount.displayBalance()

                elif userChoice == 4:
                    break
                else:
                    print("Invalid input, try again.")

    elif userChoice == 3:
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid input, please choose between 1-3.")
