#!/bin/bash

FILE="users.csv"

tail -n +2 "$FILE" | while read line
do
        username=$(echo $line | cut -d',' -f1)
        password=$(echo $line | cut -d',' -f2)


        useradd "$username"

        echo "$username:$password" | chpasswd

        echo "Created the user: $username"

done
