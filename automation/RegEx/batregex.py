#!/usr/bin/python3
import re
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()



re.compile(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d') # ip address regex

