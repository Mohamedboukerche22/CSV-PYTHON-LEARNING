import csv
"""
simple app to check my knowlege in csv

"""
fieldnames = ['name', 'age', 'city']
with open('people.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()

    while True:
        name = input("Enter name (or 'stop'): ")
        if name.lower() == 'stop':
            break
        age = input("Enter age: ")
        city = input("Enter city: ")
        writer.writerow({'name': name, 'age': age, 'city': city})
