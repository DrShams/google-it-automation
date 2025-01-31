#!/usr/bin/python3

import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2],result[1])

#shell...
#from rearrange import rearrange_name
#rearrange_name("Ruslan, Shamsiev")
#'Shamsiev Ruslan'
