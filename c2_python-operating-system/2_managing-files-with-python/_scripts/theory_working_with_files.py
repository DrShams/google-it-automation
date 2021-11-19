import os
#os.remove("guests.txt")
#os.rename("guests.txt","newfile.txt")
print(os.path.exists("newfile.txt"))
print(os.path.getsize("newfile.txt"))
print(os.path.getmtime("newfile.txt"))

import datetime as dt
timestamp = os.path.getmtime("newfile.txt")
x = dt.datetime.fromtimestamp(timestamp)
print(x)

print(os.path.abspath("file.txt"))
print(os.getcwd())
#os.mkdir("newdir")
#os.chdir("newdir")
#os.rmdir("newdir")
print(os.getcwd())
print(os.listdir())

#os.listdir("newfolder")
dir = "newfolder"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))


#option1
file = open("file.txt", encoding='utf-8')
#print(file.readline())
print(file.read())
file.close()

#option2
with open("file.txt") as newfile:
    for line in newfile:
        print(line.strip().upper())
#file.close() is not necesserily cause with automatically close that file

#option2
with open("file.txt", "r+") as nextfile:
    characters = nextfile.write("XXXXX")
    print(characters)
