#!/usr/bin/python
#coding=utf-8

blacklist = ['acunetix', 'awvs', 'wvstest', 'vulnweb.com', 'injected_by_wvs']
ips = []

try:
	with open('/var/log/apache2/access.log','r') as f:
		for i in f.readlines():
			for j in blacklist:
				if j in i:
					ip = i.split(' ')[0]
					if ip not in ips:
						ips.append(ip)
						print "[+]Found AWVS Scan!"
						print "[+]IP Address: " + ip
						print "[+]The Detail Info: "
						print i.strip('\n').strip('\r')
						print
		
		if len(ips) == 0:
			print "[*]There is no action of AWVS scan."

except Exception as e:
	print "[-]Can't open the Apache2's access.log!"
	print e