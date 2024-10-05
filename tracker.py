import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename='data/expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_expenses(self):
        with open(self.filename, 'w') as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self, amount, category, description):
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': str(datetime.now())
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        return self.expenses