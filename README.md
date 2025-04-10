# Expense Tracker

A simple command-line expense tracker application built with Python.

## Features

- Add expenses with categories and descriptions
- View all expenses
- View expenses by category
- View category-wise summary
- View total expenses
- Colorful command-line interface
- SQLite database for persistent storage

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python expense_tracker.py
   ```

2. Follow the menu prompts to:
   - Add new expenses
   - View your expense history
   - Get category-wise summaries
   - View total expenses

## Categories

The application includes the following expense categories:
- Food
- Transportation
- Housing
- Entertainment
- Utilities
- Shopping
- Healthcare
- Education
- Other

## Database

The application uses SQLite to store your expenses in a file named `expenses.db`. This file will be automatically created when you run the application for the first time. 
