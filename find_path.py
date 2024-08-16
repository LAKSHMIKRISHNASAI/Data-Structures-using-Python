# # find the path from source to destination, where 1 denotes source
# # 2- destination, 3-blank cell to move, 0-blank/empty wall cannot access.

# # approach is making visited matrix and flag true/false.
# # first find the source cell in the given matrix, once soruce found then check is it safe to move and up/down/right/left.
# # if any of the recrusive function found the path destination then return true.
def issafe(matrix,i,j):
    if (i>=0 and i<len(matrix)) and (j>=0 and j<len(matrix[0])):
        return True 
    return False
def is_checkpath(matrix,i,j,visited):
    # from current cell need to check in four directions if next movement found destination then return true.
    if issafe(matrix,i,j) and matrix[i][j]!=0 and visited[i][j]==False:
        visited[i][j]=True
        if matrix[i][j]==2:
            return True 
        
        up=is_checkpath(matrix,i-1,j,visited)
        if up:
            return True
        down=is_checkpath(matrix,i+1,j, visited)
        if down:
            return True 
        left=is_checkpath(matrix,i,j-1,visited)
        if left:
            return True
         
        right=is_checkpath(matrix,i,j+1,visited)
        if right:
            return True 
    return False #if path not found
def ispath_exist(matrix,n):
    visited=[[False for j in range(n)]for i in range(n)]
    flag=False 

    # first need to find the source 1.
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==1 and not visited[i][j]:
                if is_checkpath(matrix,i,j,visited):
                    visited[i][j]=True 
                    flag=True
                    break 
                    # return True 
    if flag:
        print('path found')
    else:
        print('path not found')

matrix=[[0, 3, 0, 1],
              [3, 0, 3, 3],
              [2, 3, 3, 3],
              [0, 3, 3, 3]]
ispath_exist(matrix,4)

#################################################################
# jump of knight
# minimum steps needed to jump from one position to target position.
# approach is finding distance to reach target cell using bfs.
# first consider the given soruce (r,c) -(i,j) append that to the queue,
# make two arrays of all possible 8 movements of knight combination with 1,2,-1,-2
# from the appended cell, pop each cell and check whether it is only destination cell. if it's target cell then return true
# if not, iterate in the loop within range of 8 possible movements if not visited yet.
# if move is resulting to make path to reach destination then add popped cell x vertex with dx an y vertex with dy. if it is safe to move and not visited then make visited true and append that result to the queue with increment of distance by 1.
# this will continue until queue is empty. 
class cell:
    def __init__(self,x=0,y=0,dist=0):
        self.x=x 
        self.y=y 
        self.dist=dist 

def issafe(x,y,n):
    if x>=0 and x<n and y>=0 and y<n:
        return True 
    return False 

def minstepToreachTarget(knightposition,targetposition,n):
    visited=[[False for j in range(n+1)]for i in range(n+1)]
    # 8 possible movements of knight
    # a knight can jump in total 8 possible ways with the combination of x and y as row and col.
    dx=[2,1,-2,2,1,-1,-1,-2]
    dy=[1,2,1,-1,-2,2,-2,-1]

    queue=[]
    queue.append(cell(knightposition[0],knightposition[1],0))
    visited[knightposition[0]][knightposition[1]]=True

    while queue:
        t=queue.pop(0)

        if t.x==targetposition[0] and t.y==targetposition[1]:
            return t.dist 
         
        for i in range(8):
            x=t.x+dx[i]
            y=t.y+dy[i]
            if issafe(x,y,n) and not visited[x][y]:
                visited[x][y]=True 
                queue.append(cell(x,y,t.dist+1))
    return t.dist
if __name__=='__main__':
    n=30 
    knightposition=[1,1]
    targetposition=[30,30]
    print(minstepToreachTarget(knightposition,targetposition,n))