#!/usr/bin/env python
#-*-coding:utf-8-*-

try:
	import sys, os, re
	from scapy.all import *

	if len(sys.argv) == 2:
		if sys.argv[1] == '--help' or sys.argv[1] == '-h':
			print 'Use SCAPY to found the route between a source address & destination address\n'
	        	print 'How to use ?'
	        	print 'python Traceroot.py @destination'
		else:
			print 'Try to found the route to {0}\n'.format(sys.argv[1])
			ttl = 1
			ans = sr1(IP(dst=sys.argv[1], ttl=ttl)/ICMP(), verbose=0)

			while ans.type != 0:
				if ans.type == 11:
					print 'dst = {0}, ttl = {1}'.format(ans.src, ttl)
					ttl += 1
				ans = sr1(IP(dst=sys.argv[1], ttl=ttl)/ICMP(), verbose=0)
	else:
		print '[ParameterError] parameter 1 mandatory'
except ImportError as err:
	print err
except AttributeError as err:
	print err
except KeyboardInterrupt as err:
	print err
