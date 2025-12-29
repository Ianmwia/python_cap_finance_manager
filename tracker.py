from income_expense import Income, Expense
from database import income_collection, expense_collection

class FinanceTracker():
    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_income(self, income):
        self.incomes.append(income)
        income_collection.insert_one(income.to_dict())
    def add_expense(self, expense):
        self.expenses.append(expense)
        expense_collection.insert_one(expense.to_dict())

    def total_income(self):
        total_income = 0 
        for i in self.incomes:
            total_income += i.amount
        return total_income
    def total_expenses(self):
        total_expenses = 0 
        for i in self.expenses:
            total_expenses += i.amount
        return total_expenses

    def balance(self):
        return self.total_income() - self.total_expenses()
    def __str__(self):
        return f'Total Income {self.total_income()}, Total Expenses : {self.total_expenses()} and Balance is Ksh: {self.balance(): ,} '

e = FinanceTracker()

income = Income(30000)
expense1 = Expense(3000, "Food")
expense2 = Expense(3000, "Electricity")

e.add_income(income)
e.add_expense(expense1)
e.add_expense(expense2)
bal = e.balance()
#print(bal)
print(e)