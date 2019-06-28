import os
import csv

csvpath = os.path.join('..', 'Resources', 'netflix_ratings.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

MovieChoice = print(input("What movie are you looking for? "))

