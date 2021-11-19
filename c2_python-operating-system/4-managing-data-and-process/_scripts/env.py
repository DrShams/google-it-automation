#!/usr/bin/python3

import os

print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

#in bash
#export FRUIT=apple
#it will appear in os.environ.get

import sys
print(sys.argv)

#in bash
#wc env.py
#lines words and characters

#echo $?
#return 0 if previous command successefull
#return 1 if previous command not successefull

filename = sys.argv[1]# takes the first agrument py env.py example - where example is [1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists".format(filename))
    sys.exit(1)
    #echo $? will return 1
