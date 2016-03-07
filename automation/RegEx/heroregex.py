#!/usr/bin/python3
import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex = heroRegex.search('Batman and Tina Fey.')
mo1.group()

print(mo1)