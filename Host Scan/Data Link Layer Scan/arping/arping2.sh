#!/bin/bash
if ["$#" -ne 1]
then
	echo "Usage : ./arping2.sh [filename]"
	exit
fi

file=$1
for addr in $(cat $file)
do
	arping -c 1 $addr | grep "bytes from" | cut -d " " -f 5 | cut -d "(" -f 2 | cut -d ")" -f 1
done
