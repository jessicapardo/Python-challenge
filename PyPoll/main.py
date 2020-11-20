## PyPoll

#Import Modules
import os
import csv


#Set path for file
pypoll_path = os.path.join('Resources', 'election_data.csv')

#Create dictionary for data
vote_count ={}
vote_percentage ={}

#Create variables
total_votes = 0
winner_count = 0

#Open and read csv file 
with open(pypoll_path, "r") as pypoll_file:
    pypoll_reader = csv.reader(pypoll_file, delimiter=",")
    
    #Read header and skip
    pypoll_header = next(pypoll_reader)

    #Loop through the rows of data
    for row in pypoll_reader:

        #Calculate Total Votes
        total_votes += 1

        #Calculate votes for each candidate
        if row[2] in vote_count:
            vote_count[row[2]] += 1
        else:
            vote_count[row[2]] = 1


#Calculate the vote percentage 
for candidate in vote_count:
    vote_percentage[candidate] = (vote_count[candidate] / total_votes) * 100

    #Determine the winner
    if vote_count[candidate] > winner_count:
        winner_count = vote_count[candidate]
        winner = candidate

#Print Election Results
print('Election Results')
print('----------------------------')
print(f'Total Votes: {total_votes}')
print('----------------------------')
for candidate, votes in vote_count.items(): 
    print(f'{candidate}: {vote_percentage[candidate]:.2f}% ({votes})')
print('----------------------------')
print(f'Winner: {winner}')
print('----------------------------')

#Create a .txt file containing the same results in the print out
output_path = os.path.join("Analysis", "PyPollResults.txt")
with open(output_path, "w", newline='') as text_file:
     text_file.write('Election Results\n')
     text_file.write('----------------------------\n')
     text_file.write(f'Total Votes: {total_votes}\n')
     text_file.write('----------------------------\n')
     for candidate, votes in vote_count.items():
        text_file.write(f'{candidate}: {vote_percentage[candidate]:.2f}% ({votes})\n')
     text_file.write('----------------------------\n')
     text_file.write(f'Winner: {winner}\n')
     text_file.write('----------------------------\n')