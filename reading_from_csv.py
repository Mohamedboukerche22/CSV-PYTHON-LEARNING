import csv


def read(filename):
    people = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in file:
            #row['age'] = int(row['age'])
            people.append(row)
    return people


arr = read('file.csv')
for i in arr:
    print(i)


"""
output will be like :

name,age,city

Alice,30,New York

Bob,25,London
"""
