import csv
hosts = [["workstation.local", "192.168.31.1"], ["webserver.cloud", "10.0.0.2"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
