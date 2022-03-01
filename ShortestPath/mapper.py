#!/usr/bin/env python
import sys

#Separates a main source and all it's neighbors and find out each of their weights
for line in sys.stdin:
    # if line == '\n':     
    #     break
    data = line.strip().split(' ')
    nid = data[0]
    d = int(data[1])
    neighbors = 'blank'
    if len(data) > 2:
        neighbors = data[2]
    route = nid
    if len(data) > 3:
        route = data[3]
        elem = route.split('-')
        if elem[len(elem) - 1] != nid:
            route = data[3] + '-' + nid
    print(nid + ' NODE ' + str(d) + ' ' + neighbors + ' ' + str(route))

    if neighbors != 'blank':
        adj = neighbors.split(':')
        for i in range(len(adj) - 1):
            neighborData = adj[i].split(',')
            neighbor = neighborData[0]
            currentRoute = route + '-' + neighbor
            neighborDistance = d + int(neighborData[1])
            print(neighbor + ' VALUE ' +  str(neighborDistance) + ' ' + currentRoute)