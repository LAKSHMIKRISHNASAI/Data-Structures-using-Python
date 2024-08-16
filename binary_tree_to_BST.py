class node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 
# approach - used to create array
def sorted_inorder(root,arr):
    if root:
        sorted_inorder(root.left,arr)
        arr.append(root.data)
        sorted_inorder(root.right,arr)

def count_nodes(root):
    if root is None:
        return 0 
    return count_nodes(root.left) + 1 + count_nodes(root.right)
# first need to convert array to binary search tree
# for every insertion of node, it follows the left order, root and right order.
def convert_arr_to_bst(arr,root):
    if root is None:
        return 
    convert_arr_to_bst(arr,root.left)
    root.data=arr[0]
    arr.pop(0)
    convert_arr_to_bst(arr,root.right)
def bst(root):
    if root is None:
        return
    n=count_nodes(root)
    arr=[]
    sorted_inorder(root,arr)
    arr.sort()
    convert_arr_to_bst(arr,root)
    # approach is to convey loeft to right traversal
def mirror_tree(root):
    if root is None:
        return 
    temp=root 
    mirror_tree(root.left)
    mirror_tree(root.right)

    temp=root.left
    root.left=root.right
    root.right=temp
    # root.right,root.left=root.left,root.right
    # mirror_tree(root.left)
    # mirror_tree(root.right)
def mirror(root):
    if root is None:
        return
    q=[]
    temp=root 
    q.append(root)
    while q:
        temp=q[0]
        q.pop(0)
        if temp.left and temp.right:
            temp.left,temp.right=temp.right,temp.left
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
def isMirror(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        if root1.data==root2.data:
            return (isMirror(root1.left,root1.right) and isMirror(root1.right,root2.left))
    return False
def isSymmetric(root):
    # checking is same tree is mirror itself
    return isMirror(root,root)
def ismirror(root):
    # if root is null then binary tree is symmetric
    if root is None:
        return True
    q=[]
    q.append(root.left)
    q.append(root.right)
    while q:
        # now popping the left and right nodes of root.
        # comparing whether both are images to each other or not
        node1=q.pop()#here right pops first
        node2=q.pop()# then left pops
        if not node1 and not node2:
            # if there is no nodes exist on both sides
            continue 
        if not node1 or not node2:
            return False 
        if node1.data!=node2.data:
            return False 
        q.append(node1.left)
        q.append(node2.right)
        q.append(node1.right)
        q.append(node2.left)
    return True
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data,end=" ")
    printInorder(root.right)

# another similar approach to find symmetric
# 
#if root1.data ==root2.data:
#   compare left tree of root1 with right tree of root2
# and right tree of root1 with left tree of root2
# if equal then true.
#   return ismirror(root1.left,root2.right) and ismirror(root1.right,root1.left)
from queue import Queue
def is_mirror(root):
    if root is None:
        return True
    q=Queue()
    q.put(root.left)
    q.put(root.right)
    while not q.empty():
        node1=q.get()
        node2=q.get()

        if node1 is None and node2 is None:
            continue
        if node1 is None or node2 is None:return False
        if node1.data!=node2.data:return False 
        q.put(node1.left)
        q.put(node2.right)
        q.put(node1.right)
        q.put(node2.left)
    return True 

# root=node(10)
# root.left=node(6)
# root.right=node(12)
# root.left.left=node(4)
# root.left.right=node(8)
# root.right.left=node(3)
# root.right.right=node(20)
root = node(1)
root.left = node(2)
root.right = node(2)
root.left.left = node(3)
root.left.right = node(4)
root.right.left = node(4)
root.right.right = node(3)
# bst(root)
# printInorder(root)
# print()
# mirror(root)
# printInorder(root)
# print()
if is_mirror(root)==True:
    print('symmetric')
else:
    print('not symmetric')

# mirror tree (inversion of binary tree)
# inverting the subtrees of left and right.
# temp=root.left 
# root.left=root.right
# root.right=temp


# compare two tree are symmetric or not 
# need to return true if two trees are mirrored each other else false.
# to check whether trees are mirrored or not, condition is mainly two root nodes should be equal
# the right subtree of right tree in mirror tree equals to left subtree of left tree in normal tree
# similarly the left subtree of right tree equals to right subtree of left tree should be mirror images.

  