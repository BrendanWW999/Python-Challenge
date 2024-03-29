import os
import csv
import decimal

csvpath = os.path.join('Python-Challenge', 'PyPoll', 'Resources', 'election_data.csv')      # sets path info

with open(csvpath) as csvfile:                                                              # opens and reads CSV file
    election = csv.reader(csvfile)
    next(election)

    total_vote = 0                                                                          # setting initial values
    Khan_vote = 0
    Correy_vote = 0
    Li_vote = 0
    Otooley_vote = 0
    Khan_perc = 0
    Correy_perc = 0
    Li_perc = 0
    Otooley_perc = 0
   
    for row in election:                                                                   
        total_vote = total_vote + 1                                                         # totaling the votes
        if row[2] == 'Khan':                                                                # totaling the votes for each candidate
            Khan_vote += 1
        if row[2] == 'Correy':
            Correy_vote += 1
        if row[2] == 'Li':
            Li_vote += 1
        if row[2] == 'O\'Tooley':
            Otooley_vote += 1 

csvfile.close

Khan_perc = round(((Khan_vote/total_vote) * 100),3)                                         # calculating candidate percentages and rounding them
Correy_perc = round(((Correy_vote/total_vote) * 100),3)
Li_perc = round(((Li_vote/total_vote) * 100),3)
Otooley_perc = round(((Otooley_vote/total_vote) * 100),3)

win_vote = [int(Khan_vote), int(Correy_vote), int(Li_vote), int(Otooley_vote)]              # making a list of candidate votes
win1 = max(win_vote)                                                                        # checking the maimum value in the vote counts

if Li_vote == win1:                                                                         # matching the maximum vote to the candidate
    winner = ("Li")
if Khan_vote == win1:
    winner = ("Khan")
if Correy_vote == win1:
    winner = ("Correy")
if Otooley_vote == win1:
    winner = ("O'Tooley")

textoutput = "Election Analysis\n----------------------------"                              # text output
textoutput = textoutput + "\nTotal Votes: " + str(total_vote)
textoutput = textoutput + "\n----------------------------"
textoutput = textoutput + "\nKhan: " + str(Khan_perc) + "% (" + str(Khan_vote) + ")"
textoutput = textoutput + "\nCorrey: " + str(Correy_perc) + "% (" + str(Correy_vote) + ")"
textoutput = textoutput + "\nLi: " + str(Li_perc) + "% ("  + str(Li_vote) + ")"
textoutput = textoutput + "\nO'Tooley: " + str(Otooley_perc) + "% (" + str(Otooley_vote) + ")"
textoutput = textoutput + "\n----------------------------"
textoutput = textoutput + "\nWinner: " + str(winner)
textoutput = textoutput + "\n----------------------------"
textoutput = textoutput + "\n```"

print(textoutput)

outputfile = open("C:\\Users\\Brendan\\Desktop\\Python-Challenge\\PyPoll\\Analysis\\output.txt","x")
outputfile.write(textoutput)
outputfile.close