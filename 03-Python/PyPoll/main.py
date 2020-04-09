import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Output', 'election_results.csv')

f = open(csvpath, "r")
poll_data = list(csv.reader(f))
poll_data_header = poll_data[0]

total_votes = len(poll_data[1:])
#print(total_votes)

candidate_votes = {}

for row in poll_data[1:]:
	candidate = row[2]

	if candidate in candidate_votes:
		candidate_votes[candidate] += 1
	else:
		candidate_votes[candidate] = 1

candidates_list = list(candidate_votes.keys())
votes_list = list(candidate_votes.values())
sum_votes = sum(votes_list)
most_votes = max(votes_list)
print(most_votes)

#extracted votes
khan_votes = candidate_votes['Khan']
correy_votes = candidate_votes['Correy']
li_votes = candidate_votes['Li']
otooley_votes = candidate_votes["O'Tooley"]

#print(otooley_votes)

#calculate percentages
per_khan_votes = (khan_votes / sum_votes)
per_correy_votes = (correy_votes / sum_votes)
per_li_votes = (li_votes / sum_votes)
per_otooley_votes = (otooley_votes / sum_votes)

#print(per_otooley_votes)

#get winner key based on the most votes
for k, v in candidate_votes.items():
	if v == most_votes:
		winner = k

#print('The winner is ' + winner)

#format and print reults 
print('')
print('Election Results')
print('-----------------------------')
print(f'Total Votes: {total_votes} ')
print('-----------------------------')
print(f'Khan: {per_khan_votes:.3%} ({khan_votes})')
print(f'Correy: {per_correy_votes:.3%} ({correy_votes})')
print(f'Li: {per_li_votes:.3%} ({li_votes})')
print(f"O'Tooley: {per_otooley_votes:.3%} ({otooley_votes})")
print('-----------------------------')
print(f'Winner: {winner}')
print('-----------------------------')

with open(output_path, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(['Election Results'])
	csvwriter.writerow(['-----------------------------'])
	csvwriter.writerow([f'Total Votes: {total_votes} '])
	csvwriter.writerow(['-----------------------------'])
	csvwriter.writerow([f'Khan: {per_khan_votes:.3%} ({khan_votes})'])
	csvwriter.writerow([f'Correy: {per_correy_votes:.3%} ({correy_votes})'])
	csvwriter.writerow([f'Li: {per_li_votes:.3%} ({li_votes})'])
	csvwriter.writerow([f"O'Tooley: {per_otooley_votes:.3%} ({otooley_votes})"])
	csvwriter.writerow(['-----------------------------'])
	csvwriter.writerow([f'Winner: {winner}'])
	csvwriter.writerow(['-----------------------------'])

