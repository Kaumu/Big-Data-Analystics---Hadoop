import sys

constant = 999
path = ''
currentNode = None
startPoint = ''
nodes = []
neighbors = []

#Prints node with distance and a path to reach that node
def printPath():
    dist = constant
    if currentNode == startPoint:
        dist = 0
    nodes.append(currentNode)
    open('mapper_input.txt', 'a').write(currentNode + ' ' + str(dist) + ' ' + path + "\n")

# Adds all the neighbors for a source node
def addNeighbor(neighbor):
    isAdded = False
    for i in range(len(neighbors)):
        if neighbor == neighbors[i]:
            isAdded = True
    if isAdded == False:
        neighbors.append(neighbor)

for line in sys.stdin:
    if line == '\n':     
        break
    lineData = line.strip().split(' ')
    nid = lineData[0]
    neighbor = lineData[1]    
    distance = int(lineData[2])
    if currentNode != None:
        if currentNode != nid:
            printPath()
            path = ''
            currentNode = nid
    else:
        startPoint = nid
        currentNode = nid
    addNeighbor(neighbor)
    path = path + neighbor + ',' + str(distance) + ':'

printPath()