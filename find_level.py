def find_order(edges,v,x):
    max_vertex=0
    for i in edges:
        max_vertex=max(max_vertex,max(i[0],i[1]))
    print(max_vertex)

    adj_list=[[] for _ in range(max_vertex+1)]
    for i in range(len(edges)):
        adj_list[edges[i][0]].append(edges[i][1])
        adj_list[edges[i][1]].append(edges[i][0])
    
    if x>max_vertex and len(adj_list[x]==0):
        return -1
    q=[]
    q.append(0)
    visited=[False]*(max_vertex+1)
    visited[0]=True
    level=0
    # need to understand while moving to next level  size is going to be reduce at each iteration.
    while q:
        size=len(q)
        while size>0:
            curr_node=q[0]
            q.pop(0)
            if curr_node==x:
                return level
            for neighbors in adj_list[curr_node]:
                if not visited[neighbors]:
                    q.append(neighbors)
                    visited[neighbors]=True
            size=size-1
        level=level+1
    return -1

edges=[[0,1],[0,2],[1,3],[2,4]]
v=5
# x=2
print(find_order(edges,v,3))

    # [ , ]    [ , ]    [ , ]    [ , ]   [ , ]
    #   0        1        2        3       4
# 0 -1,2
# 1-0,3
# 2-0,4

#finding the path in the matrix that reaches the end with maximum height difference is minimum of adjacent cells.
#need to check the next step is valid on all four sides in the grid of cell(i,j)
# consider current cell as visited[i][j]
# consider maximum difference 
# using binary search, finding the mid. check if we go outside the matrix or if cell(i,j) is visited or absolute difference b/w 
# consecutive cells is greater than our assumed maximum energy required.
# check if we reach the bottom right cell.
# creating is valid function which used to check whether the node is reached last end, if yes then true.
# consider current node is visited true and recursively check row and column not less than 0 and absolute difference between consecutive cells becomes maximum i.e. >x then False
# if abs(arr[i][j]-parent(previous cell))>x (obtained current diff) then return False. As we need only minimum difference between consecutive cells.
# continuosly checking of position of current cell, where top, bottom, right and left side.
import sys
# m,n=0,0
def is_valid(i,j,x,visited,arr,parent):
    # m number of rows
    # n number of columns 
    m=len(arr)
    n=len(arr[0])
    if(i<0 or j<0 or i>=m or j>=n or visited[i][j] or abs(arr[i][j]- parent)>x):
        return False 
    if i==m-1 and j==n-1:
        return True

    visited[i][j]=True #make sure current visited node is true
    #now need to check on four sides whether current cell has valid move. 
    if (is_valid(i+1,j,x,visited,arr,arr[i][j])):
        return True 
    if (is_valid(i-1,j,x,visited,arr,arr[i][j])):
        return True
    if (is_valid(i,j+1,x,visited,arr,arr[i][j])):
        return True 
    if (is_valid(i,j-1,x,visited,arr,arr[i][j])):
        return True 
    return False 
def minimum_energy(arr):
    # need to find the step where absolute difference between consecutive cells should be less as long as reaches the end of path.
    start=0
    end= 100000 #sys.maxsize # or int('inf or infinity')
    result=arr[0][0]
    m=len(arr)
    n=len(arr[0])
    while start<=end:
        mid=(start+end)//2
        # visited,i, j
        visited=[[False for j in range(n)] for j in range(m)]

        if (is_valid(0,0,mid,visited,arr,arr[0][0])):
            result=mid 
            end=mid-1
        else:
            start=mid+1
    return result 
arr=[[1,2,1],[2,8,2],[2,4,2]]
# m=len(arr)
# n=len(arr[0])
print(minimum_energy(arr))

        







