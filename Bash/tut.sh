#!/bin/bash
# https://devhints.io/bash

# name="hello"
# echo $name

# Parameters
# name=$#
# echo $name

# Reading user input
# echo "Enter your name: "
# read name
# echo "Your name is $name"


# Arrays
# transport=("bike", "car", "bus", "truck")
# unset transport[1]
# transport[1]="carride"
# echo "${transport[@]}"

# Conditionals
count=10
if [ $count -eq 10 ]
then
    echo "true"
else
    echo "false"
fi

# Operators: -eq, -ne, -gt, -lt, -ge