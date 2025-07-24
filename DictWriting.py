import csv 

fieldnames = ['name', 'age', 'city']

with open('file.csv', mode='w' , newline='') as file:
  writer = csv.DictWriter(file , fieldnames = fieldnames)
  writer.writeheader()
  for row in data:
    writer.writerow(row)


"""
in file we 'll find :

name,age,city
Alice,30,New York
Bob,25,London

"""
    
  
  
