import os

# Module for reading CSV files
import csv

import statistics

csvpath = os.path.join('Resources', 'budget_data.csv')

# make empty buckets
total = []
months = []
month_change = []

# make calculation for average
def average (numbers):
    total = 0.0
    for number in numbers:
        total += number
    find_average = total/len(numbers)
    return find_average



with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    # append rows
    for row in csvreader:
        months.append(row[0])
        total.append(row[1])
        month_change.append(int(row[1]))



    # find net amount profit and losses
    total_revenue = 0
    for values in total:
        total_revenue += int(values)
    print(f'Total Profits/Losses: ${total_revenue}')
    net_revenue = [j-i for i,j in zip(month_change[:-1], month_change[1:])]
    print(f'Average Change: ${round(average(net_revenue),2)}')
    net_revenue.sort(reverse=True)
    
    print(f'Total Months: {len(months)}')
    print(f'The greatest increase in profits: ${net_revenue[0]}')
    print(f'The greatest decrease in profits: ${net_revenue[len(net_revenue)-1]}')

    # output
    output_path = 'Financial Analysis.txt'
with open(output_path, 'w', newline ='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["------------------------------------------------------"])
    csvwriter.writerow([f'Total Months: {len(months)}'])
    csvwriter.writerow([f'Total Profits/Losses: ${total_revenue}'])
    csvwriter.writerow([f'Average Change: ${round(average(net_revenue),2)}'])
    csvwriter.writerow([f'The greatest increase in profits: ${net_revenue[0]}'])
    csvwriter.writerow([f'The greatest decrease in profits: ${net_revenue[len(net_revenue)-1]}'])
