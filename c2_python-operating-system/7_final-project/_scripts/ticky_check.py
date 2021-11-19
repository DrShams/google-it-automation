#!/usr/bin/env python3

import re
import operator

error_dict = {}
per_user  = {}

with open('syslog.log') as f:
    for line in f.readlines():
        line = line.strip()
        print(line)
        x = re.search(r"ticky:\s(INFO|ERROR):\s([\w' ]*) [\[[#\d]*\]?]? ?\(([.*])\)$", line)

        status = x.group(1)
        mess = x.group(2)
        uname = x.group(3)
        if uname not in per_user.keys():
            per_user[uname] = {}
            per_user[uname]['INFO'] = 0
            per_user[uname]['ERROR'] = 0

        if status == 'ERROR':
            error_dict[mess] = error_dict.get(mess, 0) + 1
            #
            per_user[uname]['ERROR'] += 1
        else:#if status == 'INFO':
            per_user[uname]["INFO"] += 1
        # Populates per_user dict with users and default values
f.close



error_list = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)#sort dictionary by second parameter
error_list.insert(0, ('Error','Count'))
with open('error_message.csv', 'w') as er_file:
    for k, v in error_list:
        er_file.write(str(k) + ', ' + str(v) + '\n')
er_file.close

per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))
with open('user_statistics.csv', 'a') as usr_file:
    usr_file.write('Username' + ',' +  'Info' + ',' + 'Error'+'\n')
    for k, v in per_user_list:
        usr_file.write(str(k) + ',' + str(v['INFO']) + ',' + str(v['ERROR'])+'\n')
usr_file.close
