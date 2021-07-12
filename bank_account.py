class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Your available balance is " +str(self.balance))
    def withdrawal(self,amount):
        if(amount>self.balance):
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
            print("Your available balance is " +str(self.balance))

   
b=BankAccount("Sai Manish",2000)
print(b)
print(b.owner)
print(b.balance)
b.withdrawal(1500)
b.deposit(1000)
b.withdrawal(4000)
b.deposit(2000)
b.withdrawal(1000)
