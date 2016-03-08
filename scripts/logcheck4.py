#!/usr/bin/python
import re, sys

try:
	file = open('/var/log/auth.log')
	
	ips = []
	
	for text in file.readlines():
		text = text.rstrip()
		regex = re.findall(r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}', text)
		regexloc = re.findall(r'\b192\.168\.0\.[\d]{1,3}', text)
				
		if regex == regexloc:
			pass
		else:
			if regex is not None and regex not in ips:
				ips.append(regex)
			
			for ip in ips:
				add = "".join(ip)
				if add is not '':
					with open('/tmp/bannedips', 'a') as bip:
						bip.write(add + "\n")
						bip.close()
	
	file.close()

except IOError as err:
	print('opps error: %s') % err
