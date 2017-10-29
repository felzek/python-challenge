import os
import csv
from collections import Counter

filepath = os.path.join("raw_data","election_data_2.csv")



voter_ID = []
county = []
canadiate = []

with open(filepath,newline="") as csvpoll:

    csvreader = csv.reader(csvpoll,delimiter=",")

    next(csvreader,None)
    
    for row in csvreader:

        voter_ID.append(row[0])

        canadiate.append(row[2])

    canadiate_dict = Counter(canadiate)

for x in canadiate_dict:

    print(canadiate_dict)

print("Election Results")


print("\n")


