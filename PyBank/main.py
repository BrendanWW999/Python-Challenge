from importlib.resources import path
import os                               # Importing the file
import csv
import decimal

#sets path info
csvpath = os.path.join('Python-Challenge', 'PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:          # opens and reads CSV file
    budget = csv.reader(csvfile)

    for row in budget:

        if budget.line_num == 2  :      # initilise first variable and preload lower and upper result
            indexold = int(row[1])
            ginc = 0
            gdec = 0
            total = indexold
            months = 1
            total1 = 0

        if budget.line_num > 2  :       # runs here all lines bar the first 2 lines
            index = int(row[1])         # copies the data from the CSV and converts to int
            diff = index - indexold     # calulates between the new and old data
            total1 += diff
            total += index              # generates the total result
            indexold = index            # updates indexold for next check
            months += 1                 # adds up the months
                
            if diff > ginc:             # checks if the diffrence is larger then the old result
                ginc = diff
                highdate = row[0]
            if diff < gdec:             # checks if the diffrence is smaller then the old result
                gdec = diff
                lowdate = row[0]
csvfile.close

Average = round((total1 / (months - 1)), 2)          # Calulates the Average change

textoutput = "Financial Analysis\n----------------------------"
textoutput = textoutput + "\nTotal Months: " + str(months)
textoutput = textoutput + "\nTotal: $"+ str(round(total, 2))
textoutput = textoutput + "\nAverage Change: $" + str(Average)
textoutput = textoutput + "\nGreatest Increase in Profits: " + highdate +  " ($" + str(ginc) + ")"
textoutput = textoutput + "\nGreatest Decrease in Profits: " + lowdate +  " ($" + str(gdec) + ")"
textoutput = textoutput + "\n```"
print(textoutput)

outputfile = open("C:\\Users\\Brendan\\Desktop\\Python-Challenge\\PyBank\\Analysis\\output.txt","x")
outputfile.write(textoutput)
outputfile.close

    

