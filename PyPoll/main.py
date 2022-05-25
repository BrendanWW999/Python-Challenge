#Importing the file
from inspect import BoundArguments
import os
import csv

#sets path info
csvpath = os.path.join('Python-Challenge', 'PyPoll', 'Resources', 'election_data.csv')


#opens and reads CSV file
with open(csvpath) as csvfile:
    election = csv.reader(csvfile)
    next(election)

    total_vote = 0
    Khan_vote = 0
    Correy_vote = 0
    Li_vote = 0
    Otooley_vote = 0
    Khan_perc = 0
    Correy_perc = 0
    Li_perc = 0
    Otooley_perc = 0
   
    for row in election:         
        total_vote = total_vote + 1
        if row[2] == 'Khan':
            Khan_vote += 1
        if row[2] == 'Correy':
            Correy_vote += 1
        if row[2] == 'Li':
            Li_vote += 1
        if row[2] == 'O\'Tooley':
            Otooley_vote += 1 
        
    Khan_perc = (Khan_vote/total_vote) * 100
    Correy_perc = (Correy_vote/total_vote) * 100
    Li_perc = (Li_vote/total_vote) * 100
    Otooley_perc = (Otooley_vote/total_vote) * 100 

print("Total Votes ", str(total_vote))
print("Khan: ", str(Khan_perc) + " " + str(Khan_vote))
print("Correy: ", str(Correy_perc) + " " + str(Correy_vote))
print("Li: ", str(Li_perc) + " " + str(Li_vote))
print("O'Tooley: ", str(Otooley_perc) + " " + str(Otooley_vote))