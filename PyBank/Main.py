# Analyzes the records to calculate bank data
import csv
import os

# Open csv file
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #capture header row
    csvheader = next(csvreader)
    
    #initializing variables
    previousprofit = ""
    currentprofit = ""
    total = 0
    months = 0
    change = 0
    totalchange = 0
    greatestincrease = ["",0]
    greatestdecrease = ["",0]
    #scroll through all data (not including header)
    for row in csvreader:
         #sum total of column 2
         total += int(row[1])
         #find total lines in csv file
         months += 1
         #find total of differences in csv file
         currentprofit = int(row[1])
         if previousprofit != "":
              change = currentprofit - previousprofit
         totalchange += change
         #initializing previousprofit for next iteration
         previousprofit = currentprofit
         #find max of 2nd column and storing the row
         if change > int(greatestincrease[1]):
              greatestincrease = [row[0], change]
         #find min of 2nd column and storing the row 
         if change < int(greatestdecrease[1]):
              greatestdecrease = [row[0], change]      


#printing results in command line
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {months}")
print(f"Total: {total}")
print(f"Average Change: ${round(totalchange/(months-1),2)}")
print(f"Greatest Increase in Profits: {greatestincrease[0]} (${greatestincrease[1]})")
print(f"Greatest Decrease in Profits: {greatestdecrease[0]} (${greatestdecrease[1]})")



#printing results in txt file
#establishing txt path
outputpath = os.path.join('Analysis','results')
#establishing file
with open(outputpath, 'w') as txtfile:
    #writing results into txt file.  basically same thing from last block.  that's right...i'm writing txt with a csv.writer.  it...works...
    txtwriter = csv.writer(txtfile)
    txtwriter.writerow(["Financial Analysis"])
    txtwriter.writerow(["--------------------------"])
    txtwriter.writerow([f"Total Months: {months}"])
    txtwriter.writerow([f"Total: {total}"])
    txtwriter.writerow([f"Average Change: ${round(totalchange/(months-1),2)}"])
    txtwriter.writerow([f"Greatest Increase in Profits: {greatestincrease[0]} (${greatestincrease[1]})"])
    txtwriter.writerow([f"Greatest Decrease in Profits: {greatestdecrease[0]} (${greatestdecrease[1]})"])
