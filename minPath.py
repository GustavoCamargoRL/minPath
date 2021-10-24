# Implementation of the Dijkstra algorithm for minimum path problem
#
## Author: Gustavo Lima

import math

graph = [[[1,1],[3,1]],[[3,1],[4,1],[5,1]],[[0,1],[6,1],[7,1]],[[2,1],[5,1]],[[8,1]],[[8,1]],[[3,1],[7,1],[8,1]],[],[]]  ## initialization of the graph with the (neighbor, distance)

known=[]
unkown=[0,1,2,3,4,5,6,7,8]
origin = 1
destination = 9
minPath = []
dist = [0]
pred = [None]

for i,neighbor in enumerate(graph):
    if(i == 0):
        None
    else:
        dist.append(math.inf)
        pred.append(len(graph)+1)

while(len(unkown) > 0):
    minDist = math.inf
    for visit in unkown:
        if(dist[visit] < minDist):
            minDist = dist[visit]
            node = visit
    known.append(node)
    unkown.remove(node)
    for neighbor in graph[node]:
        cost = dist[node] + neighbor[1]
        if (cost < dist[neighbor[0]]):
            dist[neighbor[0]] = cost
            pred[neighbor[0]] = node

k = destination - 1

while(k != origin - 1):
    p = k + 1
    k = pred[k]
    minPath.append([p,k+1])

#print(minPath)
print("Distance from A to the respective nodes:")
print(dist)
print("Parent of the respective nodes:")
print(pred)