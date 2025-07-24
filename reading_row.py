import csv

with open('file.csv', newline='') as file:
  reader = csv.DictReader(file)
  for row in reader:
    print(row['name'])

"""
output will be like :

Alice
Bob
"""
