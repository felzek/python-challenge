# -*- coding: UTF-8 -*-
"""PyBank Homework."""

# Dependencies
import csv

# Files to load and output (Remember to change these)
file_to_load = "raw_data/budget_data_1.csv"
file_to_output = "analysis/budget_analysis_1.txt"

month = 0
revenue = 0
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)
    
    for row in reader:
        month = month +1 
        
        print(row[1])

        

    #print(f""(sum(int(row["Revenue"])))