#!/usr/bin/env python
import sys

for line in sys.stdin:
    if line == '\n':
        break

    lineValues = line.strip().split(',')
    nid = lineValues[0]
    neighbors = lineValues[1]
    adj = lineValues[1].split(' ')
    p = float(lineValues[2]) / (len(adj))
    print(nid + ' NODE ' + neighbors)       #Pass along graph structure
    for nodeid in adj:
        print(nodeid + ' VALUE ' +  str(p))	#Pass pagerank mass to neighbors