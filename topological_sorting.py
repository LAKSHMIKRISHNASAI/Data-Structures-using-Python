# topological sorting follows the order of using for scheduling jobs in order,
# determining the order of tasks while respecting dependencies.

# solving using dfs traversal, initiating the visited and stack pop and
# used to append the values.
# calling recursion for adding neighbhors into it if already present in visited then no need of recursion.


# indegree and out degree of adjacent nodes.
# having less indegrees need to consider first priority.

# DFS
# visited=[]
# def topological_sort(graph,start,visited,stack):
#     #if already visited then recursion won't add 
#     # simple working logic of topological sorting, no indegrees are allowed to consider.
#     visited.add(start)
#     for neighbhors in graph[start]:
#         if neighbhors not in visited:
#             topological_sort(graph,neighbhors,visited,stack)
#     stack.append(start)
#     # [0,1,3,]
    
# def topological(graph):
#     # if visited is None:
#     visited=set()
#     stack=[]
#     vertices=len(graph)
#     for node in range(vertices):
#         if node not in visited:
#             topological_sort(graph,node,visited,stack)
#     return stack

###############################################################################################################
#BFS
from collections import deque
def topological_sort(graph,start):
    v=6
    indegrees={node:0 for node in range(v)} 
    #{0:0,1:0,2:0,3:0}
    for i in graph:
        #[]
        for node in range(len(i)):
            indegrees[i[node]]=+1 
    
    #using bfs traversal for topological sort is counting the in degrees and considering the node having less indegrees.
    #and then start with them. whenever going through them removing of indegrees with on it.
    queue=deque([u for u,v in indegrees.items() if indegrees[u]==0])
    traversal=[]
    # queue.append(start)
    while queue:
        
        node=queue.popleft()
        traversal.append(node)
        for neighbhors in graph[node]:
            indegrees[neighbhors]-=1
            if indegrees[neighbhors]==0:
                queue.append(neighbhors)
                
                #queue(3)
    if len(indegrees)==len(traversal):
        return traversal
    
        
#topological sorting follows the DAG. 
# graph=[[],[],[3],[1],[0,1],[0,2]]
graph=[[4,5],[3,4],[5],[2],[],[]]
# 5-->0<--4 
# |       |
# 2-->3-->1
print(topological_sort(graph,0))
