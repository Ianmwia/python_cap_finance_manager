from income_expense import Income, Expense
from database import income_collection, expense_collection
from datetime import datetime

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

choice = input("Do You want to add an INCOME or EXPENSE, write 'income' for INCOME and 'expense' for Expense: ")

if choice == 'income':
    income_amount = input('Enter an Income Amount: ')
    note_input = input('Add a note: ')
    date_input = input('Enter a date in the format DD-MM-YYYY: ')

    if date_input:
        date = datetime.strptime(date_input, "%d-%m-%Y")
    else:
        date = None

    income = Income(amount = income_amount, note = note_input, date = date_input)
    e.add_income(income)

# e.add_income(income)
# e.add_expense(expense1)
# e.add_expense(expense2)
# bal = e.balance()
# #print(bal)
# print(e)
elif choice == 'expense':
    expense_amount = input('Add an expense Amount: ')
    category_input = input('Add an expense category: ')
    note_input = input('Add a note: ')
    date_input = input('Enter a date in the format DD-MM-YYYY: ')


    if date_input:
        date = datetime.strptime(date_input, "%d-%m-%Y")
    else:
        date = None

    expense = Expense(amount = expense_amount, category = category_input, note = note_input, date = date_input)
    e.add_expense(expense)
else:
    print("Invalid input choice , write 'income' for INCOME and 'expense' for Expense")