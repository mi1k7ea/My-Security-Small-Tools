#!/usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*

if len(sys.argv)!=2:
	print"Usage : ./arp2.py [filename]"
	sys.exit()
	
filename=str(sys.argv[1])
file=open(filename,'r')

for addr in file:
	answer=sr1(ARP(pdst=addr.strip()),timeout=0.1,verbose=0)
	if answer==None:
		pass
	else:
		print addr.strip()
