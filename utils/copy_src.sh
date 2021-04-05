#!/bin/bash

user=$1
host=$2
rsa=$3

ssh -i "${rsa}" "${user}"@"${host}" "rm -rf ~/Documents/ws/cassusfett/bin; mkdir ~/Documents/ws/cassusfett/bin"
scp -i "${rsa}" ./src/*.py ./main.py "${user}"@"${host}":~/Documents/ws/cassusfett/bin
