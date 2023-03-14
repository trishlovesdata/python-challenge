#Importing modules
import os
import csv

#Reading csv file
budget_csv = os.path.join("..","Resources","budget_data.csv")
csvpath = 'Desktop\python-challenge\PyBank\Resources\budget_data.csv'

#Opening csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(f"CSV Header: {header}")