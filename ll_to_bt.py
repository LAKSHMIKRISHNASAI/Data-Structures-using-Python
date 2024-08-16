# # aim is to convert linkedlist into a binary tree.
# # first need to make method for insertion of nodes in linkedlist, make a queue insert all the nodes in queue one after another.
# # while q is empty pop the element and check for next two elements if not none and append them. make left child and right child 
# # in left child insert next data and if next is not none insert that node as right child
# # here i-1//2 as root, 2*i+1 as left and 2*i+2 as right child.
class node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class tree_node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 

# tree node insertion
# another class
class conversion:
    def __init__(self,data=None):
        self.root=None 
        self.head=None 
    
    def push_node(self,data):
        newnode=node(data)
        newnode.next=self.head 
        self.head=newnode
    def conversion_ll_to_bt(self):
        if self.head is None:
            self.root=None 
            return 
        # now create an array consider first node as root and append a node into it.
        # pop each value from array and take next two elements as left and right childs 2*i+1 and 2*i+2
        q=[]
        self.root=tree_node(self.head.data)
        q.append(self.root)
        self.head=self.head.next
        while self.head:
            parent_node=q.pop(0)

            leftchild=None 
            rightchild=None 
            leftchild=tree_node(self.head.data)
            q.append(leftchild)
            self.head=self.head.next 
            # if next of self.head.next is not none then appending as right child.
            if self.head:
                rightchild=tree_node(self.head.data)
                q.append(rightchild)
                self.head=self.head.next 
            parent_node.left=leftchild
            parent_node.right=rightchild
        
    def print_tree(self,root):
        if root is None:
            return
        self.print_tree(root.left)
        print(root.data,end=' ')
        self.print_tree(root.right)
l=conversion()
l.push_node(10)
l.push_node(5)
l.push_node(20)
l.push_node(15)
l.push_node(7)
l.push_node(27)
l.push_node(17)
l.push_node(9)
l.conversion_ll_to_bt()
l.print_tree(l.root)

########################################################
class Node:
    def __init__(self,data):
        self.data=data 
        self.left=self.right=None 

# from the array need to create the tree.
# aim is need to create the tree, here first find the parent element and make left,right elements
def createnode(arr,created,root,i):
    if created[i] is not None:
        return 
    created[i]=node(i) 
    if created[arr[i]]==-1:
        root[0]=created[i]
    if created[arr[i]] is None:
        createnode(arr,created,root,arr[i])
    p=created[arr[i]]
    if p.left is None:
        p.left=created[i]
    else:
        p.right=created[i]

def create_tree(arr):
    n=len(arr)
    created=[None for _ in range(n+1)]
    root=[None]
    for i in range(n):
        createnode(arr,created,root,i)
    return root[0]
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.key,end=" ")
        inorder(root.right)
arr=[-1, 0, 0, 1, 1, 3, 5]
root=create_tree(arr)
inorder(root)


# construct tree from the given inorder and preorder traversal.
# simple approach in which in preorder traversal root node appears first from the we can recognize first value of preorder arr is the root of inorder arr.
# with this we can find the root first and then traverse through left and right childs of tree.
def construct_tree(inorder,preorder,start,end):
    if start>end:
        return  None 
    # preindex=0
    tnode=node(preorder[construct_tree.preindex])
    construct_tree.preindex=construct_tree.preindex+1
    if start==end:
        return tnode
    inIndex=search(inorder,start,end,tnode.data)
    print(inIndex)
    tnode.left=construct_tree(inorder,preorder,start,inIndex-1)
    tnode.right=construct_tree(inorder,preorder,inIndex+1,end)
    # first pick element from preorder and increase an index count.
    # create tnode with data as picked element.
    # pick element from preorder and search in inorder array 
    return tnode
def search(arr,start,end,value):
    for i in range(start,end+1):
        if arr[i]==value:
            return i
def printInorder(node):
    if node is None:
        return
     
    # first recur on left child
    printInorder(node.left)
     
    # then print the data of node
    print (node.data,end=' ')
 
    # now recur on right child
    printInorder(node.right)
     
# Driver program to test above function
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
construct_tree.preindex=0
root=construct_tree(inOrder,preOrder,0,len(inOrder)-1)
printInorder(root)


# construct a tree using inorder and preorder traversal.
def construct_tree(inorder,preorder,start,end):
    global mp 
    # first need to take first element from preorder and find it in inorder.
    curr=preorder[construct_tree.preindex]
    construct_tree.preindex+=1 
    tnode=node(curr)
    if start==end:
        return tnode 
    inIndex=mp[curr]
    tnode.left=construct_tree(inorder,preorder,start,inIndex-1)
    tnode.right=construct_tree(inorder,preorder,inIndex+1,end)
    return tnode

def buildtree(inn,pre):
    # global mp 
    # mp={}
    for i in range(len(inn)):
        mp[inn[i]]=i 
    # print(mp)
    return construct_tree(inn,pre,0,len(inn)-1)
def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
     
    print (node.data,end=' ')
    printInorder(node.right)
mp={}
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
# print(mp)
construct_tree.preindex=0
root=construct_tree(inOrder,preOrder,0,len(inOrder)-1)
printInorder(root)


################################################################################################
# find the maximum path sum between two leaves
# approach is to find the distance from root to left leaf nodes
# and from root to right leaf nodes.
# root to left
# INT_MIN=-2**32
def find_sum(root,max_sum):
    if root is None:
        return 0 
    # left_sum=0 
    # right_sum=0
    res=0
    if root.left==None and root.right==None:
        return root.data
    #####################################################################################
    rs=find_sum(root.right,max_sum)
    ls=find_sum(root.left,max_sum)
    if root.left and root.right:
        max_sum=max(max_sum[0],ls+rs+root.data)
        return max(ls,rs) + root.data
    if root.right is None:
        return ls+root.data
    else:
        return rs+root.data
def maxpathsum(root):
    max_sum=[float('-inf')]
    res1=find_sum(root,max_sum)
    if root.left and root.right:
        return max_sum[0]
    return max(max_sum[0],res1)

root=Node(-15)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(-8)
root.left.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
root.right.left = Node(3)
root.right.right = Node(9)
root.right.right.right = Node(0)
root.right.right.right.left = Node(4)
root.right.right.right.right = Node(-1)
root.right.right.right.right.left = Node(10)
print(maxpathsum(root))


