Expense Tracker
  Overview
    This is a command-line-based Expense Tracker application written in Python. The application allows users to add and manage expenses, create custom categories, and perform expense analysis, such as calculating total expenses and categorizing spending.

Features
  Add Expenses: Users can log expenses with an amount, category, and description.
  Manage Categories: Users can add their own custom categories to classify expenses.
  View Expenses: Users can view all recorded expenses along with the details.
  Expense Analysis: The app provides a summary of total spending and spending per category.
  Persistent Storage: Expenses are saved to a file (expenses.json), so data is retained across sessions.

Project Structure 
   expense_tracker/
│
├── main.py               # Main file to run the application
├── tracker.py            # Logic for tracking expenses
├── categories.py         # Logic for managing categories
├── analysis.py           # Logic for analyzing expenses
├── README.md             # Project documentation
└── data/
    └── expenses.json     # File to store expenses data (persistent storage)

Requirements
    Python 3.x

Installation and Setup
  1  Clone the repository or download the project files:
        git clone <repository-url>
        cd expense_tracker
        
  2  Create a virtual environment
        python -m venv venv

  3  Activate the virtual environment:
      On Windows :
          venv\Scripts\activate
      On MacOS/Linus :
          source venv/bin/activate

Usage
  
  1  Run the application:
        python main.py

  2  Menu Options:

  Add Expense: Enter the expense amount, category, and description.
  View Expenses: View all recorded expenses.
  Add Category: Add a new expense category.
  Analyze Expenses: View total spent and amount spent per category.
  Exit: Exit the application.

Future Enhancements
  Implement a Graphical User Interface (GUI) using Tkinter or a web-based interface using Flask.
  Use SQLite or a more robust database for storing expenses.
  Add more analysis features like monthly trends, expense limits, and notifications.
