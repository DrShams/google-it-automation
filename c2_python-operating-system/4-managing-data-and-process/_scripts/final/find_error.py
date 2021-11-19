#!/usr/bin/env python3

import sys
import os
import re

def error_search(log_file):

    error = input("What is the error? ")
    returned_errors = []

    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            es = error.split(' ')
            for i in range(len(es)):
                error_patterns.append(r"{}".format(es[i].lower()))
            if all(re.search(ep, log.lower()) for ep in error_patterns):
                returned_errors.append(log)
    file.close#is not necesserily cause we use 'with' open
    return returned_errors

def file_output(returned_errors):
    #with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    with open('errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
    file.close#is not necesserily cause we use 'with' open

if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)
