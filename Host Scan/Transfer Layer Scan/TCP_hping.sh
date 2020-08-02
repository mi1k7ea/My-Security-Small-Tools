#!/bin/bash

if ["$#" -ne 1]
then
	echo "Usage : ./TCP_hping.sh [/24 network address]"
	exit
fi

prefix=$(echo $1 | cut -d'.' -f 1-3)

for addr in $(seq 1 254)
do
	hping3 $prefix.$addr -c 1 >> r.txt;
done
grep ^len r.txt | cut -d " " -f 2 | cut -d "=" -f 2 >> TCP_hping.txt
rm r.txt
