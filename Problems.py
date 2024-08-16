#!/usr/bin/env python
# coding: utf-8

# In[11]:


# find the minimum distance from source to destination.
# check on all paths 
from collections import deque as queue

row=5 
col=5 
def isSafe(i,j,grid,visited):
    if i>=0 and i<row and j>=0 and j<col and grid[i][j]==0 and not visited[i][j]:
        return True 
    return False

def find_min_distance(grid,srcrow,srccol):
    #cell can move forward or downward only grid[src][dest]=0
    if srcrow==0 or srcrow==row-1 or srccol==0 or srccol==col-1:
        return 0 
    mindistancefromsrc=row*col
    
    
    que=queue()
    visited=[[False]*col for _ in range(row)]
    mindist=[[row*col for _ in range(col+1)]for _ in range(row+1)]
#     for i in range(row):
#         for j in range(col):
#             mindist[i][j]=row*col
    
    que.appendleft([srcrow,srccol])
    mindist[srcrow][srccol]=0
    visited[srcrow][srccol]=True
    while que:
        cell=que.pop()
        new_srcrow=cell[0]
        new_srccol=cell[1]
        
        if isSafe(new_srcrow,new_srccol+1,grid,visited):
            que.appendleft([new_srcrow,new_srccol+1])
             
            mindist[new_srcrow][new_srccol+1]=min(mindist[new_srcrow][new_srccol+1],mindist[new_srcrow][new_srccol]+1)
            visited[new_srcrow][new_srccol+1]=True
        if isSafe(new_srcrow,new_srccol-1,grid,visited):
            que.appendleft([new_srcrow,new_srccol-1])
            
            mindist[new_srcrow][new_srccol-1]=min(mindist[new_srcrow][new_srccol-1],mindist[new_srcrow][new_srccol]+1)
            visited[new_srcrow][new_srccol-1]=True 
        if isSafe(new_srcrow+1,new_srccol,grid,visited):
            que.appendleft([new_srcrow+1,new_srccol])
            
            mindist[new_srcrow+1][new_srccol]=min(mindist[new_srcrow+1][new_srccol],mindist[new_srcrow][new_srccol]+1)
            visited[new_srcrow+1][new_srccol]=True
        if isSafe(new_srcrow-1,new_srccol,grid,visited):
            que.appendleft([new_srcrow-1,new_srccol])
            mindist[new_srcrow-1][new_srccol]=min(mindist[new_srcrow-1][new_srccol],mindist[new_srcrow][new_srccol]+1)
            visited[new_srcrow-1][new_srccol]=True 
#     minsitance=row*col  
    #here traverse through first row, last row, first col and last col
    #need to find the minimum distance from source to each cell.
    for i in range(col):
        mindistancefromsrc=min(mindistancefromsrc,mindist[0][i])
    for i in range(col):
        mindistancefromsrc=min(mindistancefromsrc,mindist[row-1][i])
    for i in range(row):
        mindistancefromsrc=min(mindistancefromsrc,mindist[i][0])
    for i in range(row):
        mindistancefromsrc=min(mindistancefromsrc,mindist[i][col-1])
    
    if mindistancefromsrc==row*col:
        return -1
        
    return mindistancefromsrc
if __name__=='__main__':
    srcrow=3
    srccol=3
    grid= [[1, 1, 1, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 0]]
    print(find_min_distance(grid,srcrow,srccol))
    
    
        


# In[14]:


# edit distance between strings 
# need to find minimum edits needed to make both strings similar.
# three operations either need to insert if char missing, or remove if extra, or replace both char to become same.
# comparing both strings from end, if both charc are matches then move forward i.e. s1[m-1]==s2[n-1]
# else need to perform three operation in which any one would be correct.
# if need to insert an extra character in that position in s1 then s1[m] remains same and make add from s2, so s2[n-1]
# means s1[m],s2[n-1] and add 1 which represents edit is needed.
# or remove means extra char in s1 so s1[m-1] and s2[n] and add 1
# if need to replace then move s1[m-1] and s2[n-1], mark edit is needed.
def edit_distance(x,y,m,n):
    if m==0:
        return n 
    if n==0:
        return m
    elif x[m-1]==y[n-1]:
        return edit_distance(x,y,m-1,n-1)
    else:
        return 1+min(edit_distance(x,y,m,n-1),
                    edit_distance(x,y,m-1,n),
                    edit_distance(x,y,m-1,n-1))
