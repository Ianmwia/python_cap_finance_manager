class Income():
    def __init__(self, amount):
        self.amount = amount
    def __str__(self):
        return f'Income for the month is {self.amount}'
    
income = Income(30000)
print(income)

class Expense():
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category
    def __str__(self):
        return f'You have spent {self.amount} on {self.category}'

expense = Expense(3000, "Food")
print(expense)