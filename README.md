# Simple legant Expense Tracker

A simple command-line application for managing personal expenses. This tracker allows users to add, update, delete, view, and summarize their expenses. Users can also categorise expenses, set monthly budgets, and export their expenses to a CSV file.

## Features

- **Add Expenses:** Easily add expenses with descriptions, amounts, categories, and dates.
- **Update Expenses:** Modify existing expenses by ID, updating their description, amount, or both.
- **Delete Expenses:** Remove expenses from the tracker using their unique ID.
- **List Expenses:** View all expenses in a clean table format, sorted by date.
- **Summarize Expenses:** Get a summary of total expenses for a specific month or for all time.
- **Categorize Expenses:** Filter expenses by category (e.g., Food, Transportation, etc.).
- **Set Monthly Budgets:** Define a budget for a specific month and track whether you stay within the limit.
- **Check Budgets:** View how your expenses compare to the budget set for a specific month.
- **Export to CSV:** Save all your expenses in a CSV file for easy viewing and sharing.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/pakagronglb/simple-expense-tracker.git
    cd simple-expense-tracker
    ```

2. **Install dependencies:**

    There are no external dependencies for this command-line application, but ensure you are running Python 3.x.

## Usage

1. **Add an expense:**

    ```bash
    python expense_tracker.py add --description "Groceries" --amount 50.75 --category "Food"
    ```

2. **List all expenses:**

    ```bash
    python expense_tracker.py list
    ```

3. **Update an expense:**

    ```bash
    python expense_tracker.py update --id 1 --description "Groceries at Walmart" --amount 60.00
    ```

4. **Delete an expense:**

    ```bash
    python expense_tracker.py delete --id 1
    ```

5. **View summary for a specific month:**

    ```bash
    python expense_tracker.py summary --month 9
    ```

6. **List expenses by category:**

    ```bash
    python expense_tracker.py list-by-category --category "Food"
    ```

7. **Set a budget for a month:**

    ```bash
    python expense_tracker.py set-budget --month 10 --amount 500.00
    ```

8. **Check if expenses exceed the budget for a month:**

    ```bash
    python expense_tracker.py check-budget --month 10
    ```

9. **Export all expenses to CSV:**

    ```bash
    python expense_tracker.py export --file expenses.csv
    ```

## Data Storage

- **Expenses** are stored in `expenses.json` in the root directory of the project.
- **Budgets** are stored in `budgets.json`, ensuring budgets are tracked by month.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Example Output

Here’s an example of what the **List Expenses** command would output:

```
ID    Date         Description          Amount      Category
------------------------------------------------------------
1     2024-10-10   Groceries            $50.75      Food
2     2024-10-11   Bus fare             $2.50       Transportation
3     2024-10-12   Coffee               $3.00       Food
```

## Roadmap

- [x] Basic expense tracking (add, update, delete)
- [x] Summarize expenses by month
- [x] Categorize expenses
- [x] Set and check monthly budgets
- [ ] Add support for recurring expenses
- [ ] Integrate with Google Sheets for expense tracking

---

### Get Started Today!

Manage your finances efficiently with this simple yet powerful expense tracker. Clone the repo and start tracking your expenses today!

---
## Credits
https://roadmap.sh/projects/expense-tracker
- Roadmap for this project was taken from this website -- roadmap.sh
- With multiple exercises and projects to follow along, this website is a great resource for anyone looking to learn how to code.