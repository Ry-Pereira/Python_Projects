"""
Add expenses (date, amount, category, description)
Save to CSV
View all expenses
Show total spent
Show spending by category (using Pandas)
"""

import pandas

class TrackerBrain:
    def __init__(self,expense_csv_file):
        self.expense_csv_file = expense_csv_file
        self.expense_data_frame = pandas.read_csv(expense_csv_file)

    def add_expense(self,date,amount,category,description):
        new_data = pandas.DataFrame({
            "Date":[date],
            "Amount":[amount],
            "Category":[category],
            "Description":[description]
        })
        new_data.to_csv("expenses.csv",mode="a",header=False,index=False)

    def show_total_spent(self):
        total_amount = self.expense_data_frame['Amount'].to_list()
        total_spend = sum(total_amount)
        return total_spend
    
    def show_expenses(self):
        pass

    def show_expenses_by_category(self):
        pass



    




