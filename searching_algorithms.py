# rabin-karp algorithm for pattern matching
# aim is to check the pattern present in text.
def findpattern(text,pattern):
    m=len(pattern)
    n=len(text)
    for i in range(n-m+1):
        j=0 
        # i increments whenever only j reaches end of pattern.
        # need to search individually again.
        # need to find the pattern in the text until then increment pointer.
        while j<m and pattern[j]==text[i+j]:
            j=j+1 
        if j==m:
            print(i)
    
text='AABAACAADAABAABA'
pattern='AABA'
findpattern(text,pattern)

##############################################################

# create a adjacency matrix of graph 
# aim is create a matrix rows and columns mark vertex position where vertex contains weight.
# takes directed graph and need to make adjacent matrix.
def adj_matrix(graph):
    vertices=sorted(graph.keys())
    print(vertices)
    num_vertices=len(vertices)
    # need to return the output as adjacent matrix
    adj_matrix= [[0]*num_vertices for _ in range(num_vertices)]
    # adj_matrix=[[0] for j in range(num_vertices) for i in range(num_vertices)]
    for i,vertex in enumerate(vertices):
        for neigbhors in graph[vertex]:
            j=vertices.index(neigbhors)
            adj_matrix[i][j]=1 
    return adj_matrix        
graph={
    '1':['2'],
    '2':['3'],
    '3':['2','4'],
    '4':['1','2']
}
print(adj_matrix(graph))


# print adjacency matrix from the graph with vertices and edges.
# containing the directed graph need to mark the 1 wherever vertex points in the graph.
def adj_graph(graph):
    vertices=sorted(graph.keys())
    print(vertices)
    num_vertices=len(vertices)

    adj_matrix=[[0 for j in range(num_vertices)]for i in range(num_vertices)]
    for i,vertex_ele in enumerate(vertices):
        for neighbors in graph[vertex_ele]:
            j=vertices.index(neighbors)
            # j traverse through each vertex.
            adj_matrix[i][j]=1 
    # print()
    return adj_matrix
    # print()

graph={
    'A':['B','C'],
    'B':['C','D'],
    'C':['A','D'],
    'D':['C','E'],
    'E':['A']
}
print(adj_graph(graph))

# greatest common difference of two numbers 
# a=20,b=28
# (20,28)
# (20,8)
# (12,8)
# (8,8)

# (20,28)
# (20,8)
# (12,8)
# (4,8)
# (4,4)
def gcd(a,b):
    if a is None:
        return b 
    if b is None:
        return a 
    if a==b:
        return a 
    if a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)
a=20
b=28
print(gcd(a,b))

# def gcd(a,b):
#     # (20,28)

#     # (0,8) here mod not eqauls to 0
#     res=min(a,b)
#     while res:
#         if a%res==0 and b%res==0:
#             break 
#         res=res-1
#     return res
# a=20
# b=28
# print(gcd(a,b))
# a.r**n-1
# arthimetic progression, geometric progression -- a(r^n-1)/[1-r]

# 2 if num%2==0 or 
# 11 is prime
# def check_prime(num):
#     if num>1:
#         for i in range(2,num//2+1):
#             if num%i==0:
#                 break
#         print(num, 'is prime')
#     else:
#         print(num,' is not prime')
#                 # print(num,' is prime')
#             # print(num,' is not prime')               
#                 # print(num,' is prime number')
#         #         break 
#         #     print(num, ' is not prime number')
#         # else:
#         #     print(num,' is prime number')
# num=29
# check_prime(num)

# shortest path from source to destination.
# aim is to find the shortest path from custom source to destination of i vertex to j vertex.
# approach - need to create an distance arr to count the distance on visiting at each vertex and parent arr to store the parent of each node visited as neighbor.
# using bfs starts the source node with dist 0 and append the source vertex to the visited queue.
# then pop that visited then find it neighbors and add the popped node as parent to the neighbors in the parent array.
# then after make dist arr of neighbor from source node increments by one.
# at each iteration vertices stores the corresponding neighbors and find distance.
# Now final method to initialize the distance arr which stores the distance between s to d and parent arr  which stores the parent nodes of each visited.
# and then call the bfs method.
# now initalize one path arr, consider d as current node and start with appending destination node d.
# now iterates while loop until it iterates back upto -1, append parent of current node to the path and make current node as that parent of current node.
# from queue import deque
def bfs(graph,s,par,dist):
    # q=deque()
    q=[]
    dist[s]=0 #initialised distance with 0
    q.append(s)
    while q:
        node=q.pop(0)
        for neighbors in graph[node]:
            # if neighbors not visited then make them visited add them to the q.
            # here distance measures the count, if not node reached before that represent it is in infinity.
            if dist[neighbors]==float('inf'):
                par[neighbors]=node 

                dist[neighbors]=dist[node]+1 
                q.append(neighbors)
    # return q
def printshortestpath(graph,s,d,v):
    dist=[float('inf')]*v
    par=[-1]*v
    bfs(graph,s,par,dist)

    if dist[d]==float('inf'):
        print('path not found')
        return 
    path=[]
    current_node=d 
    path.append(d)
    while par[current_node]!=-1:
        path.append(par[current_node])
        # after appending curr node and make parent node of curr node as curr node until it reaches source.
        current_node=par[current_node]
    
    for i in range(len(path)-1,-1,-1):
        print(path[i],end='->')

if __name__=='__main__':
    v=8
    edges= [
        [0, 1], [1, 2], [0, 3], [3, 4],
        [4, 7], [3, 7], [6, 7], [4, 5],
        [4, 6], [5, 6]
    ]
    graph=[[] for _ in range(v)]

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    print(graph)
    printshortestpath(graph,0,7,v)

