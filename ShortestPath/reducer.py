#!/usr/bin/env python

import sys

minDist = 9999
currentMin = None
neighbors = None
currentNode = None

def printPath(route):
    print(str(currentNode) + ' ' + str(minDist) + ' ' + neighbors + ' ' + route)

#Calculates the minimum distance and route to target from source
for line in sys.stdin:
    # if line == '\n':     
    #     break
    data = line.strip().split(' ')
    nid = data[0]
    nodeType = data[1]
    d = int(data[2])

    if nodeType == 'NODE':
        if currentNode != None:
            if currentMin == None:
                currentMin = nid
            printPath(route)
        route = data[4]
        neighbors = data[3]
        currentNode = nid
        minDist = d
        currentMin = nid
    else:
        if d < minDist:
            minDist = d
            currentMin = nid
            route = data[3]
printPath(route)