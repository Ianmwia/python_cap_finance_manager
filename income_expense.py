from datetime import datetime
class Income():
    def __init__(self, amount, note='', date = None):
        self.amount = amount
        self.note = note
        if date is not None:
            self.date = date
        else:
            self.date = datetime.now()
        
    def to_dict(self):
        return {
            "amount": self.amount,
            "date": self.date,
            "note": self.note
            }
    def __str__(self):
        return f'Income for the month is {self.amount}'
    
class Expense():
    def __init__(self, amount, category, note='', date = None):
        self.amount = amount
        self.category = category
        self.note = note
        if date is not None:
            self.date = date
        else:
            self.date = datetime.now()
        
    def to_dict(self):
        return {
            "amount": self.amount, 
            "category": self.category,
            "date": self.date,
            "note": self.note
            }
    def __str__(self):
        return f'You have spent {self.amount} on {self.category}'
