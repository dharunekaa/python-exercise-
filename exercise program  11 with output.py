import os

EXPENSE_FILE = "expenses.txt"  # File to store expenses

# Function to add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, etc.): ")
    amount = input("Enter amount: ")
   
    with open(EXPENSE_FILE, "a") as file:  # Append mode
        file.write(f"{date}, {category}, {amount}\n")
    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    if os.path.exists(EXPENSE_FILE):  # Check if file exists
        with open(EXPENSE_FILE, "r") as file:
            expenses = file.readlines()
        if expenses:
            print("\nYour Expenses:")
            for idx, expense in enumerate(expenses, start=1):
                print(f"{idx}. {expense.strip()}")
        else:
            print("No expenses found.")
    else:
        print("No expenses found.")

# Function to delete all expenses
def delete_expenses():
    if os.path.exists(EXPENSE_FILE):
        os.remove(EXPENSE_FILE)  # Delete file
        print("All expenses deleted successfully!")
    else:
        print("No expenses to delete.")

# Main menu loop
while True:
    print("\nExpense Tracker Application")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete All Expenses")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expenses()
    elif choice == "4":
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")




output:

    Expense Tracker Application
1. Add Expense
2. View Expenses
3. Delete All Expenses
4. Exit
Enter choice: 50000
Invalid choice. Try again.

Expense Tracker Application
1. Add Expense
2. View Expenses
3. Delete All Expenses
4. Exit
Enter choice: 1
Enter date (YYYY-MM-DD): 2025-02-28
Enter category (Food, Transport, etc.): food
Enter amount: 5000
Expense added successfully!

Expense Tracker Application
1. Add Expense
2. View Expenses
3. Delete All Expenses
4. Exit
Enter choice: 2

Your Expenses:
1. 2025-02-28, food, 5000

Expense Tracker Application
1. Add Expense
2. View Expenses
3. Delete All Expenses
4. Exit
Enter choice: 3
All expenses deleted successfully!

Expense Tracker Application
1. Add Expense
2. View Expenses
3. Delete All Expenses
4. Exit
Enter choice: 4
Exiting. Goodbye!
