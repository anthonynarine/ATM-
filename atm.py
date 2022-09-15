import sys

class Person:
    def __init__(self, first_name, last_name ):
        self.firstname = first_name
        self.last_name = last_name
        

class Customer(Person):
    def __init__(self, first_name, last_name, account_number, account_balance = 0):
        super().__init__(first_name, last_name) #no inhereted from Person
        self.account_number = account_number
        self.account_balance = account_balance

    def __str__(self) :
        return f"Customer: {self.firstname} {self.last_name}\nAccount Balance: {self.account_number}: ${self.account_balance}"

    def deposit(self, amount_deposit):
        self.account_balance += amount_deposit
        print("Deposit completed")
    
    def withdraw(self, amount_withdraw):
        if self.account_balance >= amount_withdraw:
            self.account_balance -= amount_withdraw
            print("Withdrawal complete")
        else:
            print ("Insufficent funds")
       

def create_customer():
    first_name_ct = input("Enter your name: ")
    last_name_ct = input("Enter your last name: ")
    account_number = input("Enter your account number: ")
    customer1 = Customer (first_name_ct, last_name_ct, account_number)
    return customer1

def start():
    my_customer = create_customer()
    print(my_customer)
    option = 0


    while option != "E":
        print("Choose: Deposit (D), Withdraw (W), or Exit (E)")
        option = input()
        if option == "D":
            deposit_amount = int(input("Deposit amoutnt: "))
            my_customer.deposit(deposit_amount)
        elif option == "W":
            withdrawal_amount = int(input("Withdrawal amount: "))
            my_customer.withdraw(withdrawal_amount)
        print (my_customer)

    print("Thank you for using Julia's Bank")

start()








"""create program for code to run aasking the user to choose wheather they want to make a deposit or withdrawal.
creat 2 functions:

 1. that is in charge of chreating the client, asking the user for all the necessary infromation 
and returning throught a "return" a client object already 

2. function that can be called START or something
like that """

#code to choose to:Deposit, Withdraw or Exit
    #function:create_customer()








