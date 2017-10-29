# -*- coding: UTF-8 -*-
"""PyBank Homework."""
# Dependencies
import csv
import os

data_path = os.path.join("Resources")


def loadfiles():
	files = []
	for file in os.listdir(data_path):
		if file.endswith(".csv"):
			files.append(os.path.join(data_path, file))
	return files
# Files to load and output (Remember to change these)

file_to_output = "analysis/budget_analysis_1.txt"
# Read the csv and convert it into a list of dictionaries
hello = []
revenue_change=[] 
with open(files) as revenue_data:
    reader = files.DictReader(revenue_data)
    for row in reader:
        hello.append(int(row["Revenue"]))
    for x in range(1,len(hello)):
        revenue_change.append(int(hello[x]-hello[x-1]))
    average_change = sum(revenue_change) / (len(hello)-1)
    print(len(hello))
    print(sum(hello))
    print(average_change)

   

    for x in reader:

        if max(revenue_change) == reader[x]:
            
            


    print(max(revenue_change))
    print(min(revenue_change))
