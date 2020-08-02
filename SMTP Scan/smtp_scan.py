#!/usr/bin/python
#coding=utf-8

import socket
import sys

def main():
	if len(sys.argv) != 3:
		print '[*]Usage: python smtp_scan.py [IP] [Username]'
		sys.exit(0)

	ip = sys.argv[1]
	user = sys.argv[2]

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect = s.connect((ip, 25))
	banner = s.recv(1024)
	print banner + '----------'
	s.send('VRFY ' + user + '\r\n')
	result = s.recv(1024)
	print result
	s.close()

if __name__ == '__main__':
	main()