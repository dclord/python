# DO NOT USE - USE NEXT VERSION INSTEAD

#!/usr/bin/python

import re
import sys

def remove_duplicates(ipaddr):
    output = []
    seen = set()
    for ip in ipaddr:
        if ip not in seen:
            output.append(ip)
            seen.add(ip)
        return output


try:
    #open file
   #  bannedip = open('/root/bannedips', 'w')
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

#	with open("/root/bannedips", "ab") as bip:
# loop through the list
	    for ip in ips:
		add = "".join(ip)
		if add is not '':
#leaving in as learning - Not needed- text = add.strip('[')
			with open('/root/bannedips', 'a') as bip:
		                ipaddr = add
              			result = remove_duplicates(ipaddr)
				bip.write(result)
#				bip.write(result + "\n")
				bip.close()
    # close file
    file.close()

except IOError as err:
	print('oops error: %s') % err


