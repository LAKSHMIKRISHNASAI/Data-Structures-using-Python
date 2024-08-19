def dfs(graph,src):
    traversal=[]
    stack=[]
    visited=[False]*len(graph)
    #here dfs approach is adding src element to stack and add its adjacent nodes to traversal
    #traversal finds the nodes and if those nodes not in stack append them. 
    stack.append(src)
    while stack:
        node=stack.pop(0)
        if not visited[node]:
            visited[node]=True 
            traversal.append(node)
            print(node,end=' ')
            for neighbors in graph[node]:
                if neighbors not in stack:
                    stack.append(neighbors)
    return traversal 
def addEdge(graph,u,v):
    graph[u].append(v)
    graph[v].append(u)
   
# vertices=5
vertices=5
graph=[[]*vertices for _ in range(vertices)]
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
dfs(graph,2)
