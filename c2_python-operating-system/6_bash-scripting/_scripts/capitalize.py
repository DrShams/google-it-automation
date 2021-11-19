#!/usr/bin/python3

import sys

for line in sys.stdin:
    words = line.strip().split()
    print(" ".join([word.capitalize() for word in words]))
    #string.replace(old_substring, new_substring)
