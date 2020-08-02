#!/usr/bin/python
#coding=utf-8
import requests
import sys
from Queue import Queue
import threading
from agent_proxy import user_agent_list
from optparse import OptionParser

class DirScanMain:
	"""docstring for DirScanMain"""
	def __init__(self, options):
		self.url = options.url
		self.filename = options.filename
		self.count = options.count
		
	class DirScan(threading.Thread):
		"""docstring for DirScan"""
		def __init__(self, queue,total):
			threading.Thread.__init__(self)
			self._queue = queue
			self._total = total
				
		def run(self):
			while not self._queue.empty():
				url = self._queue.get()

				#
				threading.Thread(target=self.msg).start()

				try:
					r = requests.get(url=url, headers=user_agent_list.get_user_agent(), timeout=8,)
					if r.status_code == 200:
						sys.stdout.write('\r' + '[+]%s\t\t\n' % (url))
						result = open('result.html','a+')
						result.write('<a href="' + url + '" target="_blank">' + url + '</a>')
						result.write('\r\n</br>')
						result.close()
				except Exception as e:
					pass

		def msg(self):
			# print self._total,self._queue.qsize()
			per = 100 - float(self._queue.qsize())/float(self._total) * 100
			percentage = "%s Finished| %s All| Scan in %1.f %s"%((self._total - self._queue.qsize()),self._total,per,'%')
			sys.stdout.write('\r'+'[*]'+percentage)

	def start(self):
		result = open('result.html','w')
		result.close()

		queue = Queue()

		f = open('./dics/%s'%self.filename,'r')
		for i in f:
			queue.put(self.url+i.rstrip('\n'))

		#
		total = queue.qsize()

		threads = []
		thread_count = int(self.count)

		for i in range(thread_count):
			threads.append(self.DirScan(queue,total))
		for i in threads:
			i.start()
		for i in threads:
			i.join()

if __name__ == '__main__':

	print '''
	 ____  _      ____                  
	|  _ \(_)_ __/ ___|  ___ __ _ _ __  
	| | | | | '__\___ \ / __/ _` | '_ \ 
	| |_| | | |   ___) | (_| (_| | | | |
	|____/|_|_|  |____/ \___\__,_|_| |_|

	'''

	parser = OptionParser('./web_dir_scan.py -u <Target URL> -f <Dictionary file name> [-t <Thread_count>]')
	parser.add_option('-u','--url',dest='url',type='string',help='target url for scan')
	parser.add_option('-f','--file',dest='filename',type='string',help='dictionary filename')
	parser.add_option('-t','--thread',dest='count',type='int',default=10,help='scan thread_count')
	(options,args)=parser.parse_args()

	if options.url and options.filename:
		# start(options.url,options.filename,options.count)
		dirscan = DirScanMain(options)
		dirscan.start()
		sys.exit(1)
	else:
		parser.print_help()
		sys.exit(1)