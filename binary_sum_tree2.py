class node:
    def __init__(self,data):
        self.data=data
        self.right=None 
        self.left=None 
def size_of_tree(root):
    # size=1 #it includes root node within it
    if root is None:
        return 0
    # left=size_of_tree(root.left)
    # right=size_of_tree(root.right)
    queue=[]
    queue.append(root)
    size=1
    while queue:
        # temp=queue[0]
        temp=queue.pop(0)
        # print(temp.data,end=' ')

        if temp.left:
            queue.append(temp.left)
            size=size+1
        if temp.right:
            queue.append(temp.right)
            size=size+1
        # size+=1
    return size
# another method to find size
def tree_size(root):
    if root is None:
        return 0
    return tree_size(root.left) + 1 + tree_size(root.right)

def sum(root):
    if root is None:
        return 0
    return sum(root.left) + root.data + sum(root.right)
def is_sum_tree(root):
    if root==None or (root.left==None and root.right==None):
        return True 
    ls=sum(root.left)
    rs=sum(root.right)

    if (root.data==(ls+rs) and is_sum_tree(root.left) and is_sum_tree(root.right)):
        return True 
    return False 
def print_tree(root):
    if root is None:
        return #when it reaches all the nodes then return 
    print(root.data,end=' ')
    print_tree(root.left)
    print_tree(root.right)
root=node(39)
root.left=node(3)
root.right=node(10)
root.left.left=node(1)
root.left.right=node(4)
root.right.left=node(7)
root.right.right=node(14)
print_tree(root)
print()
# # res=is_sum_tree(root)
# # print("Is Given a sumtree?",res)
size_of_tree(root)
print(tree_size(root))



# convert linkedlist into binary tree
# aim-- the linked list contain head, the first node of linkedlist is to be root of binary tree
# the remaining elements are the left and right subtrees.
# next two elements of head in linked list are childrens of root.
# so need to make them left child and right child of root.
# at each iteration while head.next is not None
# This procedure follows with parent and child nodes

# approach: Need to create two classes one for linked list node insertion and traversal.
# another class for binary tree node.
class node:
    def __init__(self,data):
        self.data=data
        self.next=None 
class binary_node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
class convertlist2binarytree:
    def __init__(self):
        self.head=None #for linked list traversal
        self.root=None #binary tree traversal
    #creation of linked list
    def insert(self,data):
        new_node=node(data)
        new_node.next=self.head 
        self.head=new_node 
    def convert(self):
        if self.head is None:
            self.root=None 
            return
        self.root=binary_node(self.head.data)
        #first node in linked list always a root node of tree.
        #now need to traverse to next every two nodes to make them as left and right childs.
        #now head starts from second node of linked list. head shifts to next node.
        self.head=self.head.next #next of root node/first node 
        q=[]
        q.append(self.root)
        while self.head:
            parent=q.pop(0)
            #now need to make left and right child
            leftchild=None 
            rightchild=None
            leftchild=binary_node(self.head.data)
            q.append(leftchild)
            self.head=self.head.next 
            if self.head:
                # q.append(self.head)
                rightchild=binary_node(self.head.data)
                q.append(rightchild)
                self.head=self.head.next
            parent.left=leftchild
            parent.right=rightchild
    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data,end=' ')
            self.inorder_traversal(root.right)
t=convertlist2binarytree()
t.insert(10)
t.insert(7)
t.insert(12)
t.insert(5)
t.insert(11)
t.insert(10)
t.insert(17)
t.convert()
t.inorder_traversal(t.root)

# convert the binary tree into binary search tree
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
# to convert the binary tree into binary search tree need to construct the tree 
# and applying binary search tree rules.
# convert the bin
def inorder_traversal(root,arr):
    # this function used to follow the tree from left to right
    # and insert the any new value at the root and then compared with other elements.
    # nodes is an array 
    if root:
        inorder_traversal(root.left,arr)
        arr.append(root)
        inorder_traversal(root.right,arr)

def construct_tree(arr,start,end):
    if start<end:
        mid=(start+end)//2
        root=arr[mid]
        root.left=construct_tree(arr,0,mid-1)
        root.right=construct_tree(arr,mid+1,len(arr)-1)
        return root
def convert_to_BST(root):
    arr=[]
    inorder_traversal(root,arr)
    arr.sort(key=lambda node:node.val)
    return construct_tree(arr,0,len(arr)-1)
# to convert the binary tree into binary search tree, it needs the inorder traversal of elements.
# firstly converting array into binary search tree and making order traversal where left, root and right
# if any new element is inserting then it appends to root and compared to another nodes.
# approach- array arr[] where values are appended in inorder format root at middle.
# after every insertion of element sort the arr[].
# then construct the binary search tree where left elements and right elements are partitioned.
def inorder_traversal(root,arr):
    if root:
        inorder_traversal(root.left,arr)
        arr.append(root)
        inorder_traversal(root.right,arr)
def construct_bst(arr,start,end):
    # arr=[]
    # if start<end:
    if start>end:
        return 
    mid=(start+end)//2
    root=arr[mid]
    root.left=construct_bst(arr,start,mid-1)
    root.right=construct_bst(arr,mid+1,end)
    return root
def convert_to_bst(root):
    arr=[]
    # now follows the inorder traversal
    inorder_traversal(root,arr)
    arr.sort(key=lambda node:node.data)
    return construct_bst(arr,0,len(arr)-1)
def print_tree(root):
    if root is None:
        return 
    print_tree(root.left)
    print(root.data,end=' ')
    print_tree(root.right)

root=node(10)
root.left=node(6)
root.right=node(12)
root.left.left=node(4)
root.left.right=node(8)
root.right.left=node(3)
root.right.right=node(20)
res=convert_to_bst(root)
print_tree(res)


