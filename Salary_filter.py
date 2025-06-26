import csv
with open('Employee.csv',mode='r') as file:
    reader=csv.DictReader(file)
    
    print("Employees with Salary > 50k")
    for row in reader:
        if int (row['Salary'])>50000:
            print(row)