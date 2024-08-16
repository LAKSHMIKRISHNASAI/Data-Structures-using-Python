class queueEntry:
    def __init__(self,vertex=0,distance=0):
        self.v=vertex 
        self.dist=distance 

# approach is need to find the minimum steps required to reach the end of the game.
# here first made all 30 vertices as -1, and then solves using bfs traversal. In which it helps to find the neighbor verteices.
# moving the horizontal way from the initial vertex, and then if in any move ladder found then jumps to up cell and if snake then moves to tail.
# main theme is need to find the distance, so that if any movement occurs need to increment the count.
# first append the initial cell to the queue, and then mark it as visited. later while queue becomes empty i.e. until reaching the final vertex
# moving the dice, popping out the appended vertex and finding the neighbors and then checkig the whether it is a final destination if it is then break and return dist.

def minimum_no_of_throws(move,n):
    visited=[False]*n 

    queue=[]
    queue.append(queueEntry(0,0))
    visited[0] =True 
    # make opening of queueentry to store all the distanc with same name
    qe=queueEntry()
    while queue:
        qe=queue.pop(0)
        v=qe.v
        if v==n-1:
            break
    # initially popped first cell.
        j=v+1 
        while j<=v+6 and j<n:
            if visited[j]==False:
                a=queueEntry()
                a.dist=qe.dist+1 
                visited[j]=True 
                a.v=move[j] if move[j]!=-1 else j 
                queue.append(a)
            j=j+1 
    return qe.dist 
n=30 
moves=[-1]*n
moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28

# Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6
print(minimum_no_of_throws(moves,n))

#################################################################################################
# dijkstra's algorithm used to find the shortest path from source to all vertices.
# this algorithm used to find the shortest path from source vertex to destination. This traversal done by using bfs traversal.
# without changing the source vertex, makes moves on all reachable ways to next vertex with minimum distace.
# djikstra's algorithm used to find the shortest path from source vertex to all vertices.
# two approaches are used find the shortest path one is making utility method.
# creating two list of dist and visited. Initially distance of from source to all vertices is infinite.
import sys 
# first creating method of djkistra's to select source vertex and run it on loop of vertices look up on adjacent vertices, from the help of utility function select the index with minimum value.
class Graph:
    def __init__(self,v):
        self.v=v 
        self.graph=[[0 for i in range(v)]for j in range(v)]
    def printsolution(self,dist):
        for i in range(self.v):
            print(i,dist[i])

    def mindistance(self,dist,visited):
        min=sys.maxsize
        for i in range(self.v):
            if dist[i]<min and visited[i]==False:
                min=dist[i]
                min_index=i 
        return min_index
    def djikstras(self,src):
        visited=[False]*self.v 
        dist=[sys.maxsize]*self.v 

        dist[src]=0 
        # visited[src]=True 

        for _ in range(self.v):
            # now check the adjacent node and select having minimum distance.
            x=self.mindistance(dist,visited)

            visited[x]=True 

            for i in range(self.v):
                if self.graph[x][i]>0 and visited[i]==False and dist[i]>dist[x]+self.graph[x][i]:
                    dist[i]=dist[x]+self.graph[x][i]
        return self.printsolution(dist)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
g.djikstras(0)


# djkistra's using adjacency list using bfs traversal.
import heapq
class graph:
    def __init__(self,vertices):
        self.v=vertices 
        self.adj_list=[[] for _ in range(vertices)]
    def addEdge(self,u,v,w):
        self.adj_list[u].append((v,w))
        self.adj_list[v].append((u,w))
    def shortest_path(self,src):
        pq=[]
        # appending distance and vertex
        heapq.heappush(pq,(0,src))
        dist=[float('inf')]*self.v 
        dist[src]=0 
        while pq:
            d,u=heapq.heappop(pq)

            for v,weight in self.adj_list[u]:
                if dist[v]>dist[u]+weight:
                    dist[v]=dist[u]+weight
                    heapq.heappush(pq,(dist[v],v))
        for i in range(self.v):
            print((i,dist[i]))

if __name__=='__main__':
    v=9 
    g=graph(v)
    g.addEdge(0,1,4)
    g.addEdge(0,7,8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)
    g.shortest_path(0)
