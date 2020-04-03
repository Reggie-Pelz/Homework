
import os
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')

f = open(csvpath, "r")
budget_data = list(csv.reader(f))


#Verify csv is being read correctly
#print(budget_data[:5])

#count months 
total_months = len(budget_data[1:])
#print(total_months)

#calculate total p&l
total_pl = []

for row in budget_data[1:]:
	value = int(row[1])
	total_pl.append(value)

pl_sum = sum(total_pl)
#print(pl_sum)

#create difference list
diff_list = []

for x, y in zip(total_pl[0:], total_pl[1:]):
	diff_list.append(y-x)

#print(diff_list)

avg_change = sum(diff_list) / len(diff_list)
#print(avg_change)

max_increase = max(diff_list)
max_decrease = min(diff_list)

#get indexes of min/max values to return dates
max_increase_loc = diff_list.index(max(diff_list)) + 2
max_decrease_loc = diff_list.index(min(diff_list)) + 2
#print(budget_data[max_increase_loc][0])

max_increase_date = budget_data[max_increase_loc][0]
max_decrease_date = budget_data[max_decrease_loc][0]

#print(max_increase_date + ' ' + str(max_increase))

#format and print the output
print('')
print('Financial Analysis')
print('-----------------------------------')
print(f'Total Months:  {total_months}')
print(f'Total: ${pl_sum}')
print(f'Average Change: ${avg_change:.2f}')
print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')
print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')
