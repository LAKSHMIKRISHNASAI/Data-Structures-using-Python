# djkistra's algorithm 
# approach is need to find the shortest distance from source node to last vertex.
# first need to find the minimum distance between src to all near vertex.
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=[[0 for _ in range(vertices)]for _ in range(vertices)]
        
    def printSolution(self,dist):
        for i in range(self.v):
            print((i,dist[i]))
    def mindistance(self,dist,visited):
        min=float('inf')
        for v in range(self.v):
            if dist[v]<min and visited[v]==False:
                min=dist[v]
                min_index=v 
        return min_index
    def djikstras(self,src):
        dist=[float('inf')]*self.v
        #approach is from the source i.e. source can be anything either which we mention.
        visited=[False]*self.v
        dist[src]=0
        
        for cout in range(self.v):
            #here source should not change, from source need to find minimum distance vertex.
            u=self.mindistance(dist,visited)
            visited[u]=True
            
            for v in range(self.v):
                if self.graph[u][v]>0 and dist[v]>dist[u]+self.graph[u][v] and visited[v]==False:
                    dist[v]=dist[u]+self.graph[u][v]
        self.printSolution(dist)
                    
                    
g=Graph(9)
g.graph=[[0, 4, 0, 0, 0, 0, 0, 8, 0],
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
