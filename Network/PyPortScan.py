#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Parameter 1 : range @ip (ex: 192.168.0.1-254)
Use : python PyPortScan.py range @ip
'''

try:
	import sys
	from scapy.all import *
except ImportError as err:
	print err

if len(sys.argv) == 2:
	ans, unan = sr(IP(dst=sys.argv[1])/TCP(dport=(1,1024),flags='S'),verbose=0,timeout=1)
	if ans:	ans.filter(lambda(s,r): r.sprintf('%TCP.flags%') == 'SA').make_table(lambda(s,r): (r.src,r.sport,'Open'))
else:
	print 'Parameter 1 is mandatory'
