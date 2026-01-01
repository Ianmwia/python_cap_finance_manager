from tracker import FinanceTracker
from income_expense import Income, Expense
from datetime import datetime
from database import users_collection

#ask for username
username = input("Please input your username: ").strip()

#check if user exists , if not create one
user = users_collection.find_one({"username": username})
if user:
    print(f"welcome back {username}")
else:
    users_collection.insert_one({"username": username})
    print(f"new user {username} created")

#create the object
e = FinanceTracker(username)

choice = input("Do You want to add an INCOME or EXPENSE or check BALANCE, write 'income' for INCOME , 'expense' for Expense or 'balance' for BALANCE or list_all_expenses to LIST ALL EXPENSES: ")

if choice == 'income':
    income_amount = float(input('Enter an Income Amount: '))
    note_input = input('Add a note: ')
    while True:
        date_input = input('Enter a date in the format DD-MM-YYYY: ').strip()
        if not date_input:
            print("Date is required! Please enter a date")
            continue
        try:
            date = datetime.strptime(date_input, "%d-%m-%Y")
            break
        except ValueError:
            print("invalid date format! use DD-MM-YYYY")

    income = Income(amount = income_amount, note = note_input, date = date)
    e.add_income(income)

elif choice == 'expense':
    expense_amount = float(input('Add an expense Amount: '))
    category_input = input('Add an expense category: ')
    note_input = input('Add a note: ')
    while True:
        date_input = input('Enter a date in the format DD-MM-YYYY: ').strip()
        if not date_input:
            print("Date is required! Please enter a date")
            continue
        try:
            date = datetime.strptime(date_input, "%d-%m-%Y")
            break
        except ValueError:
            print("invalid date format! use DD-MM-YYYY")

    expense = Expense(amount = expense_amount, category = category_input, note = note_input, date = date)
    e.add_expense(expense)
elif choice == 'balance':
    """
    read the users balance from mongodb
    """
    balance = e.balance()
    print(f'{username}, Your current balance is: {balance:,.2f}')

elif choice == "list_all_expenses":
    """
    list all expenses indexed
    """
    list_expense = e.list_expenses()
    total_expenses = e.total_expenses()
    if list_expense:
        print(f"{username} You have spent a total of {total_expenses:,} on all your expenses which are: ")
        for idx,expense_list in enumerate(list_expense, start=1):
            print(f"{idx}.{expense_list}")
    else:
        print(f'{username}, You have no expenses')
else:
    print("Invalid input choice , write 'income' for INCOME and 'expense' for Expense")

#balance = e.balance()
#print(f'Your current balance is: {balance}')