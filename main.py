from tracker import ExpenseTracker
from categories import Categories
from analysis import Analysis

def main():
    expense_tracker = ExpenseTracker()
    categories = Categories()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Add Category")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            print("Available categories: ", categories.get_categories())
            category = input("Enter category: ")
            if category not in categories.get_categories():
                print("Category not found. Please add it first.")
            else:
                description = input("Enter description: ")
                expense_tracker.add_expense(amount, category, description)
                print("Expense added successfully!")

        elif choice == '2':
            expenses = expense_tracker.view_expenses()
            if expenses:
                for exp in expenses:
                    print(f"Amount: {exp['amount']}, Category: {exp['category']}, Description: {exp['description']}, Date: {exp['date']}")
            else:
                print("No expenses found.")

        elif choice == '3':
            category = input("Enter category to add: ")
            categories.add_category(category)
            print(f"Category '{category}' added successfully!")

        elif choice == '4':
            analysis = Analysis(expense_tracker.view_expenses())
            print("\nTotal Spent: ", analysis.total_spent())
            print("Spent Per Category: ", analysis.spent_per_category())

        elif choice == '5':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
