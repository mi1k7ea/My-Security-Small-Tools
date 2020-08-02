#!/bin/bash

if ["$#" -ne 1]
then
	echo "Usage : ./pinger.sh [/24 network address]"
	exit
fi

prefix=$(echo $1 | cut -d '.' -f 1-3)

for addr in $(seq 1 254)
do
	ping -c 1 $prefix.$addr | grep "bytes from" | cut -d " " -f 4 | cut -d ":" -f 1
done
