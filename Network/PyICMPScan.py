#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Parameter 1 : range @ip (ex: 192.168.0.1-254)
Use : python PyICMPScan.py range @ip
'''

try:
	import sys
	from scapy.all import *
except ImportError as err:
	print err

if len(sys.argv) == 2:
	ans, unan = sr(IP(dst=sys.argv[1])/ICMP(type='echo-request'),verbose=0,timeout=1)
	if ans: ans.make_table(lambda(s,r): ('echo-reply',r.src,r.sprintf('%ICMP.type%') == 'echo-reply'))
else:
	print 'Parameter 1 is mandatory'
