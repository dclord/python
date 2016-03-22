#!/usr/bin/python3
import json

with open('mytweeys.json', 'r') as f:
    line = f.readline()
    tweet = json.load(line)
    print(json.dumps(tweet, indent=4))

    