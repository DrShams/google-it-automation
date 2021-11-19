#!/usr/bin/python3
import os
import sys

def check_reboot():
    """Return True is the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending reboot")
        sys.exit(1)
    print("Everythin is ok")
    sys.exit(0)

main()
newfucn()
