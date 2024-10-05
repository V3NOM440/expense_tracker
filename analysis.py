class Analysis:
    def __init__(self, expenses):
        self.expenses = expenses

    def total_spent(self):
        return sum(expense['amount'] for expense in self.expenses)

    def spent_per_category(self):
        category_totals = {}
        for expense in self.expenses:
            category = expense['category']
            category_totals[category] = category_totals.get(category, 0) + expense['amount']
        return category_totals
