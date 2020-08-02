#!/usr/bin/python
#coding=utf-8

import socket
import select
import sys

def main():
	if len(sys.argv) != 4:
		print '[*]Usage: python get_banner_info.py [Target IP] [First Port] [Last Port]'
		sys.exit(0)

	ip = sys.argv[1]
	start = int(sys.argv[2])
	end = int(sys.argv[3])

	for port in range(start, end):
		try:
			ban = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			ban.connect((ip,port))
			ready = select.select([ban],[],[],1)
			if ready[0]:
				print "TCP Port " + str(port) + " : " + ban.recv(4096)
				ban.close()
		except:
			pass

if __name__ == '__main__':
	main()