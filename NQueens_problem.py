# N-queens problem.
# approach is using backtracking, how many ways we can places the queens without any interaction with next or previous queens.
# queens can move left to right columnwise. Need a isSafe function to check if any other queen not placed before and after the position of current queen in same row.
# and also need to check upper diagonal and lower diagonal of current queen. 
# if each time isSafe function satisfies then can place the queens in safe places.
global n
n=8

def isSafe(board,row,col):
    # check if any queen already placed before and after.
    for i in range(col):
        if board[row][i]==1:return False
    for x,y in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[x][y]==1:
            return False 
    for x,y in zip(range(row,n), range(col,-1,-1)):
        if board[x][y]==1:
            return False
    return True
def NQueens(board,col):
    # first starts from each cell and move columnwise front and by taking each decision check whether it is safe or not then can move.
    # first need to mention base cases.
    n=len(board)
    if col>=n:
        return True 
    for i in range(n):
        if isSafe(board,i,col):
            # consider current cell and check is it worth of placing queen in current cell
            board[i][col]=1 
            # now before moving to next cell we can use recursion of current function.
            # at each move need to check whether the next step may be end of row.
            nextstep=NQueens(board,col+1)
            if nextstep==True:
                return True 
             # check for next cell if objection found or not safe to move then keep current cell queen 0 as previous.
            board[i][col]=0
    return False
def printsolution(board):
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                print('Q',end=' ')
            else:
                print('.',end=' ')
        print()
def nqueens():   
    board=[[0]*n for _ in range(n)]
    if NQueens(board,0):
        printsolution(board)
        return True 
    return False
if __name__=='__main__':
    nqueens()