X='GEEXSFRGEEKKS'
Y='GEEKSFORGEEKS'
print(edit_distance(X,Y,len(X),len(Y)))


# In[18]:


def min_distance(x,y,m,n):
#     using tabulation bottom-up approach 
    dp=[[0 for _ in range(n+1)]for _ in range(m+1)] 
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=j
            if j==0:
                dp[i][j]=i
            if x[i-1]==y[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+ min(dp[i][j-1],
                               dp[i-1][j],
                               dp[i-1][j-1])
    return dp[m][n]

x='GEEXSFGEEKKS'
y='GEEKSFORGEEKS'
print(min_distance(x,y,len(x),len(y)))


# In[26]:


# top-down memoization approach 
def edit_dist(x,y,m,n):
    dp=[[-1 for _ in range(n+1)]for _ in range(m+1)]
    
    if m==0:
        return n 
    if n==0:
        return m 
    if dp[m][n]!=-1:
        return dp[m][n]
    if x[m-1]==y[n-1]:
        if dp[m][n]==-1:
            dp[m][n]=edit_dist(x,y,m-1,n-1)
            return dp[m][n]
        else:
            dp[m][n]=dp[m-1][n-1]
            return dp[m][n]
    else:
        if dp[m][n-1]!=-1:
            m1=dp[m][n-1]
        else:
            m1=edit_distance(x,y,m,n-1)
        if dp[m-1][n]!=-1:
            m2=dp[m-1][n]
        else:
            m2=edit_distance(x,y,m-1,n)
        if dp[m-1][n-1]==-1:
            m3=edit_distance(x,y,m-1,n-1)
        else:
            m3=dp[m-1][n-1]
        dp[m][n]=1+min(m1,min(m2,m3))
        #print(dp)
        return dp[m][n]
    
X='GEEXSFRGEEKKS'
Y='GEEKSFORGEEKS'
print(edit_dist(X,Y,len(X),len(Y)))


# In[47]:


# longest common supersequence 
# first find the longest common subsequence.
# finding lcs of two strings, then add remaining characters to the lcs word.

#     return m+n-l
def lcs(x,y,m,n):
    #this method is tabulation.
    L=[[0 for i in range(n+1)] for j in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0 
            elif x[i-1]==y[j-1]:
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    return L[m][n]
def isshortestcommon(x,y):
    m=len(x)
    n=len(y)
#     print(m)
#     print(n)
    l=lcs(x,y,m,n) 
#     print(l)
    return m+n-l
x= "AGGTAB"
y = "GXTXAYB"
# print(lcs(x,y,len(x),len(y)))
print(isshortestcommon(x,y))


# In[51]:


#finding palindromic subsequences.
# either if first and last characters are similar then (i+1,j-1)
# or check (i,j-1) or (i+1,j)
# aab- need to print count of all possible palindromic subsequences.
def palindromic_subsequences(s,i,j): 
    if i==j:
        return 1
    if i>j:
        return 0
    elif s[i]==s[j]:
        #if both left and right characters are matched said to be chances of palindrome.
        #now need to check remaining characters also forming in same way on both the sides.
        return 1+palindromic_subsequences(s,i+1,j)+palindromic_subsequences(s,i,j-1)
    else:
        #if during the counting of above palindromic substrings if same palindromes repeated twice.
        #so remove the multiple times appeared palindromes.
        return palindromic_subsequences(s,i+1,j)+palindromic_subsequences(s,i,j-1)-palindromic_subsequences(s,i+1,j-1)
s='abcb'
print(palindromic_subsequences(s,0,len(s)-1))


# In[54]:


def count_ps(s,i,j):
    #here need to count the number of palindromic substrings can form.
    dp=[[-1 for _ in range(100)]for _ in range(100)]
    if i==j:
        dp[i][j]=1 
        return dp[i][j]
    if i>j:
        return 0 
    if s[i]==s[j]:
        dp[i][j]=1+count_ps(s,i+1,j)+count_ps(s,i,j-1)
        return dp[i][j]
    else:
        dp[i][j]=count_ps(s,i+1,j)+count_ps(s,i,j-1)-count_ps(s,i+1,j-1)
        return dp[i][j]
s='abcb'
print(count_ps(s,0,len(s)-1))


# In[39]:


# dfs traversal 
def dfs(graph,src,visited):
#     stack=[]
#     stack.append(src)
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


# In[38]:


# def dfs(graph,visited,src):
#     visited=set()
#     visited.add(src)
#     print(src,end=' ')
#     for neighbors in graph[src]:
#         if neighbors not in visited:
#             dfs(graph,visited,neighbors)

# another approach 
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


# In[42]:


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


# In[72]:


# from collections import deque
def bfs(graph,src):
    visited=set()
    queue=[]
    queue.append(src)
    traversal=[]
    visited.add(src)
    while queue:
        node=queue.pop(0)
        traversal.append(node)
        print(node,end=' ')
        for neighbors in graph[node]:
            if neighbors not in visited:
                queue.append(neighbors)
                visited.add(neighbors)
    return traversal
   


graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','E','D'],
    'D':['E','C'],
    'E':['B','C','D']
}
# g=[[0,1],[]]
bfs(graph,'C')


# In[68]:


from collections import deque

def bfs(graph, src):
    visited = set()
    queue = deque([src])
    traversal = []

    visited.add(src)

    while queue:
        node = queue.popleft()
        traversal.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return traversal

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E', 'D'],
    'D': ['E', 'C'],
    'E': ['B', 'C', 'D']
}

