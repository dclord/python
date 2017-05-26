#!/usr/bin/python
import random
import urllib

def generate():
    d = ['.com', '.org', '.co.uk', '.org.uk']
    u = ''.join([random.choice('abcdefghijklmnopqrstuvwyxz') for x in range(random.randint(30, 40))])
    r = random.choice(d)
    l = u + r
    get(l);

def get(l):
    try:
        urllib.urlopen(l)
        print "Connected" + l
    except Exception, e:
        print "Unable to connect - " + l

if __name__ == "__main__":
    x = 0
    while x <= 10:
        x += 1
        generate()

