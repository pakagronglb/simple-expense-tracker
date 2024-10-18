import argparse
import json
import csv
from datetime import datetime

# File paths
DATA_FILE = 'expenses.json'
BUDGET_FILE = 'budgets.json'

# Load existing expenses
def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Load the budgets from the JSON file
def load_budgets():
    try:
        with open(BUDGET_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save budgets to the JSON file
def save_budgets(budgets):
    with open(BUDGET_FILE, 'w') as file:
        json.dump(budgets, file, indent=4)

# Add an expense
def add_expense(description, amount, category="Other"):
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    date = datetime.now().strftime('%Y-%m-%d')
    new_expense = {
        "id": expense_id,
        "date": date,
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense_id})")

# List all expenses
def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print(f"{'ID':<5}{'Date':<12}{'Description':<20}{'Amount':<10}{'Category':<10}")
    for expense in expenses:
        print(f"{expense['id']:<5}{expense['date']:<12}{expense['description']:<20}${expense['amount']:<10.2f}{expense['category']:<10}")

# Update an expense
def update_expense(expense_id, new_description=None, new_amount=None):
    expenses = load_expenses()
    expense = next((exp for exp in expenses if exp['id'] == expense_id), None)

    if not expense:
        print(f"Expense with ID {expense_id} not found.")
        return

    if new_description:
        expense['description'] = new_description
    if new_amount is not None:
        expense['amount'] = new_amount
    
    save_expenses(expenses)
    print(f"Expense ID {expense_id} updated successfully")

# Delete an expense
def delete_expense(expense_id):
    expenses = load_expenses()
    expenses = [exp for exp in expenses if exp['id'] != expense_id]
    save_expenses(expenses)
    print(f"Expense ID {expense_id} deleted successfully.")

# Summarize expenses
def summarize_expenses(month=None):
    expenses = load_expenses()
    total = 0

    if month:
        expenses = [exp for exp in expenses if datetime.strptime(exp['date'], '%Y-%m-%d').month == month]

    for expense in expenses:
        total += expense['amount']

    if month:
        print(f"Total expenses for month {month}: ${total:.2f}")
    else:
        print(f"Total expenses: ${total:.2f}")

# List expenses by category
def list_by_category(category):
    expenses = load_expenses()
    filtered_expenses = [exp for exp in expenses if exp['category'].lower() == category.lower()]

    if not filtered_expenses:
        print(f"No expenses found for category '{category}'.")
        return

    print(f"{'ID':<5}{'Date':<12}{'Description':<20}{'Amount':<10}{'Category':<10}")
    for expense in filtered_expenses:
        print(f"{expense['id']:<5}{expense['date']:<12}{expense['description']:<20}${expense['amount']:<10.2f}{expense['category']:<10}")

# Set a budget for a specific month
def set_budget(month, amount):
    budgets = load_budgets()
    budgets[str(month)] = amount
    save_budgets(budgets)
    print(f"Budget for month {month} set to ${amount}")

# Check if the user exceeds the budget
def check_budget(month):
    expenses = load_expenses()
    budgets = load_budgets()
    total = sum(exp['amount'] for exp in expenses if datetime.strptime(exp['date'], '%Y-%m-%d').month == month)
    
    if str(month) in budgets:
        budget = budgets[str(month)]
        print(f"Total expenses for month {month}: ${total:.2f}")
        print(f"Budget for month {month}: ${budget:.2f}")
        
        if total > budget:
            print(f"Warning: You have exceeded the budget for month {month} by ${total - budget:.2f}!")
        else:
            print(f"You are within the budget for month {month}.")
    else:
        print(f"No budget set for month {month}.")

# Export expenses to CSV
def export_to_csv(filename):
    expenses = load_expenses()

    if not expenses:
        print("No expenses to export.")
        return

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'date', 'description', 'amount', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

    print(f"Expenses exported successfully to {filename}.")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Command: add
    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("--description", required=True, help="Description of the expense")
    add_parser.add_argument("--amount", required=True, type=float, help="Amount of the expense")
    add_parser.add_argument("--category", help="Category of the expense (default: Other)", default="Other")

    # Command: list
    list_parser = subparsers.add_parser("list", help="List all expenses")

    # Command: update
    update_parser = subparsers.add_parser("update", help="Update an expense")
    update_parser.add_argument("--id", required=True, type=int, help="ID of the expense")
    update_parser.add_argument("--description", help="New description for the expense")
    update_parser.add_argument("--amount", type=float, help="New amount for the expense")

    # Command: delete
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument("--id", required=True, type=int, help="ID of the expense")

    # Command: summary
    summary_parser = subparsers.add_parser("summary", help="View summary of expenses")
    summary_parser.add_argument("--month", type=int, help="Summary for a specific month")

    # Command: list-by-category
    category_parser = subparsers.add_parser("list-by-category", help="List expenses by category")
    category_parser.add_argument("--category", required=True, help="Category to filter expenses")

    # Command: set-budget
    budget_parser = subparsers.add_parser("set-budget", help="Set a budget for a specific month")
    budget_parser.add_argument("--month", required=True, type=int, help="Month (1-12)")
    budget_parser.add_argument("--amount", required=True, type=float, help="Budget amount")

    # Command: check-budget
    check_budget_parser = subparsers.add_parser("check-budget", help="Check if expenses exceed the budget for a month")
    check_budget_parser.add_argument("--month", required=True, type=int, help="Month to check")

    # Command: export
    export_parser = subparsers.add_parser("export", help="Export expenses to a CSV file")
    export_parser.add_argument("--file", required=True, help="Filename for the exported CSV")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount, args.category)
    elif args.command == "list":
        list_expenses()
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "summary":
        summarize_expenses(args.month)
    elif args.command == "list-by-category":
        list_by_category(args.category)
    elif args.command == "set-budget":
        set_budget(args.month, args.amount)
    elif args.command == "check-budget":
        check_budget(args.month)
    elif args.command == "export":
        export_to_csv(args.file)

if __name__ == "__main__":
    main()
