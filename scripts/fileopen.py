#!/usr/bin/python
with open(...) as f:
    for line in f:
        <do something>

import re
with open('/var/log/auth.log', r) as f:
    for line in f:
        f = s.split('.')
        if len(f) !=:
            return False
        for x in f:
            if not x.isdigit():
                return False
            i = int(x)
            if i < 0 or i > 255:
                return False
            return True

import re
with open('/var/log/auth.log', r) as f:
    ipaddr = re.compile(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d')
    for line in f:
        mo = ipaddr.search(f)
        print(f)

import re
with open('test', 'r') as f:
    rx = re.compile(r'^[:\)|:\()+%]')
    for line in f:
        x =  rx.search(f)
        print(f)
