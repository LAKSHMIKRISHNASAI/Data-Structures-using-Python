class Node:
    def __init__(self,data):
        self.data=data 
        self.left=self.right=None 
def height_of_tree(root,ans):
    if root is None:
        return 0
#     # diameter is the longest path between two leaf nodes.
#     # max left + max right path + root(1)
#     if root is None:
#         return 0
    # return 1+max(hieght_of_tree(root.left),hieght_of_tree(root.right))
    lh=height_of_tree(root.left,ans)
    rh=height_of_tree(root.right,ans)
    # return 1+max(lh,rh)
    # ans will store possibility
    ans[0]=max(ans[0],1+lh+rh)
    return 1+max(lh,rh)
def diameter(root):
    if root is None:
        return 0 
    ans=[float('-inf')]
    height=height_of_tree(root,ans)
    return max(ans[0],height)


def diameteroftree(root):
    if root is None: return 0

    lh=height_of_tree(root.left)
    rh=height_of_tree(root.right)

    dl=diameteroftree(root.left)
    dr=diameteroftree(root.right)
    return max(1+lh+rh,max(dl,dr))


# find max sum path from leaf nodes.
# first find the route is path reaches leaf node, another method for sum all 
# maximum sum from leaf to root path.
# here approach is need to find the sum in all paths until it reaches leaf.
# all leaf paths are to be considered.
def findpath(root,target_leaf):
    if root is None:
        return False 
    if root==target_leaf or findpath(root.left,target_leaf) or findpath(root.right,target_leaf):
        # print(root.data,end=' ')
        return True 
    return False
max_sum=0
target_leafnode=None
def maxsum(root,currsum):
    global max_sum
    global target_leafnode
    if root is None:
        return 0
    currsum=currsum+root.data 
    if root.left is None and root.right is None:
        if currsum>max_sum:
            max_sum=currsum
            target_leafnode=root
    # if paths not reached leaf nodes then recur the down.
    maxsum(root.left,currsum)
    maxsum(root.right,currsum)
def final_path_sum(root):
    global max_sum
    global target_leafnode
    max_sum=float('-inf')
    target_leafnode=None 
    maxsum(root,0)
    findpath(root,target_leafnode)
    return max_sum


# find minimum distance between  the two nodes.
# approach is first find the lca and then sum the paths from lca node to two nodes.
# dist(root,n1) and dist(root,n2) - 2*dist(root,lca) --0
def find_path_to_node(root,path,target):
    # (5,4)
    # if root reaches the target print path, append nodes.
    if root is None:
        return False 
    path.append(root.data)
    if root.data==target:
        return True 
    if root.left and find_path_to_node(root.left,path,target) or root.right and find_path_to_node(root.right,path,target):
        return True 
    # if root doesn't find the path remove the root.
    path.pop()
    return False
def min_dist(root,n1,n2):
    # first find the lca of two nodes. find the paths and minimum distance b/w two nodes.
    if root is None:
        return 0 
    path1=[]
    find_path_to_node(root,path1,n1)
    path2=[]
    find_path_to_node(root,path2,n2)
    print(path1)
    print(path2)
    i=0
    # j=0
    while i<len(path1) and i<len(path2):
        if path1[i]!=path2[i]:
            break
        i=i+1
        # j=j+1 
    return len(path1)+len(path2)-2*i
# 3+3 - 2*1
# dist(root,n1), dist(root,n2)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right= Node(7)
root.right.left = Node(6)
root.left.right = Node(5)
root.right.left.right = Node(8)
print(min_dist(root,2,6))
print(height_of_tree(root))
print(diameter(root))
print(diameteroftree(root))


    # to find the diameter of tree max of left tree, max of right tree + 1 (for root)
    # 1+ maximum height of left+ maximum height of right 
    # 1+max(lh,rh)


####################################################################################################################
# in dropping puzzle the need to check two conditions if egg breaks at x floor then need to check down
# it would be x-1 floor and n-1 eggs
# if eggs not broken then can go to up floor to check, then eggs are n and floors k-x.
import sys
def isbrokenornot(n,k):
    
    if k==1 or k==0:
        return k 
    if n==1:
        return k 
    min=sys.maxsize
    for i in range(1,k+1):
        res=max(isbrokenornot(n-1,i-1),isbrokenornot(n,k-i))
        if res<min:
            min=res 
    return min+1 
print(isbrokenornot(2,15))

#################################################################################################################################

# longest palindromic substring
# s='forgeeksskeegfor'
# s='aaaabbaa'
# aab baa first and last should be same.



def longest_palindromic_substring(s):
    n=len(s)
    if n==0:
        return ''
    
    maxlength='' 
    start=0 

    for i in range(n):
        for j in range(i,n):
            substring=s[i:j+1]
            if substring==substring[::-1]:
                length=j-i+1
                if length>maxlength:
                    maxlength=length 
                    start=i 
    return s[start:start+maxlength]
    l-j+1
    def expand_around_center(s,i,j):
    # i=0 
    # j=len(s)-1
        while i<len(s) and j>=0 and s[i]==s[j]:
            i=i+1 
            j=j-1 
        return s[i:j+1]
    for i in range(len(s)):
        odd_palidrome=expand_around_center(s,i,i)
        if odd_palidrome>len(maxlength):
            maxlength=odd_palidrome
        even_palindrome=expand_around_center(s,i,i+1)
        if even_palindrome>len(maxlength):
            maxlength=even_palindrome
    return maxlength
    for i in range(n):
        for j in range(i,n):
            # this is not best approach 
            flag=1 
            for k in range((j-i)//2+1):
                if s[i+k]!=s[j-k]:
                    flag=0 
            if flag!=0 and j-i+1>maxlength:
                maxlength=j-i+1 
                start=i
            flag=1
            for k in range((j-i)//2+1):
                if s[i+k]!=s[j-k]:
                    flag=0 
            if flag!=0 and j-i+1>maxlength:
                maxlength=j-i+1 
                start=i
    return s[start:start+maxlength]

######################################################################################################
                
# lps using dp
def longest_palindromic_substring(s):
    table=[[0 for j in range(len(s))]for i in range(len(s))]

    # if len of s is 1 just return s, if length is 2  if both are same values then return max length is 2.
    # if s>2 then start checking for substring moving row pointer and col pointer [i+1][j-1] if substring matches 
    maxlength=1 
    n=len(s)
    i=0
    while i<n:
        table[i][i]=True 
        # maxlength=1
        i=i+1 
    # if len of s is 2
    start=0 
    i=0 
    while i<n-1:
        table[i][i+1]=True 
        maxlength=2 
     
s='aaabbaa'
print(longest_palindromic_substring(s))
