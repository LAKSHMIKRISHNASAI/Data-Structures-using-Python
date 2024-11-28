# find the connected cities.
# connected are {0:[],1:[2],2:[1,3],3:[2],4:[]}
def countClusters(matrix,n):
    connected_cities={i:[] for i in range(n)}
    visited=[False]*n
    clusters=0
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==1:
                connected_cities[i].append(j)
    print(connected_cities)
    
    def dfs(connected_components,i):
        visited[i]=True 
        for neighbors in connected_components[i]:
            if not visited[neighbors]:
                dfs(connected_components,neighbors)
    
    for i in range(n):
        if not visited[i]:
            clusters+=1
            dfs(connected_cities,i)
    return clusters
            
n=4
# matrix=[[0,0,0,0,0],
# [0,0,1,0,0],
# [0,1,0,1,0],
# [0,0,1,0,0],
# [0,0,0,0,0]]
matrix=[
[0,1,0,0],
[1,0,1,0],
[0,1,0,0],
[0,0,0,0]]
print(countClusters(matrix,n))
