import csv
# with open('hosts.csv') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(("user:{} ip:{}").format(row["machines"],row["ip"]))
#     print(type(reader))

users = [{"name": "Han Solo", "username": "solm", "department": "IT Infrastructure"},
{"name": "Lio Nelson", "username": "lion", "department": "User"},
{"name": "Ruslan Shamsiev", "username": "rshams", "department": "IT Chief"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_dep:
    writer = csv.DictWriter(by_dep, fieldnames = keys)
    #employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect', fieldnames = keys)
    writer.writeheader()
    writer.writerows(users)