print(bfs(graph, 'C'))


# In[5]:


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


# In[15]:


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


# In[17]:


# find the minimum cost of path from source to destination node with intermediate node.
# using heap data.

# detect cycle in undirected graph.
# if visited, mark nodes if again visited then return true
# if any node appeared again once visited then return true.

# find the cycle in undirected graph.
# how to know is cycle present or not is if parent of current node is not equal and already in visited nodes then cycle is formed.
class Graph:
    def __init__(self,v):
        self.v=v 
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def dfs_cyclic(self,v,visited,parent):
        visited[v]=True 
        
        for i in self.graph[v]:
            if visited[i]==False:
                self.dfs_cyclic(i,visited,v)
                return True
            elif i!=parent:
                return True 
        return False
                
    def isCyclic(self):
        visited=[False]*self.v 
        
        for i in range(self.v):
            if visited[i]==False:
                if self.dfs_cyclic(i,visited,-1):
                    return True 
        return False
g = Graph(5)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle ")
# g1 = Graph(3)
# g1.addEdge(0, 1)
# g1.addEdge(1, 2)
                


# In[ ]:


# find the number of islands 
# count the islands. visit each vertex and go through vertex is it safe to move and then mark count.
class Graph:
    def __init__(self,r,c,graph):
        self.row=r 
        self.col=c 
        self.graph=graph 
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        return (i >= 0 and i < self.row and
                j >= 0 and j < self.col and
                not visited[i][j] and self.graph[i][j])     
    def dfs(self,i,j,visited):
        move_x=[1,0,-1,1,1,-1,-1,0]
        move_y=[0,1,1,-1,1,-1,0,-1]
        visited[i][j]=True
        for k in range(8):
            if self.isSafe(move_x[k]+i,move_y[k]+j,visited):
                self.dfs(i+move_x[k],j+move_y[k],visited)
                
            
    def count_islands(self):
        visited=[[False]*self.col for _ in range(self.row)] 
        
        for i in range(self.row):
            for j in range(self.col):
                if visited[i][j]==False and self.graph[i][j]==1:
                    self.dfs(i,j,visited)
                    count=count+1 
        return count


# In[2]:


# count the level of nodes.
class node:
    def __init__(self,data):
        self.data=data 
        self.left=self.right=None 
def count_levels(root,data,level):
    if root is None:
        return 0 
    if root.data==data:
        return level 
    downlevel=count_levels(root.left,data,level+1)
    if downlevel!=0:
        return downlevel 
    downlevel=count_levels(root.right,data,level+1)
    return downlevel
root=node(3)
root.left=node(2)
root.right=node(5)
root.left.left=node(1)
root.left.right=node(4)
for i in range(1,6):
    levels=count_levels(root,i,1)
    if levels:
        print('level of node',i,'is',count_levels(root,i,1))
    else:
        print(i,'not present')
    


