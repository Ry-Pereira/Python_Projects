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



    def run():


data = pandas.read_csv("expenses.csv")
print(data)


new_data = pandas.DataFrame({
    "Date":[1121],
    "Amount":[1212],
    "Category":['Hello'],
    "Description":["jew"]

})

data_dict = data.to_dict()
print(data_dict)

date_list = data['Date'].to_list()
print("List")
print(date_list)

print("\nAppend")

new_data.to_csv("expenses.csv",mode="a",header=False,index=False)


data = pandas.read_csv("expenses.csv")
print(data)