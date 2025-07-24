import csv

with open('file.csv',newline='') as file :
  reader = csv.reader(file)
  for row in reader:
    print(row)


"""
output will be like this 

['name', 'age', 'city']
['Alice', '30', 'New York']
['Bob', '25', 'London']

"""
