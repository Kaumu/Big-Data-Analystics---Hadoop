#!/usr/bin/env python
import sys

M = dict()
v =[]
for line in sys.stdin:
    lineValues = line.strip().split(' ')
    nid = lineValues[0]
    ntype = lineValues[1]    
    neighbors = lineValues[2:]

    if ntype == 'NODE':
        neighbors = ' '.join([str(elem) for elem in neighbors])
        M.update({nid : neighbors})		#Recover graph structure
    else:
        neighbors = float(lineValues[2])
        v.append({nid : neighbors})

res = dict()
for dict in v:
    for list in dict:
        if list in res:
            res[list] += (dict[list])		#Sum incoming PageRank contributions
        else:
            res[list] = dict[list]

def emit():
    for k,v in M.items():
        for j,l in res.items():
            if k == j:
                print(str(k) +',' + v + ',' + str(l))

emit()