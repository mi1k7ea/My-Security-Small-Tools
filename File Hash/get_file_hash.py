#coding=utf-8
import hashlib
import sys
 
if len(sys.argv) == 3:
	try:
		if(sys.argv[2].lower() == 'md5'):
			print hashlib.md5(open(sys.argv[1],'rb').read()).hexdigest()
		elif(sys.argv[2].lower() == 'sha-1'):
			print hashlib.sha1(open(sys.argv[1],'rb').read()).hexdigest()
		elif(sys.argv[2].lower() == 'sha-256'):
			print hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest()
		elif(sys.argv[2].lower() == 'sha-512'):
			print hashlib.sha512(open(sys.argv[1],'rb').read()).hexdigest()
		else:
			print '[-]Please input a correct encryption algorithm.'
	except:
		print '[-]Please input a correct filename.'
else:
	print '[*]Usage: python check_hash.py [Filename] [MD5|SHA-1|SHA-256|SHA-512]'