# -*- coding: UTF-8 -*-
"""
pyBank is a program that enables you to pinpoint any Bank Data's Total revenue, Greatest Increase in Revenue,
Average revenue Change, Greatest Decrease in Revenue with one simple run

"""

import os
import csv

csvpath = os.path.join("raw_data","budget_data_1.csv")
output_path = os.path.join("raw_data","Analysis.csv")

total_months = 0

total = 0


revenue = []
date=[]
revenue_2 = []
revenue_change = []
with open(csvpath,newline="") as csvfile: 

    csvreader = csv.reader(csvfile,delimiter=",")

    next(csvreader, None)

    total_revenue = 0


    



    for row in csvreader:
        
        

        date.append(row[0])

       


        revenue.append(int(row[1]))

month=len(date)
       

for x in range(2,len(date)):
    
    revenue_change.append(int(revenue[x])-int(revenue[x-1]))

avg_revenue_change = revenue_change/month=len(date)


print(revenue_change)

print ("Financial Analysis")

print ("----------------------------")

print ("Total Months: " + str(len(date)))

print ("Total Revenue: $" + str(sum(revenue)))