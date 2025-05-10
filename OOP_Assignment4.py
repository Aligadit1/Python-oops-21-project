""""4. Class Variables and Class Methods
Assignment:
Create a class Bank with a class variable bank_name. 
Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.
"""

class Bank:
    bank_name = "My Bank"
    def __init__(self,user,balance):
        self.user = user
        self.balance = balance
    def user_balance(self):
        print(f"Your balance in the {Bank.bank_name} is {self.balance} ")
    @classmethod
    def change_name(cls,new_name):
        cls.bank_name = new_name        

bank_acc = Bank("Ali",10000)   
bank_acc.user_balance()     
Bank.change_name("Your Bank")
bank_acc.user_balance()