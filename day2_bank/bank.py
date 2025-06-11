class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            return self.balance
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance = self.balance - amount
            elif self.balance < amount:
                print("Insufficient funds")

    def display_balance(self):
        print(f"Current balance: {self.balance:.2f}")

account = BankAccount("Aidan")
account.deposit(100)
account.withdraw(30)
account.display_balance() 