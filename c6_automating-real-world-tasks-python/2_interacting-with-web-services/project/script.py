#! /usr/bin/env python3

import os
import requests

dir = "/data/feedback/"
for f in os.listdir("/data/feedback/"):
    format = ["title","name","date","feedback"]
    info = {}

    with open('{}/{}'.format(dir,f), 'r') as file:
        for x, line in enumerate(file):
            line = line.replace("\n", "")
            info[format[x]] = line.strip('\n')

    response = requests.post("http://34.70.254.249/feedback/",json = info)

    if response.status_code == 201:
        print("+")
    else:
        print("-{}".format(response.status_code))
