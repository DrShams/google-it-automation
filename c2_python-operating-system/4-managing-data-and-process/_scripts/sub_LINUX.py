#!/usr/bin/python3
#only works in LINUX

import subprocess
subprocess.run(["date"])
#Пт 22 окт 2021 15:19:42 +05

print(subprocess.run(["sleep","2"]))
#CompletedProcess(args=['sleep', '2'], returncode=0)

a = subprocess.run(["ls","this_file_isnt_exists"])
print(a.returncode)
if a.returncode == 2:
    print(f"SUCCESS {a.returncode}")
else:
    print(f"NOT SUCCESS {a.returncode}")
#2

#a = subprocess.run(["ping","ufaparadise.com"])
#print(a.returncode)
#START to send packages

result = subprocess.run(["host","8.8.8.8"], capture_output= True)#we will see stdout
print(result.returncode)
print(result.stdout)
#b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
#b - an array of bytes

print(result.stdout.decode().split())
#['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

result = subprocess.run(["rm","this_file_isnt_exists"], capture_output=True)
print(result.returncode)
#1
print(result.stdout)
#b''
print(result.stderr)
#b"rm: cannot remove 'this_file_isnt_exists': No such file or directory\n"

import os
#my_env = os.environ.copy()
#my_env["PATH"] = os.pathsep.join(["/opt/myapp", my_env["PATH"]])

#result = subprocess.run(["myapp"], env = my_env)
#print(result)