# In[4]:


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
def print_level(root,data):
    if root is None:
        return 0 
    #approach is selecting the root node with level count 1, until queue is empty pops out first element and append left and right of that node and increase count level 1.
    q=[]
    q.append(root)
    countlevel=1 
    while q:
        size=len(q)
        for i in range(size):
            node=q.pop(0)
            if node.data==data:
                return countlevel 
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        countlevel=countlevel+1 
    return 0 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(6)
for i in range(1,8):   
    level=print_level(root,i)    
    if level:
        print('level of',i,'is',print_level(root,i))
    else:
        print(i,'not present')
        


# In[21]:


# minimum spanning tree 
# this kruskals algorithm first need to sort the edges in increasing order.
# for every edge need to check whether it forming cycle or not, if any edge forming cycle need to discard that edge.
# selecting minimum weight of each edge and then creates a graph.

# kth largest sum contiguous subarray 
def kthlargestsum(arr,k):
    res=[]
    for i in range(len(arr)):
        curr_sum=0
        for j in range(i,len(arr)):
            curr_sum=curr_sum+arr[j]
            res.append(curr_sum)
    print(res)
    for i in range(len(res)):
        if i==k-1:
            return res[i]
   
k=5
# k=3
# arr=[20,-5,-1] 
arr=[10, -10, 20, -40]
print(kthlargestsum(arr,k))


# In[25]:


# height of the binary tree
class node:
    def __init__(self,data):
        self.data=data 
        self.left=self.right=None 
def height(root):
    if root is None:
        return 0 
#     ldepth=height(root.left)
#     rdepth=height(root.right)
#     if ldepth>rdepth:
#         return ldepth+1 
#     else:
#         return rdepth+1
    q=[]
    q.append(root)
    heightcnt=0
    while q:
        #finding height using level  order traversal. iterating on whole level of nodes and moving down.
        size=len(q)
        while size>0:
            node=q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            size=size-1 
        heightcnt+=1 
    return heightcnt
root=node(3)
root.left=node(2)
root.right=node(5)
root.left.left=node(1)
root.left.right=node(4)
height(root)


# In[33]:


# check is the binary tree is heap.
# first need to check whether it is a complete binary tree or not and then check heap property.
# 2i+1 left child and 2i+2 right child.

# traverse through nodes in level wise if node has two childrens or node has single left child then it can continue,
# if node has no children then it is a leaf node.
# check if given tree is complete binary tree 
# to check if at any index if current index is greater than number of nodes then it is not complete binary tree.
# first count the nodes and then recurly check left and right sub trees.
# height of the binary tree
class Node:
    def __init__(self,data):
        self.data=data 
        self.left=self.right=None
def count_nodes(root):
    if root is None:
        return 0 
    return 1+ count_nodes(root.left)+count_nodes(root.right)
def isComplete_tree(root,index,number_nodes):
    if root is None:
        return True 
    if index>=number_nodes:
        return False 
    return isComplete_tree(root.left,2*index+1,number_nodes) and isComplete_tree(root.right,2*index+2,number_nodes)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right=Node(7)
node_count=count_nodes(root)
index=0 
if isComplete_tree(root,index,node_count):
    print('complete binary tree')
else:
    print('not complete binary tree')


# In[34]:


# check if binary tree is heap.


# In[8]:


def k_len_duplicates(s,k):
    dic=set()
    res=[]
    for i in range(len(s)-k+1):
        substr=s[i:i+k]
            # res=res+s[j]
        if substr not in dic:
            #dic[substr]=1 
            dic.add(substr)
            res.append(substr)
    res=''.join(res[i] for i in range(0,len(res),k)) #''.join(keys for keys in dic if dic[res]==1)
    return str(res)
s='geeksforfreeksfo'
k=3
print(k_len_duplicates(s,k))


# In[15]:


# longest distinct characters in the string 
#User function Template for python3

# class Solution:

def longestSubstrDistinctChars(S):
    res=''
        
    max_len=0
    for i in range(len(S)-2):
        dic=set()
        for j in range(i,len(S)-1):
            if S[j]!=S[j+1] and S[j+1] not in dic:
                res=res+S[j]
                dic.add(S[j])
            max_len=max(max_len,len(dic))
#         print(dic)
    return max_len+1
S='geeksforgeeksssseffss'
print(longestSubstrDistinctChars(S))


# In[16]:


