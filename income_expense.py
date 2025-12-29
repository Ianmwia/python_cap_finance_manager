class Income():
    def __init__(self, amount):
        self.amount = amount
    def to_dict(self):
        return {"amount": self.amount}
    def __str__(self):
        return f'Income for the month is {self.amount}'
    
class Expense():
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category
    def to_dict(self):
        return {"amount": self.amount, "category": self.category}
    def __str__(self):
        return f'You have spent {self.amount} on {self.category}'
