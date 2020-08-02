#!/usr/bin/python
#coding=utf-8
import exrex
import sys

web_white = ['com','cn','org','edu','gov','www']

#处理URL的格式，去掉http://、https://以及URL中的/符号
def host_para(host):
	if '://' in host:
		host = host.split('://')[1]
	if '/' in host:
		host = host.replace('/','')

	return host

def dic_create(hosts):
	web_dics = hosts.split('.')

	#打开并读取规则配置文件
	f_rule = open('rule.ini','r')
	for i in f_rule:
		if '#' != i[0]:
			rule = i

	#创建字典保存文件
	f_dic = open('dic.txt','w')
	f_dic.close()

	for web_dic in web_dics:
		if web_dic not in web_white:
			f_pass = open('pass.txt',"r")
			for dic_pass in f_pass:
				#使用exrex模块和规则配置文件的内容进行组合匹配生成字典
				dics = list(exrex.generate(rule.format(web_dic=web_dic,dic_pass=dic_pass.strip('\n'))))

				for dic in dics:
					#用于排除过于简单的口令，这里只是简单地进行口令长度的判断，可以自行根据条件进行设置
					if len(dic) > 4:
						f_dic = open('dic.txt','a+')
						f_dic.write(dic)
						f_dic.close()
						print dic.strip('\n')

if __name__ == '__main__':
	if len(sys.argv) == 2:
		dic_create(host_para(sys.argv[1]))
		sys.exit(0)
	else:
		print '[*]Usage: pyhon create_dic.py [URL]'