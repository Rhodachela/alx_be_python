class BankAccount:
    def __init__(self, initial_balance = 0):
        self.current_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.current_balance:
            print("Insufficient funds in your account")
        elif amount > 0:
            self.current_balance -= amount
            return True
        else:
            print("Withdraw amount must be positive")
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.current_balance:.2f}")
    