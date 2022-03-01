a = set(line.strip() for line in open('nodes_small.txt'))
a = list(a)

for row in a:
    open('pg_small.txt', 'a').write(row + "\n")

with open('pg_small.txt') as f:
    lines = [x.split() for x in f.read().splitlines()]
nodes = {}
for line in lines:
    nodes[line[0]] = []

for line in lines:
    if line[1:] == []:
        nodes[line[0]] = [] #Handling dangling nodes
    else:
        nodes[line[0]].append(line[1:][0]) #Appending the outgoing nodes

unique_nodes = len(nodes.keys()) 
pagerank = 10/ float(unique_nodes) #Using 10 to get better decimal pageranks

#Saving output in a new file
with open('small_pg_input.txt', 'a') as out_file:
    for i, adj in nodes.items():
        adj = ' '.join([str(elem) for elem in adj])
        out_file.write(str(i) +',' + adj + ',' + str(pagerank) + "\n")