# find missing number in the array 
# total 
# (n+1)(n+2)/2-sum
def find_missing_number(arr):
    # consider one empty hashmap with all 0s 
    n=len(arr)
    temp=[0]*(n+1)
    # now need to fill the temp with 1 as per their positions.
    for i in range(n-1):
        temp[arr[i]]=1
    print(temp)
    for i in range(n+1):
        if temp[i]==0:
            ans=i
            # print(ans)
    return ans
arr=[1, 2, 4, 6, 3, 7, 8]
print(find_missing_number(arr))
# total-sum
def find_missing(arr):
    n=len(arr)
    total=(n+1)*(n+2)/2
    avg_sum=sum(arr)
    # for i in range(n):
    #     sum=sum+arr[i]
    res=total-avg_sum 
    return res 
arr=[1, 2, 4, 6, 3, 7, 8]
print(find_missing(arr))
#################################################################################

def buy_and_sell(arr):
    # first buy at particular day at less cost and sell it on profit day within near days.
    # first while loop to find the lowest price to buy the stock.
    i=0
    day_buy=0
    day_sell=0
    total=0
    n=len(arr)
    # check if i+1<i, iF arr[i+1]<arr[i] then make lesser price as i+1 or while  arr[i+1]>arr[i] break.
    # here we need lower day value we need to stop the pointer where lesser value found, we need to ignore or break wherever next value becoming bigger.
    # if arr[i+1]>arr[i] means no use of moving forward until we need i+2, i+3.. will have lesser value than i, then only change the pointer to that next lowest value.
    #here comparing with next day price so i+1 will reach the end of arr first so i need to stop at n-1 only.
    while i<n-1:
        while i<n-1 and arr[i]>=arr[i+1]:
            i=i+1
        # if i is lower then buy=i 
        if i==n-1:
            break 
        buy=i 
        day_buy=day_buy+arr[i]

        # now need to start for selling day with profit day.
        # starts i iteration from next value onwards.
        i=i+1
        # now comparing with previous value.
        while i<n and arr[i]>arr[i-1]:
            i=i+1 
        sell=i-1 
        day_sell+=arr[i-1]

        print('buy stocks on day:', buy)
        print('sell stocks on day:',sell)
    total=max(total,(day_sell-day_buy))
    return total

arr=[100, 180, 260, 310, 40, 535, 695]
print(buy_and_sell(arr))
#########################################################

# rain water trapping problem.
# need to find the number of units can fill between the heights of buildings.
def rain_water_trapping(arr):
    # first consider the two pointers first they finds the maximum
    #height on left and maximum height on right then substracting middle
    # heights in total units count. whenever comparing both heights minimum height's matters more.
    n=len(arr)
    res=0
    # left max and right max need to find 
    for i in range(n-1):
        left=arr[i]
        for j in range(i):
            # upto i left part and i+1 considers as right part 
            left=max(left,arr[j])
            # finding max element on left part 
        right=arr[i]
        for j in range(i+1,n):
            right=max(right,arr[j])

        res=res+ min(left,right)-arr[i]
    return res 
arr=[3,0,2,0,4,0,2]
print(rain_water_trapping(arr))
################################################################################
# approach is finding maximum of left part upto current value and
def rain_water_trapping(heights):
    n=len(heights)
    res=0
    # find left max and right max, here the approach is need to find the max heights from each height of building and selecting minimum
    # from both heights and then remove the remaining middle heights.
    for i in range(n-1):
        left=arr[i]
        for j in range(i):
            left=max(left,arr[j])
        right=arr[i]
        for j in range(i+1,n):
            right=max(right,arr[j])
        res=res+ min(left,right)-arr[i]
    return res 
arr=[0, 1, 0, 2, 1, 0,
           1, 3, 2, 1, 2, 1]
print(rain_water_trapping(arr))

# #         |
# # |       |
# # |       |   |
# # |  |    |   |
# # 3 0 1 0 4 0 2
# arr=[3, 0, 1, 0, 4, 0, 2]
#######################################################################################
# def sort_elements(arr1,arr2,res):
    # need to merge the two sorted arrays and find kth element.
    # half=len(arr1)+len(arr2)//2
    # l=0, r=len(arr1)
    # midofarr1= l+r/2
    # midofarr2=half-midofarr1-2 mid of arr2
    # for i in range(len(arr1)):
    #     for j in range(len(arr2)):
    #         if arr1[i]<=arr2[j]:
    #             res.append(arr1[i])
    #         else:

#     l=len(arr1)
#     r=len(arr2)
#     i=0
#     j=0
#     # res=[]
#     while i<l and j<r:
#         if arr1[i]<=arr2[j]:
#             res.append(arr1[i])
#             i=i+1 
#         else:
#             res.append(arr2[j])
#             j=j+1 

#         # l=l+1
#         # r=r-1
#     # if arr1:
#     #     res.append()
#     while i<l:
#         res.append(arr1[i])
#         i=i+1
#     while j<r:
#         res.append(arr2[j])
#         j=j+1 
#     print(res)
#     return res
# def find_kth_ele(k):
#     res=[]
#     sort_elements(arr1,arr2,res)
#     for i in range(len(res)):
#         if i==k-1:
#             print(res[i])
# arr1=[2, 3, 6, 7, 9]
# arr2=[1, 4, 8, 10]
# k=5
# find_kth_ele(5)

# largest number formed from an array.
# def findlargestnumber(arr):
arr=[54, 546, 548, 60]
# '54546'
# 54860,60548 

# '54654'
for i in range(len(arr)):
    arr[i]=str(arr[i])
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]+arr[i]>arr[i]+arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
res=''.join(arr)
print(res)








