#!/bin/bash

for file in *.txt; do
  name=$(basename "$file" .txt)
  echo mv "$file" "$name.html"
done

#tail /var/log/syslog | cut -d' ' -f5-
cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head
