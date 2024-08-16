# # floyd warshall algorithm follows finding the shortest path from current vertex and intermediate vertex.and
# # considering each vertex at every iteration rows and column wise.
# # finding the minimum distance between current distance node and intermediate node between tow nodes.
v=4 
INF=99999
def floyd_warshall(graph):
    
    # dist=list(map(lambda i: list(map(lambda j: j,i)),graph))
    dist=[[0]*v for _ in range(v)]
    print(dist)
    for i in range(len(graph)):
        for j in range(len(graph)):
            dist[i][j]=graph[i][j]
            if graph[i][j]==INF:
                dist[i][j]=99999
    print(dist)
    n=len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    printsolution(dist)

    # min(dist[i][j],dist[i][k] + dist[k][j]) 
    # dist of matrix represents vertex.
def printsolution(dist):
    for i in range(v):
        for j in range(v):
            if dist[i][j]==INF:
                print('INF',end=' ')
            else:
                print(dist[i][j],end=' ')
            if j==v-1:
                print()
graph=[[0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0,   1],
        [INF, INF, INF, 0]]
floyd_warshall(graph)

# ###################################################################
# # transitive closure which finds the path from i to j within joining the intermediate vertices.
class Graph:
    def __init__(self,vertices):
        self.v=vertices
    def printsolution(self,graph):
        for i in range(self.v):
            for j in range(self.v):
                if (i==j):
                    print(1,end=' ')
                else:
                    print(graph[i][j],end=' ')
            print()
    def transitive_closure(self,graph):
        # first create the reach matrix which stores the result nodes.
        reach=[i[:] for i in graph]
        print(reach)

        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    reach[i][j]=reach[i][j] or (reach[i][k] and reach[k][j])
        self.printsolution(reach)
graph=[[1, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1]]
g=Graph(4)
g.transitive_closure(graph)


##############################################################
# find the number of islands.
# connected components contains the nodes connecting with each other in single unit.
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=defaultdict(list)

    def dfs(self,order,visited,v):
        # applyi
        # ng dfs traversal to the unvisited nodes.
        visited[v]=True 
        order.append(v)
        for nodes in self.graph[v]:
            if visited[nodes]==False:
                order=self.dfs(order,visited,nodes)
        return order 
    def connected_components(self):
        visited=[False]*(self.v+1)
        cc=[]
        for i in range(self.v):
            if visited[i]==False:
                order=[]
                cc.append(self.dfs(order,visited,i))
        return cc
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
g=Graph(4)
g.addEdge(1, 0)
g.addEdge(2, 1)
g.addEdge(3, 4)
cc=g.connected_components()
print(cc)


# #######################################################################################################
# # find the number of islands using dfs.
# # initialize the boolean matrix visited of the size given matrix.
# # start the count variable to count the number of islands.
# # run the loop from 0 to till row and nested loop 0 to col. if field/cell is not visited yet and graph[row][col]=1 then call dfs function recursively 
# # and count the islands, then return it.
# # dfs functions contains, if current cell is 1 and not visited yet then call dfs in that and 
# # initialize rowneighbors=[-1,-1,-1,0,0,1,1,1] and colneighbors=[-1,0,1,-1,1,-1,0,1] for neighbor cells.
# # mark the current cell as visited and run loop for neigbors.
# # if the neighbor is safe to visit and not visited then call dfs increment count.

class Graph:
    def __init__(self,row,col,g):
        self.row=row 
        self.col=col 
        self.graph=g
    def issafe(self,i,j,visited):
        if (i>=0 and i<self.row) and (j>=0 and j<self.col) and not visited[i][j] and self.graph[i][j]:
            return True 
        return False
    def dfs(self,i,j,visited):
        
        # marked the current node if it contains 1 then it as visited.

        rowneighbor=[-1,-1,-1,0,0,1,1,1]
        colneighbor=[-1,0,1,-1,1,-1,0,1]
        visited[i][j]=True 

        for k in range(8):
            if self.issafe(i+rowneighbor[k],j+colneighbor[k],visited):
                self.dfs(i+rowneighbor[k],j+colneighbor[k],visited)
    def count_islands(self):
        visited=[[False]*self.col for _ in range(self.row)]
        count=0 
        for i in range(self.row):
            for j in range(self.col):
                # if current cell is 1 and not visited then call dfs.
                if visited[i][j]==False and self.graph[i][j]==1:
                    self.dfs(i,j,visited)
                    count=count+1 
        return count 

graph=[[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

row=len(graph)
col=len(graph[0])
g=Graph(row,col,graph)
print(g.count_islands())


# ######################################################################################################################
# # minimum steps needed to reach the destination of snake and ladder.
# # using the bfs traversal initialising visited and order queue to append visited node.
# # entire arr contains -1, if contains any ladders it goes to up and snakes to tail.
# # class contains vertex and calculate minimum distance.
# # approach is creating an queue appending current 0, while queue is empty pop each vertex.
# # count dist from parent node.
class QueueEntry:
    def __init__(self,v=0,dist=0):
        self.v=v
        self.dist=dist 
def get_min_throws(move,n):
    visited=[False]*n 
    queue=[]
    q=QueueEntry(0,0)
    visited[0]=True
    queue.append(q)
    parent=QueueEntry()
    while queue:
        parent=queue.pop(0)
        v=parent.v
        if v==n-1:
            break 
        j=v+1 
        while j<v+6 and j<n:
            if visited[j]==False:
                a=QueueEntry()
                a.dist=parent.dist+1 
                visited[j]=True
                queue.append(a)

                # check if a is ladder or snake, if it is ladder it moves to up.
                # if it is a snake brings down.
                a.v=move[j] if move[j]!=-1 else j 
            j=j+1 
    return parent.dist

n=30 
moves=[-1]*n 

# ladder steps
moves[2]=21 
moves[4]=7 
moves[10] = 25
moves[19] = 28

# Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6
print(get_min_throws(moves,n))

##########################################################

# bellman-ford algorithm 
# time complexity O(vertices*edges)
# process of bellman ford algorithm used to find the shortest path among all vertices.
# it contains the weights added with source distance vertex to find ditance between u to v.
# initially it starts with 0 and keep all vertices as infinity.
# at each node it iterates n-1 times. bellman-ford algorithm also used to detect negative cycle.
# to detect the negative cycle, if iterating again from one vertex to another if weights+dist[u]<dist[v] again then negative cycle detected.

class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[]
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def printArr(self,dist):
        for i in range(self.v):
            print((i,dist[i]))
    def bellman_ford(self,src):
        reach=[float('inf')]*(self.v+1)

        reach[src]=0 

        for _ in range(self.v-1):

            # now iterate through each node.
            for u,v,w in self.graph:
                if reach[u]!=float('inf') and reach[u]+w<reach[v]:
                    reach[v]=reach[u]+w 
                
            # now need to check is the current node forming negative cycle
            # to get that need to iterate again if dist[u]+w again become less than dist[v] then negative cycle is there.
            for u,v,w in self.graph:
                if reach[u]!=float('inf') and reach[u]+w<reach[v]:
                    print('graph contains negative cycle')
                    return 
        self.printArr(reach)
g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)

g.bellman_ford(0)

