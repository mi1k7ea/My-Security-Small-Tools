#!/usr/bin/python
#coding=utf-8

import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def main():
	if len(sys.argv)!=3:
		print '[*]Usage: python fw_detect.py [IP Address] [Port]'
		sys.exit()

	ip=sys.argv[1]
	port=sys.argv[2]

	ACK_response=sr1(IP(dst=ip)/TCP(dport=port,flags='A'),timeout=1,verbose=0)
	SYN_response=sr1(IP(dst=ip)/TCP(dport=port,flags='S'),timeout=1,verbose=0)

	if (ACK_response==None) and (SYN_response==None):
		print "[*]Port is either unstatefully filtered or host is down."
	elif ((ACK_response==None) or (SYN_response==None)) and not ((ACK_response==None) and (SYN_response==None)):
		print "[*]Stateful filtering in place."
	elif int(SYN_response[TCP].flags)==18:
		print "[+]Port is unfiltered and open."
	elif int(SYN_response[TCP].flags)==20:
		print "[*]Port is unfiltered and closed."
	else:
		print "[-]Unable to determine if the port is filtered."

if __name__ == '__main__':
	main()