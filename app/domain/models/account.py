class Account:
    def __init__(self, id:str, balance:int = 0):
        self.id = id
        self.balance = balance

    def deposit(self, amount:int) -> None:
        self.balance += amount

    def withdraw(self, amount:int) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False 