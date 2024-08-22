# solving sudoko using backtracking 
# from 9*9 sudoko, there are nine 3*3 subgrids are contains
# with the help of partially filled numbers it can possible to fill entire sudoko with base cases.
# primarily need to focus on one subgrid to solve optimizely and then recursively can solve remaining subgrids.

# row=9, col=9 
# sub_row=9-6, row-row%3
global n
n=9 
def isSafe(grid,row,col,num):
    # need to check whether 
    for i in range(n):
        if grid[row][i]==num:
            return False 
    for i in range(n):
        if grid[i][col]==num:
            return False 
    # 3*3-- 1 to 9
    # subrow=row-row%3--->Eg:(3-3%3)=3, (4-4%3)=3, (5-5%3)=3,(6-6%3)=6, (7-7%3)=6
    # we need to check whether it is safe to keep in 3*3 subgrid.
    # this can be get finding starting position of each sub grid.
    # we need the sub grid of 3*3 so taking remainder of each row and col, then subtract from them.
    subrow=row-row%3
    subcol=col-col%3 
    for i in range(3):
        for j in range(3):
            if grid[i+subrow][j+subcol]==num:
                return False 
    return True 
    #we need to print 1 to 9 numbers at each subgrid,    

def solve_sudoko(grid,row,col):
    if row==n-1 and col==n:
        return True 
    if col==n:
        row=row+1 
        col=0 
    # suppose if already the next cell have number then need to skip that and move to next cell.
    if grid[row][col]>0:
        return solve_sudoko(grid,row,col+1)
        
    for num in range(1,10):
        if isSafe(grid,row,col,num):
            grid[row][col]=num 
            nextcell=solve_sudoko(grid,row,col+1)
            if nextcell==True:
                return True 
            # if current num is not suitable to place in that position then 
            # find for the another num.
        grid[row][col]=0 
    return False

def printsolution(grid):
    for i in range(n):
        for j in range(n):
            print(grid[i][j],end=' ')
        print()

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
if solve_sudoko(grid,0,0):
    printsolution(grid)
