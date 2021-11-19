#!/bin/bash

>oldFiles.txt

file_list=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
echo $file_list

for file in $file_list:do

  do if test -e ~/data/"$i"; then
     echo "$i" >> OldFiles.txt;
  else
     echo "File doesn't exist"; fi
done
