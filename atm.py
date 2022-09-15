class Person:
    def __init__(self, first_name, last_name ):
        self.firstname = first_name
        self.last_name = last_name
        

class Customer(Person):
    def __init__(self, first_name, last_name, account_number, account_balance):
        super().__init__(account_number, account_balance)
        self.account_number = account_number
        self.account_balance = account_balance

    def __str__(self) :
        return f"Customer Account Number: {self.account_number}\nCustomer Account Balance: ${self.account_balance}"

    def deposit(self, deposit):
        deposit = int(input("How much will you be depositing today: "))
        self.deposit = deposit
    
    def withdraw(self, withdraw):
        withdraw = int(input("How much will you taking out today: "))
        withdraw -= self.account_balance 
        return f" Your new balance is: {self.account_balance}"

"""create program for code to run aasking the user to choose wheather they want to make a deposit or withdrawal.
creat 2 functions, 1 that is in charge of chreating the client, asking the user for all the necessary infromation 
and returning throught a "return" a client object already and anoter function taht ban be called START or something
like that """

#code to choose to:Deposit, Withdraw or Exit
    #function:create_customer()




c1 = Customer("Julia", "Narine", 123456, 1500)
print(c1)
