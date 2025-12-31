from income_expense import Income, Expense
from database import income_collection, expense_collection
from datetime import datetime

class FinanceTracker():
    def __init__(self, username):
        self.__username = username
        self.incomes = []
        self.expenses = []

    def get_username(self):
        """create the getter for the username """
        return self.__username

    def add_income(self, income):
        self.incomes.append(income)
        data = income.to_dict()
        data["username"] = self.__username
        income_collection.insert_one(data)

    def add_expense(self, expense):
        self.expenses.append(expense)
        data = expense.to_dict()
        data["username"] = self.__username
        expense_collection.insert_one(data)

    def total_income(self):
        total_income = 0 
        for i in income_collection.find({"username": self.__username}):
            total_income += float(i["amount"])
        return total_income
    def total_expenses(self):
        total_expenses = 0 
        for i in expense_collection.find({"username": self.__username}):
            total_expenses += float(i["amount"])
        return total_expenses

    def balance(self):
        return self.total_income() - self.total_expenses()
    def __str__(self):
        return f'Total Income {self.total_income()}, Total Expenses : {self.total_expenses()} and Balance is Ksh: {self.balance(): ,} '

#e = FinanceTracker()

# e.add_income(income)
# e.add_expense(expense1)
# e.add_expense(expense2)
# bal = e.balance()
# #print(bal)
# print(e)