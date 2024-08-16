# # depth first search traversal
# # approach -  considering one arbitary node as root node.
# # creating one set for visited nodes and a stack for adjacent nodes.
# # whenever the visited node in the set then its corresponding adjacent nodes are appended into stack.
# # popping the stack element and traversing through its adjacent nodes appending them.
# from collections import deque 
# # concept of graph
# # first either need to create the either graph or tree representation
# # adjacent list or adjacent graph.

# # 0--1,2,24
###########################################################################################################
def dfs(arr,start_node,visited):
    visited=set()
    # approach - 0 ---1

    if visited is None:
        visited=set()
        order=[]

    if start_node not in visited:
        visited.add(start_node)
        order.append(start_node)
        print()
        for nodes in arr[start_node]:
            if nodes not in visited:
                dfs(arr,start_node)
vertices=6
def add_edge(arr,u,v):
    arr[u].append(v)

graph=[[] for _ in range(6)]
add_edge(graph,0,1)
add_edge(graph,0,2)
add_edge(graph,0,3)
add_edge(graph,1,1)
add_edge(graph,2,1)
add_edge(graph,2,3)
add_edge(graph,2,4)
add_edge(graph,3,1)
add_edge(graph,3,2)
add_edge(graph,3,4)
add_edge(graph,4,5)
add_edge(graph,5,4) 
visited=[False]*6
dfs(graph,0,visited)
##############################################################################################################
# find the level of node in the graph
# approach - to find the level of node within their position
# whenever the neighbors of current node are added to queue and curr node not equals to target
# then it shifts to next level.
# first needs to find maximum vertex to define the lenght of adjacent list.
def find_level(edges,v,x):
    max_vertex=0
    for i in edges:
        max_vertex=max(max_vertex,max(i[0],i[1]))
    # return max_vertex

    adj_list=[[] for _ in range(max_vertex+1)]
    for i in range(len(edges)):
        adj_list[edges[i][0]].append(edges[i][1])
        adj_list[edges[i][1]].append(edges[i][0])

    if x>max_vertex and len(adj_list[x]==0):
        return -1 
    q=[]
    q.append(0)
    level=0
    visited=[False]*(max_vertex+1)
    visited[0]=True
    while len(q)>0:
        size=len(q)
        while size>0:
            curr_node=q[0]
            q.pop(0)
            if x==curr_node:
                return level 
            for neighbors in adj_list[curr_node]:
                if not visited[neighbors]:
                    q.append(neighbors)
                    visited[neighbors]=True
            size=size-1
        level=level+1
    return -1
# 0-- 1,2
# 1---0,3
# 2--0,4  based on these we can identify level.

# [0,1],[0,2],[1,3],[2,4] #undirected graph
# 0--1,2
# 1-3
# 2-4
# adj_list[[ , ],[ , ]]
edges=[[0,1],[0,2],[1,3],[2,4]]
x=3
v=5
print(find_level(edges,v,x))





#####################################################################################################################
# from collections import defaultdict
def dfs(graph,start,visited=None):
    if visited is None:
        visited=set()
    order=[]
    if start not in visited:
        visited.add(start)
        order.append(start)
        print(start,end=' ')
        for nodes in graph[start]:
            if nodes not in visited:
                dfs(graph,nodes,visited)
        
# def dfs(arr,start_node):
#     visited=set()

#     visited.add(start_node)
#     print(start_node,end=' ')

#     for neighbors in arr[start_node]:
#         if neighbors not in visited:
#             dfs(arr,neighbors)
def graph(arr,u,v):
    arr[u].append(v)
# {[],[],[]}
# graph=[[0,1],[]]
# arr=defaultdict(list)
# vertices=4
# # arr=[[] for _ in range(vertices)]
# arr={0:set([1,2,3]),
#      1:set([0]),
#      2:set([0,3,4]),
#      3:set([0,2]),
#      4:set([2,3])}
# graph(arr,0,1)
# graph(arr,0,2)
# graph(arr,0,3)
# graph(arr,1,2)
# graph(arr,2,3)
# # graph(arr,2,3)
# graph(arr,2,0)
# # graph(arr,3,0)
# graph(arr,2,3)

# graph(arr,4,2)

# v={0:1, 0:2,0:3}
# v=[[0,1],[0,2],[0,3]]
# dfs(arr,1)
############################################################################################################
from collections import deque
def BFS(arr,start_node,visited):
    # approach - need to first add the node to visited list and to the queue
    # pop from the front queue, check if adjacent nodes of that element is in visited node and queue.
    # if not then add to it.
    # similarly pop each front node from the queue and visit their neighbours and add them into queue.
    q=deque()
    visited[start_node]=True
    q.append(start_node)
    while q:
        node=q.popleft()
        print(node,end=' ')
        for neighbors in arr[node]:
            if not visited[neighbors]:
                q.append(neighbors)
                visited[neighbors]=True 
    # visited=set()
    # q=deque()
    # visited.add(start_node)
    # # print(visited)
    # q.append(start_node)
    # while q:
    #     temp=q.popleft()
    #     print(arr[temp],end=' ')
    #     for i in arr[temp]:
    #         if i not in visited:
    #             visited.add(i)
    #             q.append(i)

# arr={0:[1,2,3],
#      1:[1],
#      2:[0,3,4],
#      3:[2,4],
#      4:[2,3]}

# graph[u][v] table reparesentation 
def add_edge(arr,u,v):
    arr[u].append(v)

vertices=6
graph=[[] for _ in range(6)]
add_edge(graph,0,1)
add_edge(graph,0,2)
add_edge(graph,0,3)
add_edge(graph,1,1)
add_edge(graph,2,1)
add_edge(graph,2,3)
add_edge(graph,2,4)
add_edge(graph,3,1)
add_edge(graph,3,2)
add_edge(graph,3,4)
add_edge(graph,4,5)
# add_edge(graph,5,4) 
# initially set visited of vertices as false
visited=[False]*vertices
BFS(graph,0,visited)
