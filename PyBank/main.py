import csv


#declare file path
file = "/Users/brunomarques/python-challenge/PyBank/budget_data.csv"

#open and read file
with open(file, newline="") as csvfile:
    fileReader = csv.reader(csvfile, delimiter =",")

    csv_header = next(csvfile)
    print(csv_header)

    
    print("Financial Analysis")
    print("---------------------------------------------")
    
    month_count = []
    sum_rev = 0
    rev_vals = []
    
    for row in fileReader:
        
        month_count.append(row[0])  
        sum_rev += int(row[1])
        rev_vals.append(row[1])
    
    avg_start = int(rev_vals[0])
    avg_end = int(rev_vals[len(rev_vals) - 1])
    change_in_avg = (avg_end - avg_start)/(len(month_count) - 1)

    print(f'Total Months: {len(month_count)}')
    print(f'Total Rev: {sum_rev}')
    print(f'Average Change:{change_in_avg}')

    deInProfts = []
    counter = 0
    for i in rev_vals:
        if counter >= 1:
            deInProfts.append(int(rev_vals[counter]) - int(rev_vals[counter -1]))
            counter += 1
        else:
            counter += 1
    
    increase_date = month_count[deInProfts.index(max(deInProfts)) + 1]
    decrease_date = month_count[deInProfts.index(min(deInProfts)) + 1]
    
    print(f'Greatest Increase in Profits: {increase_date} {max(deInProfts)}')
    print(f'Greatest Decrease in Profits: {decrease_date} {min(deInProfts)}')

    print("---------------------------------------------")
