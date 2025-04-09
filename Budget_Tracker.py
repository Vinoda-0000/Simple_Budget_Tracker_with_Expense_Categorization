import numpy as np
import pandas as pd

class BudgetTracker:
    def __init__(self, budget):
        self.budget = budget
        self.remaining = budget
        self.expenses = pd.DataFrame(columns=['Name', 'Amount', 'Category'])
    
    def add_expense(self, name, amount, category):
        if amount > self.remaining:
            print("Insufficient budget!")
            return
        new_expense = pd.DataFrame([[name, amount, category]], columns=['Name', 'Amount', 'Category'])
        self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
        self.remaining -= amount
        print(f"Added expense: {name} - ${amount} ({category})")
    
    def show_expenses(self):
        if self.expenses.empty:
            print("No expenses recorded.")
            return
        print("\nExpenses:")
        print(self.expenses)

    def get_remaining_budget(self):
        return self.remaining
    
    def get_expense_summary(self):
        if self.expenses.empty:
            return {}
        summary = self.expenses.groupby('Category')['Amount'].sum().to_dict()
        return summary
    
    def save_to_csv(self, filename="expenses.csv"):
        self.expenses.to_csv(filename, index=False)
        print(f"Expenses saved to {filename}")

# Example usage
budget = float(input("Enter your budget: "))
tracker = BudgetTracker(budget)

while True:
    print("\nOptions: 1-Add Expense, 2-Show Expenses, 3-Remaining Budget, 4-Expense Summary, 5-Save to CSV, 6-Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        name = input("Expense Name: ")
        amount = float(input("Amount: "))
        category = input("Category: ")
        tracker.add_expense(name, amount, category)
    elif choice == '2':
        tracker.show_expenses()
    elif choice == '3':
        print(f"Remaining Budget: ${tracker.get_remaining_budget()}")
    elif choice == '4':
        summary = tracker.get_expense_summary()
        print("\nExpense Summary:")
        for category, total in summary.items():
            print(f"{category}: ${total}")
    elif choice == '5':
        tracker.save_to_csv()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid option, try again.")
