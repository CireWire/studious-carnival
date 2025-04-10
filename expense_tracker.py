#! /usr/bin/env python3
"""
Expense Tracker - A command-line tool to manage your expenses.

Author: CireWire
Created: 2025-04-10
License: MIT
"""

from database import Database
from tabulate import tabulate
from colorama import init, Fore, Style
import sys

init()  # Initialize colorama

class ExpenseTracker:
    def __init__(self):
        self.db = Database()
        self.categories = [
            "Food", "Transportation", "Housing", "Entertainment",
            "Utilities", "Shopping", "Healthcare", "Education",
            "Other"
        ]

    def display_menu(self):
        print(f"\n{Fore.CYAN}Expense Tracker{Style.RESET_ALL}")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Category Summary")
        print("5. View Total Expenses")
        print("6. Exit")
        return input("Enter your choice (1-6): ")

    def add_expense(self):
        try:
            amount = float(input("Enter amount: "))
            print("\nCategories:")
            for i, category in enumerate(self.categories, 1):
                print(f"{i}. {category}")
            
            while True:
                try:
                    category_choice = int(input("\nSelect category (1-9): "))
                    if 1 <= category_choice <= len(self.categories):
                        category = self.categories[category_choice - 1]
                        break
                    else:
                        print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")

            description = input("Enter description (optional): ")
            self.db.add_expense(amount, category, description)
            print(f"{Fore.GREEN}Expense added successfully!{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Invalid amount. Please enter a valid number.{Style.RESET_ALL}")

    def view_all_expenses(self):
        expenses = self.db.get_all_expenses()
        if not expenses:
            print(f"{Fore.YELLOW}No expenses found.{Style.RESET_ALL}")
            return

        headers = ["ID", "Amount", "Category", "Description", "Date"]
        print(tabulate(expenses, headers=headers, tablefmt="grid"))

    def view_expenses_by_category(self):
        print("\nCategories:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}. {category}")
        
        while True:
            try:
                category_choice = int(input("\nSelect category (1-9): "))
                if 1 <= category_choice <= len(self.categories):
                    category = self.categories[category_choice - 1]
                    break
                else:
                    print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number.{Style.RESET_ALL}")

        expenses = self.db.get_expenses_by_category(category)
        if not expenses:
            print(f"{Fore.YELLOW}No expenses found for category: {category}{Style.RESET_ALL}")
            return

        headers = ["ID", "Amount", "Category", "Description", "Date"]
        print(tabulate(expenses, headers=headers, tablefmt="grid"))

    def view_category_summary(self):
        summary = self.db.get_category_summary()
        if not summary:
            print(f"{Fore.YELLOW}No expenses found.{Style.RESET_ALL}")
            return

        headers = ["Category", "Total Amount"]
        print(tabulate(summary, headers=headers, tablefmt="grid"))

    def view_total_expenses(self):
        total = self.db.get_total_expenses()
        print(f"\n{Fore.GREEN}Total Expenses: ${total:.2f}{Style.RESET_ALL}")

    def run(self):
        while True:
            choice = self.display_menu()
            
            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_all_expenses()
            elif choice == "3":
                self.view_expenses_by_category()
            elif choice == "4":
                self.view_category_summary()
            elif choice == "5":
                self.view_total_expenses()
            elif choice == "6":
                print(f"{Fore.CYAN}Goodbye!{Style.RESET_ALL}")
                self.db.close()
                sys.exit()
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run() 
