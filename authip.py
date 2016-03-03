#!/usr/bin/python
import re
for line in open ('/var/log/auth.log'):
	ip = re.compile(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d.')
	return [x.group() for x in ip.finditer(ip)]
	print ip

