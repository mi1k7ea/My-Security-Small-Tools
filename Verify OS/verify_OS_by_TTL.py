#!/usr/bin/python
#coding=utf-8

from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys

def main():
	if len(sys.argv) != 2:
		print '[*]Usage: python verify_OS_by_TTL.py [IP Address]'
		sys.exit()

	ip=sys.argv[1]

	# 
	ans=sr1(IP(dst=str(ip))/ICMP(),timeout=1,verbose=0)

	if ans == None:
		print "[-]No response was returned. Can\'t verify the OS info."
	elif int(ans[IP].ttl)<=64:
		print "[+]The OS of host is Linux or Unix."
	else:
		print "[-]The OS of host is Windows."

if __name__ == '__main__':
	main()