import csv
from collections import Counter
import_csv = "election_data_2.csv"

with open(import_csv) as pollData:
    readCSV = csv.reader(pollData, delimiter=",")
    next(readCSV, None)

   #lists
    VoterId = []
    Candidate = []
    
   for column in readCSV:

       VoterId.append(str(column[0]))
        Candidate.append((column[2]))

   totalvotes = len(VoterId)

   #print(totalvotes)
    cnt = Counter(Candidate)
    print(cnt)
    Khan_cnt = cnt['Khan']
    Khan_percent = (Khan_cnt/totalvotes)*float(100)
    Correy_cnt = cnt['Correy']
    Correy_percent = (Correy_cnt/totalvotes)*float(100)
    Li_cnt = cnt['Li']
    Li_percent = (Li_cnt/totalvotes)*float(100)
    OTooley_cnt = cnt["O'Tooley"]
    OTooley_percent = (OTooley_cnt/totalvotes)*float(100)

   print("'''" + "\n" + "Election Results" + "\n" + "--------------------------" + "\n" +
        "Total Votes: " + str(totalvotes) + "\n" + "--------------------------")
    print("Khan: {0:.1f}% ({1})".format(Khan_percent, Khan_cnt))
    print("Correy: {0:.1f}% ({1})".format(Correy_percent, Correy_cnt))
    print("Li: {0:.1f}% ({1})".format(Li_percent, Li_cnt))
    print("O'Tooley: {0:.1f}% ({1})".format(OTooley_percent, OTooley_cnt))

   #candidate_dict = {}
    #candidate_dict.append[cnt[]]
    #print(candidate_dict)
    #maxVal = max(cnt.values())
    Winner = max(zip(cnt.values(), cnt.keys()))
    print(Winner)