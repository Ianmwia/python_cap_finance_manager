from database import income_collection, expense_collection

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
    def list_incomes(self):
        incomes_list = []
        incomes = income_collection.find({"username": self.__username}).sort("date", 1)
        for my_incomes in incomes:
            amount = my_incomes.get("amount")
            note = my_incomes.get("note")
            date = my_incomes.get("date")
            income_string = f'{amount}, {note}, {date}'
            incomes_list.append(income_string)
        return incomes_list
    
    def list_expenses(self):
        """
        read expenses from mongo db sorted in ascending order
        stored in an instance method
        """
        expenses_list = []
        expenses = expense_collection.find({"username": self.__username}).sort("date", 1)
        for my_expense in expenses:
            category = my_expense.get("category")
            amount = my_expense.get("amount")
            note = my_expense.get("note")
            date = my_expense.get("date")

            expense_string = f"{amount}, {category}, {note}, {date}"
            expenses_list.append(expense_string)
        return expenses_list

    def balance(self):
        return self.total_income() - self.total_expenses()
    
    def update_income(self, index, field, new_value):
        """
        update a specific users income entry bases on field selection
        """
        incomes = list(income_collection.find({"username": self.__username}).sort("date", 1))
        if not incomes:
            return False
        if index <1 or index >len(incomes):
            return False
        if field not in ("amount", "note", "date"):
            return False
        
        selected_income = incomes[int(index) -1]
        update_income = income_collection.update_one(
            {"_id": selected_income["_id"]},
            {"$set": {field: new_value}})
        return update_income
    def update_expense(self, index, field, new_value):
        """
        update a specific users expense entry bases on field selection
        """
        expenses = list(expense_collection.find({"username": self.__username}).sort("date", 1))
        if not expenses:
            return False
        if index <1 or index >len(expenses):
            return False
        if field not in ("amount", "category", "note", "date"):
            return False
        
        selected_income = expenses[int(index) -1]
        update_expense = expense_collection.update_one(
            {"_id": selected_income["_id"]},
            {"$set": {field: new_value}})
        return update_expense
    
    def delete_expense(self, index):
        """
        delete a specific users expense from the database
        """
        expenses = list(expense_collection.find({"username": self.__username}).sort("date", 1))
        if not expenses:
            return False
        if index <1 or index >len(expenses):
            return False
        
        selected_income = expenses[int(index) -1]
        delete_expense = expense_collection.delete_one(
            {"_id": selected_income["_id"]})
        return delete_expense

    def __str__(self):
        return f'Total Income {self.total_income()}, Total Expenses : {self.total_expenses()} and Balance is Ksh: {self.balance(): ,} '

#e = FinanceTracker()

# e.add_income(income)
# e.add_expense(expense1)
# e.add_expense(expense2)
# bal = e.balance()
# #print(bal)
# print(e)