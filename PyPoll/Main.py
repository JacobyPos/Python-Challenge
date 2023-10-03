# Analyzes the records to calculate election data
import csv
import os

# Open csv file and looking for unique candidates
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #capture header row (really just to get it out of the way to collect the data)
    csvheader = next(csvreader)

    #initialize variables
    totalvotes = 0
    candidates = {}

    #scroll through all data (not including header)
    for row in csvreader:
        totalvotes += 1
        candidate = row[2]
        #adding a new candidate to form a unique set of all candidates
        if candidate not in candidates:
            candidates[candidate] = 0
        #summing up votes for each candidate
        candidates[candidate] += 1

#printing results in command line
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {totalvotes}")
print("-----------------------------")
#printing individual candidate info and determing winner
winner = ['',0]
for candidate, votecount in candidates.items():
    print(f"{candidate}: {round(100*votecount/totalvotes,3)}% ({votecount})")
    #determining winner
    if votecount > winner[1]:
        winner[0] = candidate
        winner[1] = votecount
#continuing printing results
print("-----------------------------")
print(f"Winner: {winner[0]}")
print("-----------------------------")


#printing results in txt file
#establishing txt path
outputpath = os.path.join('Analysis','results')
#establishing file
with open(outputpath, 'w') as txtfile:
    #writing results into txt file.  basically same thing from last block.  that's right...i'm writing txt with a csv.writer.  it...works...
    txtwriter = csv.writer(txtfile)
    txtwriter.writerow(['Election Results'])
    txtwriter.writerow(['-----------------------------'])
    txtwriter.writerow([f"Total Votes: {totalvotes}"])
    txtwriter.writerow(['-----------------------------'])
    #writing candidate info
    for candidate, votecount in candidates.items():
        txtwriter.writerow([f"{candidate}: {round(100*votecount/totalvotes,3)}% ({votecount})"])
    #continuing writing results into txt file
    txtwriter.writerow(['-----------------------------'])
    txtwriter.writerow([f"Winner: {winner[0]}"])
    txtwriter.writerow(['-----------------------------'])
