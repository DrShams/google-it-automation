
#!/usr/bin/env python3
import csv
def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

        employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect', fieldnames = keys)
        #employee_file.writeheader()
        employee_list = []
        for row in employee_file:
            #return_string = "{} {} {}".format(row["Department"],row["Username"],row["Full Name"])
            #print(return_string)
            employee_list.append(row)
        return employee_list
employee_list = read_employees('employees.csv')
print(employee_list)
