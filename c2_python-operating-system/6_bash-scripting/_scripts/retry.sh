#!/bin/bash

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
    sleep $n
    echo "retry # $n $command"
    ((n+=1))
done;