def longest_distinct(s):
    n=len(s)
    maxlen=0 
    
    for i in range(len(s)):
        visited=[0]*256 
        for j in range(i,n):
            if visited[ord(s[j])]==False:
                visited[ord(s[j])]=True 
                maxlen=max(maxlen,j-i+1)
            else:
                break 
        visited[ord(s[i])]=False 
    return maxlen 
s='geeksforgeeks'
longest_distinct(s)


# In[18]:


def longest_increasing_subsequence(arr):
    n=len(arr)
    ls=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j]:
                ls[i]=max(ls[i],ls[j]+1)
    return max(ls)

# arr=[3,10,2,1,20]
arr=[10, 22, 9, 33, 21, 50, 41, 60]
longest_increasing_subsequence(arr)


# In[30]:


arr=[10, 22, 9, 33, 21, 50, 41, 60]
count=0
ls=[1]*8
for i in range(1,len(arr)):
    for j in range(i):
        if arr[i]>arr[j]:
            ls[i]=max(ls[i],ls[j]+1)  
#     print(arr[i])
#     print(count)
print(max(ls))


# In[32]:


def lis(arr,n):
    if n==1:
        return 1 
    maximum=1
    max_end_here=1
    for i in range(1,n):
        res=lis(arr,i)
        if arr[i-1]<arr[n-1] and res+1>max_end_here:
            max_end_here=res+1 
    maximum=max(maximum, max_end_here) 
    return maximum 

arr=[10, 22, 9, 33, 21, 50, 41, 60]
n=len(arr)
lis(arr,n)


# In[34]:


# max chain length (a,b), (c,d) if b<c then it can be follows each other.
# and similarly need to take the two axeses to make max chain within the given array.
# similarly need to check next point as d<e (c,d), (e,f) then three points can form chain.
# and length will 3.
class pair:
    def __init__(self,a,b):
        self.a=a 
        self.b=b 
        
