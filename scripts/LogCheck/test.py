#!/usr/bin/python3
import re

try:
    file = open('test', 'r')
    emo = []
    for text in file.readlines():
        text = text.rstrip()
       regex = re.match(r'^(:[)(])*$', text)
        if regex is not None:
            print(regex)
except IOError as error:
    print('error: %s') % error