import pandas as pd
from datetime import datetime

def save_to_csv(data):
    save_incomes = pd.DataFrame(data)
    filename = input("save a csv file as: ")
    save_incomes.to_csv(filename)


def create_date(date_input):
    
    while True:
        if not date_input:
            print("Date is required! Please enter a date")
        try:
            return datetime.strptime(date_input, "%d-%m-%Y")
        except ValueError:
                print("invalid date format! use DD-MM-YYYY")
        exit()