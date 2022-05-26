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

print("Total Votes ", str(total_vote))
print("Khan: ", str(Khan_perc) + "% (" + str(Khan_vote) + ")")
print("Correy: ", str(Correy_perc) + "% (" + str(Correy_vote) + ")")
print("Li: ", str(Li_perc) + "% ("  + str(Li_vote) + ")")
print("O'Tooley: ", str(Otooley_perc) + "% (" + str(Otooley_vote) + ")")

win_vote = [int(Khan_vote), int(Correy_vote), int(Li_vote), int(Otooley_vote)]              # making a list of candidate votes
win1 = max(win_vote)                                                                        # checking the maimum value in the vote counts
winner = str()

if Li_vote == win1:                                                                         # matching the maximum vote to the candidate (this could be a problem if there was a tie)
    print("Winner: Li")
if Khan_vote == win1:
    print("Winner: Khan")
if Correy_vote == win1:
    print("Winner: Correy")
if Otooley_vote == win1:
    print("Winner: O'Tooley")

#textoutput = "Election Analysis\n----------------------------"
#textoutput = textoutput + "\nTotal Votes ", str(total_vote)
#textoutput = textoutput + "\nKhan: ", (Khan_perc) + "% (" + (Khan_vote) + ")"
#textoutput = textoutput + "\nCorrey: ", (Correy_perc) + "% (" + Correy_vote + ")"
#textoutput = textoutput + "\nLi: ", (Li_perc) + "% ("  + (Li_vote) + ")"
#textoutput = textoutput + "\nO'Tooley: ", (Otooley_perc) + "% (" + Otooley_vote + ")"
#print(textoutput)

#outputfile = open("output.txt","x")
#outputfile.write(textoutput)
#outputfile.close