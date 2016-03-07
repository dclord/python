#!/usr/bin/python

import re
import sys


try:
    #open file
    file = open('/var/log/auth.log')
    # create empty list
    ips = []
    # read text through file
    for text in file.readlines():
        # strip
        text = text.rstrip()
        # regex
        regex = re.findall(r'[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}', text)
        # append ips list
        if regex is not None and regex not in ips:
            ips.append(regex)

    # loop through the list
    for ip in ips:
	add = "".join(ip)
	if add is not '':
#leaving in as learning - Not needed- text = add.strip('[')
		with open('/home/root/bannedip', 'a') as bannedip:
			bannedip.write(add + "\n")
		bannedip.close()
    # close file
    file.close()

except IOError as err:
	print('oops error: %s') % err

