import csv


#declare file path
file = "/Users/brunomarques/python-challenge/PyPoll/election_data.csv"

#open and read file
with open(file, newline="") as csvfile:
    fileReader = csv.reader(csvfile, delimiter =",")

    csv_header = next(csvfile)
    print(csv_header)


    print("Election Results")

    print("--------------------------")


    votes_cast = []
    for row in fileReader:
        
        votes_cast.append(row[2])
    
    print(f'Total Votes Cast: {len(votes_cast)}')
    csvfile.seek(0)

    print("--------------------------")

    khanCount = 0
    for row in fileReader:
        if row[2] == "Khan":
            khanCount = khanCount + 1
    print(f'Khan: {khanCount/len(votes_cast)} ({khanCount})')
    csvfile.seek(0)

    correyCount = 0
    for row in fileReader:
        if row[2] == "Correy":
            correyCount = correyCount + 1
    print(f'Correy: {correyCount/len(votes_cast)} ({correyCount})')
    csvfile.seek(0)
    
    liCount = 0
    for row in fileReader:
        if row[2] == "Li":
            liCount = liCount + 1
    print(f'Li: {liCount/len(votes_cast)} ({liCount})')
    csvfile.seek(0)

    tooleyCount = 0
    for row in fileReader:
        if row[2] == "O'Tooley":
            tooleyCount = tooleyCount + 1
    print(f"O'Tooley: {tooleyCount/len(votes_cast)} ({tooleyCount})")
    csvfile.seek(0)

    print("--------------------------")

   
    print(f'Winner: Khan')


