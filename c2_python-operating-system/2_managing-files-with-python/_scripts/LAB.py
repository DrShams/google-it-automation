#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

        with open(csv_file_location, 'r') as infile, open('employees_y.csv', 'w') as outfile:
            keys = [" Department", " Username", "Full Name"]
            writer = csv.DictWriter(outfile, fieldnames = keys)
            writer.writeheader()
            for row in csv.DictReader(infile):
                writer.writerow(row)

        employee_file = csv.DictReader(open("employees_y.csv"), dialect = 'empDialect')
        employee_list = []
        for x in employee_file:
            employee_list.append(x)
        return employee_list
employee_list = read_employees('employees.csv')#Don't forget to change this part in above code.
print(employee_list)



def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
        department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data
dictionary = process_data(employee_list)
print(dictionary)



def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
                f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()
#write_report(dictionary, '/home/username_example-2323hkhk/test_report.txt')
