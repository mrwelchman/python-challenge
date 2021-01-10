# create a python script that finds
    # total votes
    # list of candidates with
        # % of votes
        # number of votes
    # winner
    
# dependencies
import os
import csv

# set file path
electiondatacsvpath = os.path.join('Resources','Resources','election_data.csv')

# create dictionary containing candidate and votes received
candivotes = {}

total_votes = 0

# read the csv
with open(electiondatacsvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    # header
    csv_header = next(csvreader)
    
    for row in csvreader:
        # adds unique candidates to dictionary and counts their votes as well as a total vote count
        total_votes += 1
        if row[2] in candivotes.keys():
            candivotes[row[2]] = candivotes[row[2]] + 1
        else:
            candivotes[row[2]] = 1
       
# create lists
candidates =[]
votes = []

# add dictionary values to list
for key, value in candivotes.items():
    candidates.append(key)
    votes.append(value)

# add percent list
vote_pct = []
for n in votes:
    vote_pct.append(round(n/total_votes*100, 1))

# convert to tuples
clean_data = list(zip(candidates, votes, vote_pct))

# winner
winner_list = []

for name in clean_data:
    if max(votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]
    
# print to terminal
print("")
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")
for entry in clean_data:
    print(entry[0] + ": " + str(entry[2]) +"% (" + str(entry[1]) +")")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")
print("")

# print to text file
analysis = os.path.join('analysis', 'analysis_file.txt')
with open(analysis, 'w') as analysis_file:
    analysis_file.write("\n")
    analysis_file.write("Election Results\n")
    analysis_file.write("----------------------\n")
    analysis_file.write(f"Total Votes: {total_votes}")
    analysis_file.write("----------------------")
    for entry in clean_data:
        analysis_file.writelines(entry[0] + ": " + str(entry[2]) +"% (" + str(entry[1]) +")\n")
    analysis_file.write("----------------------\n")
    analysis_file.write(f"Winner: {winner}\n")
    analysis_file.write("----------------------\n")
    analysis_file.write("\n")
