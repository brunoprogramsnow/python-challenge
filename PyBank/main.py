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
    #The total number of months included in the dataset
    for row in fileReader:
        
        month_count.append(row[0])  
        sum_rev += int(row[1])
    
    print(f'Total Months: {len(month_count)}')
    print(f'Total Rev: {sum_rev}')
   
   
    
    
    # maxList = []
    # for row in fileReader:
    #     maxList.append(row[1])
        
    # print(max(maxList))


    
    




#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period