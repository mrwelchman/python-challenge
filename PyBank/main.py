# create python script that finds
    # total months
    # net total amount of profit/losses
    # changes in profit/loses then avg
    # greatest increase in profts
    # greatest decrease in losses
    # print to terminal
    # export to text file
    
# dependencies
import os
import csv

# set file path
budgetdatacsvpath = os.path.join('Resources', 'budget_data.csv')

# lists
months = []
changes = []
dates = []

# set initials
count = 0
total = 0
current = 0
previous = 0
change = 0

# read the csv
with open(budgetdatacsvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    
    # header
    csv_header = next(csvreader)

    for row in csvreader:
        # count months
        count += 1
        
        # collect months into list
        months.append(row[0])
        
        # calculate total amount
        current = int(row[1])
        total += current
        
        # taking care of the first change value
        if (count == 1):
            previous = current
            continue
            
        else:
        # find change between months
            change = current - previous
            # collect changes into list
            changes.append(change)
            # collect dates into list
            dates.append(row[0])
            # set current to previous
            previous = current
        
    # sum and average of changes
    sum_changes = sum(changes)
    avg_change = round(sum_changes/(count - 1),2)
        
    # find max and min change
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
        
    # find index value that corresponds to the max and min
    best_change = changes.index(greatest_increase)
    worst_change = changes.index(greatest_decrease)
    
    # find the corresponding dates
    best_month = dates[best_change]
    worst_month = dates[worst_change]
        
# print to terminal
print("")
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {count}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {best_month} (${greatest_increase})")
print(f"Greatest Decrease in Loses: {worst_month} (${greatest_decrease})")
print("")

# export to text file
analysis = os.path.join('analysis', 'analysis_file.txt')
with open(analysis, "w") as analysis_file:
    analysis_file.write("\n")
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("---------------------------\n")
    analysis_file.write(f"Total Months: {count}\n")
    analysis_file.write(f"Total: ${total}\n")
    analysis_file.write(f"Average Change: ${avg_change}\n")
    analysis_file.write(f"Greatest Increase in Profits: {best_month} (${greatest_increase})\n")
    analysis_file.write(f"Greatest Decrease in Loses: {worst_month} (${greatest_decrease})\n")
    
