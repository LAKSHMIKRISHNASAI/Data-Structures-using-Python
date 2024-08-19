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
