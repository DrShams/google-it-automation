#!/bin/bash

grep "ticky" syslog.log
grep "ERROR" syslog.log
grep "ERROR: Connection to DB failed" syslog.log

nano user_emails.csv
sudo chmod +x csv_to_html.py
sudo chmod  o+w /var/www/html


./csv_to_html.py user_emails.csv /var/www/html/<html-filename>.html
ls /var/www/html

chmod +x ticky_check.py
./ticky_check.py

./csv_to_html.py error_message.csv /var/www/html/error_message.html
./csv_to_html.py user_statistics.csv /var/www/html/user_statistics.html
