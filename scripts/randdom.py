#!/usr/bin/python
import random

def generate():
    d = ['.com', '.org', '.co.uk', '.org.uk']
    u = ''.join([random.choice('abcdefghijklmnopqrstuvwyxz') for x in range(random.randint(30, 40))])
    r = random.choice(d)
    print u + r

if __name__ == "__main__":
    x = 0
    while x <= 10:
        x += 1
        generate()

