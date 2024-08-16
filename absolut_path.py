# find path from source to end having absolute minimum difference between consecutive cells.

# aim -  minimum number of jumps reaquired to reach the last index.
# in one jump i can move from current index i to index j.
# only if arr[i]=arr[j] and i!=j or i can jump (i+1) or (i-1)
# def minimize_jumps(arr):
#     map={}
# conditions -  we can move/jump only when arr[i]=arr[j] and i!=j
# or jump to (i+1) or (i-1).
    # map[arr[i]]=i

# need to construct a tree from inorder and preorder.
# construct the binary tree from the given inorder and preorder array 
# inorder contains left - root -  right
# preorder contains root - left - right
# traverse through pre-order collect the element and increment it.

class node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 

def construct_tree(inorder,preorder,inStart,inEnd):
    # need to take the element from the preorder, in the preorder the root follows on first node.
    # root-left-right.
    # pick the element from the preorder and find the index in the inorder.
    # divide the left and right from the picked element
    # preorder contains first element as root
    # it's way to find the element index in the inorder.
    if inStart>=inEnd:
        return None 
    # creating a new tree of tnode
    tnode=node(preorder[construct_tree.preindex])
    construct_tree.preindex+=1 
    if inStart==inEnd:
        return tnode
    # increment to the next element at each iteration.
    inIndex= search(inorder,inStart,inEnd,tnode.data)
    tnode.left=construct_tree(inorder,preorder,inStart,inIndex-1)
    tnode.right=construct_tree(inorder,preorder,inIndex+1,inEnd)
    return tnode
def search(arr,start,end,value):
    for i in range(start,end+1):
        if arr[i]==value:
            return i
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

preOrder=['D','B','E','A','F','C']
# static variable
construct_tree.preindex=0
inOrder=['A','B','D','E','C','F']
        #  left    root    right
inStart=0
inEnd=len(inOrder)-1
root=construct_tree(inOrder,preOrder,inStart,inEnd)
inorder(root)

##############################################################################

#CONSTRUCT A BST FROM preorder traversal
# in the preorder traversal, root contains in the first place.

def construct_tree(preorder):
    # if tnode is None:
    #     return tnode
    # first need to take first element and divide the elemens from that element.
    preIndex=0
    # tnode=node(preorder[construct_tree.preIndex])
    # construct_tree.preIndex=construct_tree.preIndex+1
    tnode=node(preorder[preIndex])
    # preIndex+=1
    print(tnode.data)
    tnode.left=[]
    tnode.right=[]
    for i in range(1,len(preorder)):
        if preorder[i]>tnode.data:
            tnode.right.append(preorder[i])
        if preorder[i]<tnode.data:
            tnode.left.append(preorder[i])
    return tnode.left + [tnode.data] + tnode.right
# def print_tree(root):
#     if root:
#         print_tree(root.left)
#         print(root.data,end=' ')
#         print_tree(root.right)
    # need to make sure all the elements less than root moving on left child
    # and greater than root moving on right child.
    # tnode.left= construct_tree(root.left,preorder,start,l_index-1)
    # tnode.right=construct_tree(root.right,)

# static variables
# construct_tree.preIndex=0
preorder=[10,5,1,7,40,50]

print(construct_tree(preorder))
# print_tree(root)
###############################################################

def construct_BST(preorder):
    if not preorder:
        return None 
    preIndex=0
    # create a utility function to construct a binary search tree.
    def construct_tree_util(preorder,low,high):
        # preIndex=0 
        nonlocal preIndex
        if preIndex>len(preorder) or preorder[preIndex]<low or preorder[preIndex]>high:
            return None 
        
        tnode=node(preorder[preIndex])
        preIndex=preIndex+1 

        if preIndex<len(preorder):
            tnode.left=construct_tree_util(preorder,low,tnode.data)
            tnode.right=construct_tree_util(preorder,tnode.data,high)
        return tnode
    return construct_tree_util(preorder,-float('inf'),float('inf'))
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.data,end=' ')
        print_tree(root.right)
preorder=[10,5,1,7,40,50]
root=construct_BST(preorder)
print_tree(root)


#############################################################
# construct a binary tree from parent array representation.

# print ancsestors of binary tree 
class node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 
def print_ancsestors(root,target):
    if root is None:
        return False 
    
    if root.data==target:
        return True 
    if print_ancsestors(root.left,target) or print_ancsestors(root.right,target):
        print(root.data,end=' ')
        return True
    return False

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
print_ancsestors(root,4)
####################################################################
# check if given tree is sum tree
# root.data==sum(root.left) + sum(root.right)
def sum(root):
    if root is None:
        return False 
    return sum(root.left) + root.data + sum(root.right)
def issumtree(root):
    if root==None:
        return 0 
    if root==None or (root.left==None and root.right==None):
        return 1
    ls=sum(root.left)
    rs=sum(root.right)

    if root.data==(ls+rs) and issumtree(root.left) and issumtree(root.right):
        return 1
    return 0

# aim to find whether the tree is sumtree or not 
# if root.data== sum of all child nodes then sumtree simple logic
def isleaf(root):
    if root is None:
        return False 
    if root.left is None and root.right is None:
        return True 
    return False
def issumtree(root):
    if root==None:
        return -1
    # need to track the left and right subtrees.
    # if issumtree(root.left) is None:
    #     ls=0
    # else:
    #     ls=issumtree(root.left)
    ls=issumtree(root.left)
    if ls==-1:
        return -1
    rs=issumtree(root.right)
    if rs==-1:
        return -1
    
    if root.data==(ls+rs) or isleaf(root):
        return ls+rs+root.data
    
    return -1


    # if root:
    # q.append(root.data)
    #     if root.left: 
    #         print(root.left.data)
    #         # sum=sum+q.append(root.left.data)
    #         # issumtree(root.left)
    #     if root.right:
    #         print(root.right.data)
    #         issumtree(root.right)
    #         # sum=sum+q.append(root.data)
    # return issumtree(root.left) + issumtree(root.right)
    # issumtree(root.left)
    # issumtree(root.right)
    # if root.left is None and root.right is None:
    #     return sum 

root=node(26)
root.left=node(10)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(6)
# root.right.left=node(6)
root.right.right=node(3) 
res=issumtree(root)
if res:
    print('tree is sum tree')
else:
    print('not sumtree')


