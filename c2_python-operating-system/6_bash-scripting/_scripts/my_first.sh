#!/bin/bash

#1
greeting="Welcome"
user=$(whoami)
day=$(date +%A)

echo "$greeting back $user! Today is $day, which is the best day of the entire week!"
echo "Your Bash shell version is: $BASH_VERSION. Enjoy!"

#2
input=/home/$user
# The function total_files reports a total number of files for a given directory.
function total_files {
        find $1 -type f | wc -l
}
echo -n "Files in $input"
echo
total_files $input

#3
num_a=100
num_b=200

if [ $num_a -lt $num_b ]; then
    echo "$num_a is less than $num_b!"
fi

#4
for i in 1 2 7; do
    echo "#4 $i"
done

#5
counter=0
while [ $counter -lt 3 ]; do
    let counter+=1
    echo "#5 $counter"
done

#6
counter=6
until [ $counter -lt 3 ]; do
    let counter-=1
    echo "#6 $counter"
done

#7
counter=1
while [ $counter -le 5 ]; do
    echo "#iteration number $counter"
    ((counter+=1))
done;
