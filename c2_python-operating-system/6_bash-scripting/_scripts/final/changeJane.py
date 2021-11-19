#!/usr/bin/python3

import sys
import subprocess

with open(sys.argv[1]) as f:
    for line in f.readlines():
        line = line.strip()
        #old = "./"+line
        #new = "./"+line.replace('jane','jdoe')
        old = line
        new = line.replace('jane','jdoe')
        print("old",old)
        print("new",new)
        subprocess.run(["mv", old, new])
f.close
