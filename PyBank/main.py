#Importing the OS module
import os

#Importing the CSV module
import csv

#Importing the STATISTICS module
import statistics


budget_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'budget_data.csv')

#Set start conditions
monthCount = 0
totalProLos = 0
greatestIncrease = 0
highMonth = ''
greatestDecrease = 0
lowMonth = ''

#Lists to store monthly change
change = []
monthToMonthChange = []

with open(budget_data_csv, newline='') as csvfile:

    # Specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
  
    # Read each row of data 
    for row in csvreader:   
        monthCount += 1
        totalProLos += int(row[1])
        if int(row[1]) > greatestIncrease: #Determin greatest increase
            highMonth = (row[0])
            greatestIncrease = int(row[1])
        elif int(row[1]) < greatestDecrease:#Determin greatest decrease
            lowMonth = (row[0])
            greatestDecrease = int(row[1])
        change.append(int(row[1]))

  
# track monthly changes
for i in range(len(change)-1):
    monthlyChange = (change[i+1] - change[i])
    monthToMonthChange.append(monthlyChange)   

averageChange = statistics.mean(monthToMonthChange)

#Printing analysis to the terminal
print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(monthCount))
print("Average Change is: $" + str(round(averageChange, 2)))
print("Total: $" + str(totalProLos))
print("Greatest Increase in Profits: " + str(highMonth) + "  ($" + str(greatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(lowMonth) + "  ($" + str(greatestDecrease) + ")")

#Exporting file with results
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write('\n')
f.write("___________________________________")
f.write('\n')
f.write("Total Months: " + str(monthCount))
f.write('\n')
f.write("Average Change is: $" + str(round(averageChange, 2)))
f.write('\n')
f.write("Total: $" + str(totalProLos))
f.write('\n')
f.write("Greatest Increase in Profits: " + str(highMonth) + "  ($" + str(greatestIncrease) + ")")
f.write('\n')
f.write("Greatest Decrease in Profits: " + str(lowMonth) + "  ($" + str(greatestDecrease) + ")")