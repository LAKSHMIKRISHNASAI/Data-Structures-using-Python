# longest common substring with dp.
# lcs(x,y,m,n)
# if character matches, 
# 1+max(lcs(x,y,m,n),lcs(x,y,m-1,n-1))
# if last character matches i.e. x[m-1]==y[n-1] then 1+lcs(x,y,m-1,n-1)

def lcs(x,y,m,n):
    result=0
    if len(x)==0 or len(y)==0:
        return 0 
    dp=[[0 for j in range(n+1)] for i in range(m+1)]
    # find longest common substring whenever two characters are matched
    # it will match with previous character.
    # whenever matches then increments the count.
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif x[i-1]==y[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
                result=max(result,dp[i][j])
            else:
                dp[i][j]=0
    return result

x='geeksforgeeks'
y='geeksor'
print(lcs(x,y,len(x),len(y)))

def LCS(m,n,count):
    # using recursion.
    # if matches then do recursion count+1.
    # res=0

    # recursion count if match characters.
    if m==0 or n==0:
        return count 
    if x[m-1]==y[n-1]:
        count= LCS(m-1,n-1,count+1)
    count=max(count,max(LCS(m-1,n,0),LCS(m,n-1,0)))
    return count
x='geeksforgeeks'
y='geeksor'
count=0
m=len(x)
n=len(y)
print(LCS(m,n,count))
    
########################################################################
# if s[l]==s[h] then find minimum insertions needed for s[l+1......h-1]
# else (s[l+1....h],s[l.......h-1]) +1 insertions.

# two approaches one is using recursion and another is tabulation.

def form_palindrome(s,l,r):
    # l and r are pointers 
    if l==r:
        return 0 
    if l==r-1:
        return 0 if s[l]==s[r] else 1
    elif s[l]==s[r]:
        return form_palindrome(s,l+1,r-1)
    else: 
        return min(form_palindrome(s,l+1,r),form_palindrome(s,l,r-1))+1
s='geeks'
print(form_palindrome(s,0,len(s)-1))
#############################################################
def form_palindrome(s):
    # if l==0 or r==0:
    #     return 0 
    table=[[0 for j in range(len(s))] for i in range(len(s))]
    for i in range(1,len(s)):
        l=0
        for j in range(i,len(s)):
            if s[l]==s[j]:
                table[l][j]=table[l+1][j-1]
            else: 
                table[l][j]=min(table[l+1][j],table[l][j-1])+1
            l=l+1
    return table[0][len(s)-1]
s='geeks'
print(form_palindrome(s))
########################################################
# find minimum heights of towers.
# given an array of elements containing heights of towers.
# given k integer which can increase or decrease the height of towers.
# need to find the minimum height difference from the shortest tower and longest tower after modifications.
# first lets make the mintemp and maxtemp
# first lets sort the array and where mintemp finds min(arr[0]+k,ARR[I]+k)
# maxtemp finds the maximum height by adding k value to the i-1 and subtracting with the n-1 
# after that store the elements and make difference and find final minimum.
def getmindiff(arr,n,k):
    arr.sort()
    ans=arr[n-1]-arr[0]
    temp_min=arr[0]
    temp_max=arr[n-1]
    for i in range(1,n):
        # if arr[i]<k:
        #     continue
        temp_min=min(arr[0]+k,arr[i]-k)

        temp_max=max(arr[i-1]+k,arr[n-1]-k)

        ans=min(ans,temp_max-temp_min)
    return ans
arr=[7, 4, 8, 8, 8, 9]
n=len(arr)
k=6 
print(getmindiff(arr,n,k))

###################################################################
# two approaches can do, one is using recursion.
# using recursion starting from end of cells destination cell (m,n)
# the cell can move back finding minimum of three sides up, left and diagonal from destination cell.
# min(mincost(m-1,n-1),mincost(m-1,n),min(m,n-1))+cost(m,n)
# if it reaches first cell (0,0) then return cost[m][n]
import sys
def find_mincost(m,n,cost):
    if m<0 or n<0:
        return sys.maxsize
    elif m==0 and n==0:
        return cost[m][n]
    else:
        return cost[m][n]+min(find_mincost(m-1,n-1,cost),
                                  find_mincost(m-1,n,cost),
                                  find_mincost(m,n-1,cost))
def min(x,y,z):
    if x<y:
        return x if x<z else z 
    else:
        return y if y<z else z
cost=[[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(find_mincost(2,2,cost))
# did using memoization.
def find_mincost(cost,m,n,dp):
    if m<0 or n<0:
        return sys.maxsize
    elif m==0 and n==0:
        return cost[m][n]
    if dp[m][n]!=-1:
        return dp[m][n]
    else:
        dp[m][n]=cost[m][n]+min(find_mincost(cost,m-1,n-1,dp),
                                find_mincost(cost,m-1,n,dp),
                                find_mincost(cost,m,n-1,dp))
    return dp[m][n]

if __name__=='__main__':
    c=3
    r=3
    dp=[[-1]*c for _ in range(r)]
    cost=[
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]
    print(find_mincost(cost,2,2,dp))
    
######################################################################################
# implement the queues using stacks
# need to show in fifo using LIFO.
# its one of the best approach is using two stacks, if one stack appends the value then all elements are popped out and appended to second stack.
# then after while inserting the next element all the elements are popped out from second stack and append that element to it then finally return the first stack.

class queue:
    def __init__(self):
        self.q1=[]
        self.q2=[]
    def enqeue(self,x):
        while len(self.q1)!=0:
            self.q2.append(self.q1[-1])
            self.q1.pop()
        self.q1.append(x)

        while len(self.q2)!=0:
            self.q1.append(self.q2[-1])
            self.q2.pop()
    def deqeue(self):
        if len(self.q1)==0:
            return -1 
        x=self.q1.pop(0)
        return x
q=queue()
q.enqeue(5)
q.enqeue(3)
q.enqeue(6)
q.enqeue(17)
q.enqeue(12)
q.enqeue(3)
q.enqeue(7)

print(q.deqeue())
print(q.deqeue())


# knight tour problem.
# approach is need to find the minimum number of steps needed to visit all positions in chessboard.
# a knight can move in 8 positions.

# class cell:
# n=8
def isSafe(i,j,board):
    if i>=0 and i<n and j>=0 and j<n and board[i][j]==-1:
        return True 
    return False 
# total 64 cells need to return 64 
# position counter starts wit 1 of 1st cell.
# curr_x_move,curr_y_move,x_moves,y_moves,pos


def printSolution(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=' ')
        print()
def find_minimum_moves(n):
    board=[[-1 for _ in range(n)] for _ in range(n)]

    board[0][0]=0 
    pos=1
    move_x=[2,1,2,-2,-2,-1,1,-1]
    move_y=[1,2,-1,1,-1,-2,-2,2]

    if (not knight_util(board,0,0,move_x,move_y,pos,n)):
        print('solution not found')
    printSolution(board,n)
def knight_util(board,curr_x,curr_y,move_x,move_y,pos,n):
    if pos==n**2:
        return True 
    
    for i in range(8):
        new_x=curr_x+move_x[i]
        new_y=curr_y+move_y[i]
        
        if isSafe(new_x,new_y,board):
            board[new_x][new_y]=pos
            if knight_util(board,new_x,new_y,move_x,move_y,pos+1,n):
                return True 
            board[new_x][new_y]=-1
    return False
if __name__=='__main__':
    find_minimum_moves(n)

###############################################################################################
# find minimum distance between two words.

def find_min_distance(s):
    dist1=-1
    dist2=-1
    for i in range(len(s)):
        if s[i]==s1:
            dist1=i 
        if s[i]==s2:
            dist2=i 
    return dist2-dist1
s1='the'
s2='fox'
s=["the", 'quick', 'brown', 'fox', 'quick']
print(find_min_distance(s))
######################################################

# equilibrium point 
# logic- need to find the middle 
# consider firt value , and last element
# another approach to find equilibrium.
def find_equilibrium(arr):

    for i in range(len(arr)):
        leftsum=sum(arr[:i])
        rightsum=sum(arr[i+1:])
        if leftsum==rightsum:
            return i+1 
    return -1 
arr=[-7, 1, 5, 2, -4, 3, 0]
print(find_equilibrium(arr))
################################################################################################### 
# find the level of nodes.
# count when it reaches to next level.

