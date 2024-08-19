# source to destinatioon -- 0 to 8 vertex
# minimum cost path from source node to destination node.
# src=0, dest=2 and intermediate=3 
    #find the distance from source to destination with intermediate node.
    #first find the all distances  from source to vertex u, and from intermediate to u and also from destination fro u.
    #consider minimum from all paths and add them.
    #min distance between 
    #using dijkstras algorithm to find minimum from current vertex to all.
# doing djikstras using heap
# first considering source vertex and then push it into vertices storing list.
from collections import defaultdict 
import heapq 
#and then popping out each vertex and finding neigbhors around vertex heappush.
# source to intermediate ,intermediate to destination.
dist={}
graph=defaultdict(list)
import sys
def djikstras(src,n):
    for i in range(n):
        dist[i]=sys.maxsize
    
    visited=[False]*n 
    dist[src]=0 
    
    s=[]
    heapq.heappush(s,(0,src))
    while s:
        cell=heapq.heappop(s)
        weig=cell[0]
        vertex=cell[1]
        
        for v,weig in graph[vertex]:
            if dist[vertex]+weig<dist[v]:
                dist[v]=dist[vertex]+weig
                heapq.heappush(s,(dist[v],v))
def add_edge(u,v,w):
    graph[u].append((v,w))
    graph[v].append((u,w))

def min_dist(source,intermediate,destination,n):
    ans=sys.maxsize
    djikstras(source,n)
    source_dist={}
    for i in range(n):
        source_dist[i]=dist[i]
    print(source_dist)
    djikstras(intermediate,n)
    #need to find shortest path dist[src]+weight of src(graph[u][v]).
    intermediate_dist={}
    for i in range(n):
        intermediate_dist[i]=dist[i]
    djikstras(destination,n)
    destination_dist={}
    for i in range(n):
        destination_dist[i]=dist[i]
    print(destination_dist)
    for i in range(n):
        ans=min(ans,(source_dist[i]+intermediate_dist[i]+destination_dist[i]))
    return ans
        

n=4 
source=0 
intermediate=2 
destination=3 
add_edge(0,1,1)
add_edge(1,2,2)
add_edge(1,3,3)
    
min_dist(source,intermediate,destination,n)
