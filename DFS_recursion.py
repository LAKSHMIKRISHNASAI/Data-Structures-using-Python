# dfs traversal 
def dfs(graph,src,visited):
    visited.add(src)
    print(src,end=' ')
    for nodes in graph[src]:
        if nodes not in visited:
            dfs(graph,nodes,visited)

graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','E','D'],
    'D':['E','C'],
    'E':['B','C','D']
}
visited=set()
dfs(graph,'B',visited)

###################################################################################
def dfs(graph,src,visited):
    visited.add(src)
    print(src,end=' ')
    for nodes in graph[src]:
        if nodes not in visited:
            dfs(graph,nodes,visited)
def addEdge(graph,u,v):
    graph[u].append(v)
    graph[v].append(u)
vertices=5
visited=set()
from collections import defaultdict
# graph=[[]*vertices for _ in range(vertices)] 
graph=defaultdict(list)
addEdge(graph,0,1)
addEdge(graph,0,2)
addEdge(graph,0,3)
addEdge(graph,1,0)
addEdge(graph,2,0)
addEdge(graph,2,3)
addEdge(graph,2,4)
addEdge(graph,3,2)
addEdge(graph,3,4)
addEdge(graph,4,3)
dfs(graph,2,visited)
