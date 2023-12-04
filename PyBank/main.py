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
value = 0
change = 0
dates = []
profits = []


with open(budget_data_csv, newline='') as csvfile:

    # Specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
  
    # Read the header row first (tracking changes)
    first_row = next(csvreader)
    monthCount += 1
    totalProLos += int(first_row[1])
    value = int(first_row[1])
    
    # Read each row of data after header and first
    for row in csvreader:
        #tracking dates
        dates.append(row[0])
        
        # Calculate changes and adding to list
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total Months
        monthCount += 1
        
        #Total net Profit/Loses
        totalProLos += int(row[1])
        
        #Determin gratest increase in profits
        greatest_increase = max(profits)
        greatest_index = profits.index(greatest_increase)
        greatest_date = dates[greatest_index]
        
        #Determin greatest decrease in profits
        greatest_decrease = min(profits)
        worst_index = profits.index(greatest_decrease)
        worst_date = dates[worst_index]
        
      
        #Average change in "Profit/Losses between months over entire period"
        avg_change = statistics.mean(profits)

#Printing analysis to the terminal
print("Financial Analysis")
print("___________________________________")

print("Total Months: " + str(monthCount))
print("Average Change is: $" + str(round(avg_change, 2)))
print("Total: $" + str(totalProLos))
print("Greatest Increase in Profits: " + str(greatest_date) + "  ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(worst_date) + "  ($" + str(greatest_decrease) + ")")

#Exporting file with results
f = open("financial_analysis.txt", "w")
f.write("Financial Analysis")
f.write('\n')
f.write("___________________________________")
f.write('\n')
f.write("Total Months: " + str(monthCount))
f.write('\n')
f.write("Average Change is: $" + str(round(avg_change, 2)))
f.write('\n')
f.write("Total: $" + str(totalProLos))
f.write('\n')
f.write("Greatest Increase in Profits: " + str(greatest_date) + "  ($" + str(greatest_increase) + ")")
f.write('\n')
f.write("Greatest Decrease in Profits: " + str(worst_date) + "  ($" + str(greatest_decrease) + ")")
