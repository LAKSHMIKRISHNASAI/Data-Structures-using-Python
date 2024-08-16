from collections import defaultdict
class graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph= defaultdict(list)#[[0] for _ in range(vertices)]
    def addEdge(self,u,v):
        self.graph[u].append(v)
    # [[]*6 for _ in range(6)]
    def iscyclicutil(self,vertex,visited,recstack):
        visited[vertex]=True 
        recstack[vertex]=True

        for neighbors in self.graph[vertex]:
            if visited[neighbors]==False:
                # if not visited yet then it won't make circle as for this step
                if self.iscyclicutil(neighbors,visited,recstack)==True:
                    return True 
            
            elif recstack[neighbors]==True:
                return True 
        recstack[neighbors]=False 
        return False 
    def iscyclic(self):
        visited=[False]*(self.v+1) 
        recstack=[False]*(self.v+1)
        for node in range(self.v):
            if visited[node]==False:
                if self.iscyclicutil(node,visited,recstack)==True:
                    return True 
        return False 
g=graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.iscyclic()==True:
    print('graph contains cycle')
else:
    print('not cycle')


#########################################################################
# detect cycle in undirected graph 
# if node found visited again or parent is not equal to current node.
class graph:
    def __init__(self,vertices):
        self.v=vertices
        # self.graph=defaultdict(list)
        self.adj_list=[[] for _ in range(vertices)]
    def addEdge(self,u,v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    # first need to traverse through unvisited nodes make them visited
    # add all the nodes to result list and return.
    def dfsutil(self,order,visited,v):
        visited[v]=True 
        order.append(v)
        for neighbors in self.adj_list[v]:
            if visited[neighbors]==False:
                order=self.dfsutil(order,visited,neighbors)
        return order
    def connected_component(self):
        visited=[False]*(self.v+1)
        cc=[]
        for node in range(self.v):
            if visited[node]==False:
                order=[]
                cc.append(self.dfsutil(order,visited,node))
        return cc
    def iscyclicutil(self,v,visited,parent):
        visited[v]=True 

        for neighbors in self.graph[v]:
            if visited[neighbors]==False:
                if self.iscyclicutil(neighbors,visited,v)==True:
                    return True 
            elif parent!=neighbors:
                return True 
        return False 
    def iscyclic(self):
        visited=[False]*(self.v+1)
        for node in range(self.v):
            if visited[node]==False:
                if self.iscyclicutil(node,visited,-1)==True:
                    return True 
        return False 

g = graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
cc=g.connected_component()
print(cc)
if g.iscyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle ")
g1 = graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)


# if g1.iscyclic():
#     print("Graph contains cycle")
# else:
#     print("Graph doesn't contain cycle ")