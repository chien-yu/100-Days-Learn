import csv

def read_input():
    passenagers = []
    with open('all/train.csv', newline='') as csvfile:

        rows = csv.DictReader(csvfile)
        for row in rows:
            passenagers.append(row)

    return passenagers

