## PyBank

# Import Modules
import os
import csv

# Set path for file
pybank_path = os.path.join('Resources', 'budget_data.csv')

# Create list for data
date = []
profit_losses = []


# Open and read csv file 
with open(pybank_path, "r") as pybank_file:
    pybank_reader = csv.reader(pybank_file, delimiter=",")
    
    #Read header and skip
    pybank_header = next(pybank_reader)

    #Initialize the loop to fill lists with data
    for row in pybank_reader:
        date.append(row[0])
        profit_losses.append(int(row[1]))
    
    
#Total of months
total_months = len(date)

#Total Profit/Losses
total_profit_losses = sum(profit_losses)

#The greatest increase in profits
greatest_increase_profits = max(profit_losses)
month_max = date[profit_losses.index(greatest_increase_profits)]

#The greatest decrease in losses
greatest_decrease_profits = min(profit_losses)
month_min = date[profit_losses.index(greatest_decrease_profits)]

#The changes in "Profit/Losses"
tchange = [x-y for x, y in zip(profit_losses[1:], profit_losses)]
avgchange = float('{0:.2f}'.format(sum(tchange)/len(tchange)))



#Print Analysis Results
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_losses}')
print(f'Average Change: ${avgchange}')
print(f'Greatest Increase in Profits: {month_max} (${greatest_increase_profits})')
print(f'Greatest Decrease in Profits: {month_min} (${greatest_decrease_profits})')


#Create a .txt file containing the same analysis in the print out
output_path = os.path.join("Analysis", "PyBankResults.txt")
with open(output_path, "w", newline='') as text_file:
     text_file.write("Financial Analysis\n")
     text_file.write("----------------------------\n")
     text_file.write(f'Total Months: {total_months}\n')
     text_file.write(f'Total: ${total_profit_losses}\n')
     text_file.write(f'Average Change: ${avgchange}\n')
     text_file.write(f'Greatest Increase in Profits: {month_max} (${greatest_increase_profits})\n')
     text_file.write(f'Greatest Decrease in Profits: {month_min} (${greatest_decrease_profits})\n')