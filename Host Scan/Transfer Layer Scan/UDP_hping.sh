#!/bin/bash

if ["$#" -ne 1]
then
	echo "Usage : ./UDP_hping.sh [/24 network address]"
	exit
fi

prefix=$(echo $1 | cut -d'.' -f 1-3)

for addr in $(seq 1 254)
do
	hping3 $prefix.$addr --udp -c 1 >> r.txt;
done
grep Unreachable r.txt | cut -d " " -f 5 | cut -d "=" -f 2 >> UDP_hping.txt
rm r.txt
