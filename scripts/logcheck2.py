#!/usr/bin/python

import re
import sys


try:
    #open file
    file = open('/var/log/auth.log')
    write = open('/home/dan/bannedip')
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
		with open('/home/dan/bannedip', 'a') as bannedip:
			bannedip.write(add + "\n")
    # close file
    file.close()
    write.close()

except IOError as err:
	print('oops error: %s') % err