def maxchainlength(arr,n):
    mcl=[1 for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if arr[i].a>arr[j].b and mcl[i]<mcl[j]+1:
                mcl[i]=mcl[j]+1 
    return max(mcl)
arr=[pair(5,24),pair(15,25),pair(27,40),pair(50,60)]
maxchainlength(arr,len(arr))


# In[39]:


def find_sum(arr,k):
#     arr.sort()
    for i in range(len(arr)-4+1):
        res=arr[i:i+4]
#         print(res)
        if sum(res)==k:
            return res 
arr=[0,0,2,1,1]
find_sum(arr,3)


# In[42]:


n=len(arr)
k=23
arr=[10,2,3,4,5,7,8]
for i in range(n-3):
    for j in range(i+1,n-2):
        l=j+1 
        r=n-1 
        while l<r:
            if arr[i]+arr[j]+arr[l]+arr[r]==k:
                print(f'{arr[i]} {arr[j]} {arr[l]} {arr[r]}')
                l=l+1 
                r=r-1 
            elif arr[i]+arr[j]+arr[l]+arr[r]<k:
                l=l+1 
            else:
                r=r-1

# n=len(arr)


# In[7]:


def minjumps(arr,n):
    #using tabulation finding the minimum steps needed to reach the end of an array.
    jumps=[0 for i in range(n)]
    
    if n==0 or arr[0]==0:
        return -1 
    jumps[0]=0 
    for i in range(1,n):
        jumps[i]=float('inf')
        for j in range(i):
            if i<=j+arr[j] and jumps[j]!=float('inf'):
                jumps[i]=min(jumps[i],jumps[j]+1)
                break 
    return jumps[n-1]
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n=len(arr)
minjumps(arr,n)           


# In[11]:


def min_jump(arr,l,h):
    if l==h:
        return 1 
    if arr[0]==0:
        return -1 
    
    min_steps=float('inf')
    for i in range(l+1,h+1):
        if i<l+arr[l]+1:
            jumps=min_jump(arr,i,h)
            if jumps!=float('inf') and jumps+1<min_steps:
                min_steps=jumps+1 
    return min_steps
    
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# l=0
# h=len(arr)
min_jump(arr,0,len(arr)-1)


# In[33]:


# count inversions 
# aim is to count the number of inversions needed to make array sorted.
# arr=[2,4,1,3,5]
# this problem can also do with recursion and dp.

def find_count(arr,n):
    if n==0:
        return 0
    #using tabulation. 
    
    dp=[[0 for _ in range(n)]for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                dp[i][j]=1
#     print()
    print(dp)
    inversion_count=0 
    for i in range(n):
        for j in range(i+1,n):
            inversion_count=inversion_count+dp[i][j]
    return inversion_count
arr=[2,4,1,3,5]
# arr=[2, 3, 4, 5, 6]
n=len(arr)
find_count(arr,n)


# In[39]:


# another approach is using merge sort.
def count_inversions(arr,n):
    if n==0:
        return 0
    dp=[0 for _ in range(n)]
#     count=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                dp[i]=dp[i]+1
    print(dp)
    return sum(dp)
arr=[2,4,1,3,5]
# arr=[2, 3, 4, 5, 6]
n=len(arr)
count_inversions(arr,n)


# In[41]:


class Node:  
    def __init__(self, data):  
        self.data = data  
        self.left = None  
        self.right = None  

class BST:  
    def __init__(self):  
        self.root = None  
    
    def insert_node(self, root, data):  
        if root is None:  
            return Node(data)  
        elif data < root.data:  
            root.left = self.insert_node(root.left, data)  
        else:  
            root.right = self.insert_node(root.right, data)  
        return root  

    def inorder_traversal(self, root, arr):  
        if root:  
            self.inorder_traversal(root.left, arr)  
            arr.append(root.data)  
            self.inorder_traversal(root.right, arr)  

    def merge(self, root1, root2):  
        # Get the in-order traversal of both trees  
        list1 = []  
        list2 = []  
        self.inorder_traversal(root1, list1)  
        self.inorder_traversal(root2, list2)  
        
        # Merge the two sorted lists  
        merged_list = []  
        i = j = 0  
        
        while i < len(list1) and j < len(list2):  
            if list1[i] <= list2[j]:  
                merged_list.append(list1[i])  
                i += 1  
            else:  
                merged_list.append(list2[j])  
                j += 1  
                
        # Append remaining elements  
        while i < len(list1):  
            merged_list.append(list1[i])  
            i += 1  
            
        while j < len(list2):  
            merged_list.append(list2[j])  
            j += 1  
            
        return merged_list  

# Example usage  
t = BST()  
root1 = Node(12)  
t.root = t.insert_node(root1, 8)  
t.root = t.insert_node(t.root, 6)  
t.root = t.insert_node(t.root, 24)  
t.root = t.insert_node(t.root, 14)  
t.root = t.insert_node(t.root, 2)  

root2 = Node(17)  
t.root2 = t.insert_node(root2, 18)  
t.root2 = t.insert_node(t.root2, 6)  
t.root2 = t.insert_node(t.root2, 5)  
t.root2 = t.insert_node(t.root2, 34)  
t.root2 = t.insert_node(t.root2, 21)  

# Merging the two BSTs  
ans = t.merge(t.root, t.root2)  
print(ans)


# In[66]:


def word(s,dictionary):
    
#     res=''
#     res=''.join(i for i in dictionary)
#     r=''.join(s)
#     print(res)
#     w=[0 for _ in range(len(s))]
#     for i in range(len(s)):
#         for j in range(len(res)):
#             if w[i]==0 and s[i] in res[j]:
#                 w[i]=1
                
#     print(w)
#     for i in range(len(w)):
#         if w[i]==1:
#             continue 
#         elif w[i]==0:
#             return 0
#     return 1
#             if j==len(s) and s[i] in res[j]:
#                 return 1 
#             else:
#                 return 0
                
#     return 1 if s in res else 0
#     for i in range(len(s)):
#         for j in range(n):
#             if dictionary[j]== s[i]:
#                 res=res+dictionary[j]
#     print(res)
#     return 1 if res==s else 0
# word='abcd'
# here words are also can be in any order.
# approach making one visited list for each char of word s.
#  if all chars are true then that s is present in dict.

d=['o', 'i' ,'nckl', 'f', 'zbexrampe' ,'vhqnddje']
s='ncklaboabzbexrampeabvhqnddjeabfaboaboabiabzbexrampeabiab'
# d=['lrbbmqb', 'cd', 'r', 'owkk']
# s='lrbbmqbabowkkab'
# d=['a','e','bcd','def']
# s='abcd'
# s='ilike'
# dictionary=["i", "like", "sam", "sung", "samsung", "mobile"]
word(s,d)


# In[81]:


# word break problem 
def iswordcontains(word,dic):
    for i in range(len(dic)):
        if word==dic[i]:
            return True 
    return False
    
# approach is after each splitting/breaking of word s, check from the helper function.
# if that sub string present in helper function then return true for chars of sub word as true. 
def word(s,dic):
    size=len(s)
    w=[False for _ in range(size+1)]
    for i in range(1,size+1):
        if w[i]==False and iswordcontains(s[:i],dic):
            w[i]=True
            
            if w[i]==True:
                if i==size:
                    return 1 
        
        for j in range(i+1,size+1):
            #if j reaches the end 
            
            if w[j]==False and iswordcontains(s[i:j],dic):
                w[j]=True 
            if j==size and w[j]==True:
                return 1 
#                 if j==size
    return 0

d=['o', 'i' ,'nckl', 'f', 'zbexrampe' ,'vhqnddje']
s='ncklaboabzbexrampeabvhqnddjeabfaboaboabiabzbexrampeabiab'
# d=['a','e','bcd','def']
# s='abcd'
word(s,d)


        


# In[19]:


# check whether the linked list is palindrome or not.
class node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class llist:
    def __init__(self):
        self.head=None 
#     approach is doing to check whether the string is plaindrome or not using stack and appending all the elements to the stack.
# and then pop each element from the stack then check the popped element and head i same data is true then mark variable as true and else false.
    def is_palindrome(self,head):
#         temp=self.head 
#         stack=[]
#         while temp:
#             stack.append(temp.data)
#             temp=temp.next 
        
#         is_palin=True
#         curr=self.head
#         while curr!=None:
#             Node=stack.pop()
#             if curr.data==Node:
#                 is_palin=True 
#             else:
#                 is_palin=False 
#                 break 
#             curr=curr.next
        
#         print(is_palin)
#         return is_palin 
        #using recursion 
        #by using recusrion approach is taking two pointers left and right , left pointer places at head and right pointer moves to next pointer
        #and checks whether both characters forms palindrome or not. recursion stops once right is None it means reaches last node.
    def add_node(self,data):
        new_node=node(data)
        new_node.next=self.head 
        self.head=new_node
    def print_list(self):
        temp=self.head 
        while temp:
            print(temp.data,end='->')
            temp=temp.next 
ll=llist()
nodes=['a','b','c','d','c','b','a']
for i in nodes:
    ll.add_node(str(i))
if ll.is_palindrome()==True:
    print('given list is palindrome')
else:
    print('not')
ll.print_list()
        
        


# In[ ]:


# another approach is getting the middle node first if it is odd numbers linkedlist.
# traversing through the mid node of list and start the second iteration from mid node to the end of the list.
# reverse the entire second part of the list and then compare the first half and second half nodes whether they are matches or not.
# if matches then return palindrome.


# add two numbers represted by linked lists 
class node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class add_list:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,data):
        if self.head is None:
            self.head=node(data)
            self.tail=self.head
        else:
            self.tail.next=node(data)
            self.tail=self.tail.next
    def printlist(self):
        curr=self.head 
        while curr:
            print(curr.data,end='->')
            curr=curr.next 
            
    def reverse(self,head):
        curr=head 
        prev=None
        while curr:
            next=curr.next 
            curr.next=prev 
            prev=curr 
            curr=curr.next 
        head=prev
        return head
#         self.head=prev 
#         return self.head
    #approach is adding is two numbers first represent in linked lists, make them into array values add those values.
    def add_numbers(self,l1,l2):
        s1=self.reverse(l1)
        s2=self.reverse(l2)
        sum=0
        carry=0 
        res=None
        prev=None 
        if s1 is None or s2 is None:
            return 0
        while s1 is not None or s2 is not None:
            sum=carry+s1.data if s1 else 0 + s2.data if s2 else 0 
            carry=1 if sum>=10 else 0 
            sum=sum%10 
            temp=node(sum)
            
            if res is None:
                res=temp 
            else:
                prev.next=temp 
            prev=temp 
            if s1:
                s1=s1.next 
            if s2:
                s2=s2.next 
        if carry>0:
            temp.next=node(carry)
        ans=self.reverse(res)
        return ans
ll1=add_list()
list1=[9,2,1]
for i in list1:
    ll1.insert(i)
ll2=add_list()    
list2=[3,2,1]
for i in list2:
    ll2.insert(i)
    
res=add_list().add_numbers(ll1,ll2)
print(res)
            
            


# In[13]:


# remove the duplicates from the linkedlist.
# our motive is stay calm and work silently with joy.
class node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
        
class llist:
    def __init__(self):
        self.head=None 
    def push(self,data):
        new_node=node(data)
        new_node.next=self.head 
        self.head=new_node
        return self.head
    def remove_duplicates(self):
#         #approach is using two pointers method, running one pointer after other.
#         curr=self.head 
#         prev=None 
#         while curr and curr.next:
#             if curr.data==curr.next.data:
#                 curr.next=curr.next.next
#                 curr=None
        prev=self.head
        while prev:
            curr=prev
            while curr:
                if prev.data==curr.next.data:
                    curr.next=curr.next.next 
                curr=curr.next
            prev=prev.next
#         return prev
#     def remove_duplicates(self):
#         curr=self.head 
#         while curr:
#             if curr.data==curr.next.data:
                
#                 next_node=curr.next.next 
#                 curr.next=None 
#                 curr.next=next_node
#             curr=curr.next
# #                 curr.next=None
# #                 curr.next=curr.next.next
#         return curr
    def printlist(self):
        curr=self.head 
        while curr:
            print(curr.data,end='->')
            curr=curr.next
ll=llist()
ll.push(10)
ll.push(10)
ll.push(20)
ll.push(20)
ll.push(20)
ll.push(30)
ll.remove_duplicates()
ll.printlist()
        
        
    
#              2 1 3 2 4


# In[32]:


def fibonanci(n):
    #0 1 1 2 3 5
#     if n==0:
#         return 1
#     if n==1:
#         return 1
    if n==0 or n==1:
        return n
        
    return fibonanci(n-1) + fibonanci(n-2)
fibonanci(10)


# In[15]:


def word_dictionary(dictionary,sub_word):
    for i in range(len(dictionary)):
        if sub_word==dictionary[i]:
            return True
    return False
def wordbreak(dictionary,word):
    #approach is checking whether the word is preset in the dictionary or not.
    #breaking the given word into slices and checking with the each word in the dictionary
    #one approach is useing the dp to foun whether entire of the word present in the dictionary or not.
#     to check whether the given word present in the dictioanry we need to sepearte the enter word in the single character lists.
#     dp=[False for _ in range(len(word)+1)]
#     dp[0]=True
#     for i in range(len(word)+1):
# #         if dp[i]==False and 
#         for j in range(i):
#             if dp[j] and word[j:i] in dictionary:
#                 dp[i]=True
#                 break 
#     print(dp)
#     return dp[len(word)]
    size=len(word)
    dp=[False for _ in range(len(word)+1)]
    for i in range(1,len(word)+1):
        if dp[i]==False and word_dictionary(dictionary,word[:i]):
            dp[i]=True 
        if dp[i]==True:
            #if iteration reaches the end of the array then can return the answer.
            if i==size:
                return True 
            for j in range(i+1,size+1):
                if dp[j]==False and word_dictionary(dictionary,word[i:j]):
                    dp[j]=True 
                if j==size and dp[j]==True:
                    print(dp)
                    return True 
    
    return False
                    
#     i l i k e s a m s u n g
    
dictionary=["mobile", "samsung", "sam", "sung", "man",
                "mango", "icecream", "and", "go", "i",
                "like", "ice", "cream"]
word='ilikesamsung'
wordbreak(dictionary,word)


# In[20]:


def word_break(word,dictionary):
    if not word:
        return True
    #starting by iterating from 2nd character so that in inner loop can check 0 to 1 character present in dictionary.
    # if present and similarly check with next remaining characters. If All are satisfies then return True 
    for i in range(1,len(word)+1):
        prefix=word[:i]
        if prefix in dictionary and word_break(word[i:],dictionary):
            return True 
    return False 
word='ilikesamsung' 
dictionary=["mobile", "samsung", "sam", "sung", "man",
                "mango", "icecream", "and", "go", "i",
                "like", "ice", "cream"]
word_break(word,dictionary)


# In[ ]:




