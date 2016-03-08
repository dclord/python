#!/usr/bin/python3

import re

def remove_duplicates(ipaddrs):
    output = []
    seen = set()
    for ipaddr in ipaddrs:
        if value not in seen:
            output.append(ipaddr)
            seen.add(ipaddr)
        return output

ipaddr =
result = remove_duplicates(ipaddrs)
print(result)
