import csv

with open('comments.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        print(row['ratings'])