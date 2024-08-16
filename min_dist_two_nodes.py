# # # first need to find the lowes common ancsestor
# # # LCA is used to find for two nodes n1 and n2 which follows the approach
# # # first need to find the path from root to n1 and path from root to n2 in  different data structures.
# # # then start comparing simultenously whenever we got mismatch then need to print the parent which got matched.

class node:
    def __init__(self,data):
        self.data=data
        self.right=None 
        self.left=None 
# # # need to create two arrays one for root to n1 and root to n2.
# # # and then comparing both.
# # # LCA(5,6)
def findpath(root,path_arr,k):
    # k is required n1 or n2
    # need to create a function to search an element and append to the elements of that path from root to required element.

    if root is None:
        return False
    path_arr.append(root.data)

    if root.data==k:
        return True

    if (root.left is not None and findpath(root.left,path_arr,k)) or \
    (root.right is not None and findpath(root.right,path_arr,k)):
        return True
    # if desired root is not found or element is not present then remove root from path and return false
    path_arr.pop()
    return False

def LCA(root,n1,n2):
    # first need to find the position of n1.
    # and then traversing from root to n1 and storing those elements in arr1.
    path1=[]
    path2=[]

    if not findpath(root,path1,n1) or not findpath(root,path2,n2):
        return -1
    print(path1)
    print(path2)

    # if not path1 or not path2:
    #     return -1
    i=0
    while i<len(path1) and i<len(path2):
        if path1[i]!=path2[i]:
            break
        i=i+1 
    # whenever the two array values are mismatched then need to return parent matched node.
    return path1[i-1]
def find_paths(root,path,k):
    if root is None:
        return False 
    # we are finding the path so if we found the element in the route then return true 
    
    path.append(root.data)
    if root.data==k:
        return True 
    
    if (root.left is not None and find_paths(root.left,path,k)) or (root.right is not None and find_paths(root.right,path,k)):
        # if root.data==k:
            return True
    path.pop()
    return False

# def LCA(root,n1,n2):
#     # if root is None:
#     #     return False
#     path1=[]
#     path2=[]
    
#     if not find_paths(root,path1,n1) or not find_paths(root,path2,n2):
#         return -1
#     print(path1)
#     print(path2)
    
#     i=0
#     while i<len(path1) and i<len(path2):
#         if path1[i]==path2[i]:
#             i=i+1
#         if path1[i]!=path2[i]:
#             break 
#         i+=1
#     return path1[i-1]

root=node(1)
# root = Node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

print(LCA(root,5,6))


# # find lowest common ancsestor
# # need to find path of elements on finding path from root to elements.
# # lowest common ancestor is used to return when mismatched elements are founds in two routes and returns the parent ancestor which got common.
# # need to find the minimum distance between the two nodes.
# # formula - dist(root,n1) + dist(root,n2) - 2*lca(n1,n2)
# approach is - to find the distance between the two nodes need to find the path from root to n1 and root to n2.
# then find the minimum path between n1 and n2, that can be happen when sum of two nodes paths and differnce them with 2*lca(n1,n2)

def find_dist(root,arr,k):
    if root is None:
        return False 
    arr.append(root.data)
    if root.data==k:
        return True 
    if root.left is not None and find_dist(root.left,arr,k) or root.right is not None and find_dist(root.right,arr,k):
        return True
    # popping the root from arr if there is no expected element found.
    arr.pop() 
    return False

def min_dist(root,n1,n2):
    n1_path=[]
    n2_path=[]

    if not find_dist(root,n1_path,n1) or not find_dist(root,n2_path,n2):
        return 0
    print(n1_path)
    print(n2_path)
    i=0
    while i<len(n1_path) and i<len(n2_path):
        if n1_path[i]!=n2_path[i]:
            break
        i=i+1
    return (len(n1_path)+len(n2_path)-2*i)
root=node(1)
# root = Node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
root.right.left.right=node(8)
print(min_dist(root,4,5))
print(min_dist(root,4,8))

# need to find the maximum sum from leaf to root.
# check all possible routes from leaf to root and return the maximum sum.
# need to find path from root to each leaf node exist.

# find the maximum sum of each path from leaf to root.
# first need to find the route from root to each leaf and store their values.

def find_path(root,target_leaf):
    if root is None:
        return False
    if root==target_leaf or find_path(root.left,target_leaf) or find_path(root.right,target_leaf):
        print(root.data,end=' ')
        return True
    return False
max_sum=0
target_leaf=None
def find_max_sum(Node):
    curr_sum=0
    global max_sum
    global target_leaf
    if Node is None:
        return 0

    curr_sum=curr_sum+ Node.data
    # print(curr_sum)
    if root.left is None and root.right is None:
        # it means it reaches the leaf node.
        if curr_sum>max_sum:
            max_sum=curr_sum
            # print(max_sum)
            target_sum_ref=Node
            # also update the leaf node
    # if root left is not leaf node and root right also not None it have still node means 
    find_max_sum(Node.left)
    find_max_sum(Node.right)
    # return max_sum
# import sys
# def maxpath(root):
    
#     if root==None:
#         return 0
#     global target_leaf
#     global max_sum
#     target_leaf=None
#     max_sum=-32676
#     # max_sum=0
    
#     find_max_sum(root)
#     find_path(root,target_leaf)
#     return max_sum
    
    # arr.append(root.data)
    # if root.left or find_path(root.left,arr) and root.right \
    # or find_path(root.right,arr):
    #     return True 
    # if root:
    #    if root.left:
    #     print(root.data)
    #     root_traversal(root.left)
    # if root.left or root.right:
    #     left=root_traversal(root.left)
    #     right=root_traversal(root.right)
    #     if left is None and right is None:
    #         print(root.data)
            # print()
    # if root:
    #     if root.left:
    #         root_traversal(root.left)
    #         # print(root.data)
    #     # print(root.data)
    #     if root.right:
    #         root_traversal(root.right)
    #         # print(root.data)     
    #     # print(root.data)   
    # if root.left is None and root.right is None:
    #     print(root.data)
root=node(1)
# root = Node(1)
root=node(1)   
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
root.right.left.right=node(8)
# root_traversal(root)
# print(maxpath(root))













 


 