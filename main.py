from tracker import FinanceTracker
from income_expense import Income, Expense
from datetime import datetime
from database import users_collection

#ask for username
username = input("Please input your username: ")

#check if user exists , if not create one
user = users_collection.find_one({"username": username})
if user:
    print(f"welcome back {username}")
else:
    users_collection.insert_one({"username": username})
    print(f"new user {username} created")

#create the object
e = FinanceTracker(username)

choice = input("Do You want to add an INCOME or EXPENSE, write 'income' for INCOME and 'expense' for Expense: ")

if choice == 'income':
    income_amount = float(input('Enter an Income Amount: '))
    note_input = input('Add a note: ')
    date_input = input('Enter a date in the format DD-MM-YYYY: ')

    if date_input:
        date = datetime.strptime(date_input, "%d-%m-%Y")
    else:
        date = None

    income = Income(amount = income_amount, note = note_input, date = date_input)
    e.add_income(income)

elif choice == 'expense':
    expense_amount = float(input('Add an expense Amount: '))
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

balance = e.balance()
print(f'Your current balance is: {balance}')