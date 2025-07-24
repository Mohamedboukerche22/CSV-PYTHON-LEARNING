import csv

with open('file.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['moha', 17, 'algeria']),


"""
this will delete all old data 
and create 

moha,17,algeria
"""
