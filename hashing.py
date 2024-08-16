# find the largest subarray with equal number of 0's and 1's
# approach -  need to initialize one array/hash map, traverse through arr.
# check the even balanced of elements at each iteration and insertion.
# start max variable stores the max sub array.
# here approach is need to track the values and update everytime for each max subarray
# if any new sub array in future takes place then need to update that index length.

def largestsubarr(arr):
    # mp={}
    n=len(arr)
    mp={}
    max_len=0
    end_index=-1
    currsum=0
    for i in range(n):
        if arr[i]==0:
            arr[i]=-1
        else:
            arr[i]=1
    for i in range(n):
        currsum=currsum+arr[i]
        if currsum==0:
            max_len=i+1 
            end_index=i
        # this next step for future sub array if get currsum=0 then compare it with current array
        if currsum in mp:
            if max_len<i-mp[currsum]:
                max_len=i-mp[currsum] 
                end_index=i 
            else:
                mp[currsum]=i
    print(mp)
    print(end_index-max_len+1)
    return max_len

    print(mp)
    # if mp[arr]
    # if max_len< new sub arr then update that len and index
    # max_len=i+1 
arr=[1, 0, 1, 1, 1, 0, 0]
print(largestsubarr(arr))
#################################################################
class node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
class bst:
    def __init__(self):
        self.root=None 
    def insert(self,root,data):
        if root is None:
            return node(data)
        if data<root.data:
            root.left=self.insert(root.left,data)
        elif data>root.data:
            root.right=self.insert(root.right,data)
        return root 
    def delete_node(self,root,data):
        if root is None:
            return root
        if data<root.data:
            root.left=self.delete_node(root.left,data)
        elif data>root.data:
            root.right=self.delete_node(root.right,data)
        else:
            # if it has single children nodes then check for left and right nodes
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # if node has two child nodes then need to delete the node according the inorder successor.
            # if need to delete in right tree then find minimum value in the right subtree to delete.
            root.data=self.minval(root.right)
            root.right=self.delete_node(root.right,root.data)
        return root
    def minval(self,root):
        min=root.data
        while root.left:
            min=root.left.data
            root=root.left 
        return min

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
        # print()      
t=bst()
t.root=t.insert(t.root,20)
t.insert(t.root,12)
t.insert(t.root,25)
t.insert(t.root,2)
t.insert(t.root,14)
t.insert(t.root,32)
t.inorder(t.root)
print()
t.root=t.delete_node(t.root,14)
t.inorder(t.root)


# bst to min-heap 
# root should be minimum(lesser) than left and right child nodes.
# find the second largest element in binary search tree
def inorder(root,arr):
    inorder(root.left)
    arr.append(root.data)
    inorder(root.right)
def secondlargestutil(root,c):
    if root==None or c[0]>=2:
        return 
    # traverse through right subtree from root to find second largest element.
    secondlargestutil(root.right,c)
    c[0]=c[0]+1
    if c[0]==2:
        print(root.data)
        return 
    secondlargestutil(root.left,c)
def secondlargest(root,c):
    arr=[]
    c=[0]
    # inorder(root,arr)
    secondlargest(root,c)
    
# find the sum of k number of smallest elements in the tree
def findsmallestkutil(root,k,c):
    if root is None:
        return 0
    if c[0]>k[0]:
        return 0
    res=findsmallestkutil(root.left,k,c)
    # c[0]=c[0]+1 
    res=res+root.data
    c[0]=c[0]+1 
    if c[0]>=k[0]:
        return res 
    # if left tree not reached k go right
    return res+findsmallestkutil(root.right,k,c)
def findsmallestk(root,k):
    c=[0]
    return findsmallestk(root,c,k)


# ############################################################
# kth largest element in the bst.
# traverse the tree in reverse inorder traversal, then order changes to decreasing order.
# while doing the traversal keeping the track on count of nodes.
# if count reaches the k then stop and print the key.
def inorderrev(root):
    if root:
        inorderrev(root.right)
        print(root.data,end=' ')
        inorderrev(root.left)
def kthlargestutil(root,k,count):
    # count=0
    if root is None or count[0]>=k:
        return 
    kthlargestutil(root.right,k,count)
    count[0]=count[0]+1
    if count[0]==k:
        print(root.data)
        return
    kthlargestutil(root.left,k,count)
def klargest(root,k):
    count=[0] #visited node marked with [0]
    kthlargestutil(root,k,count)

def insert(root,data):
    if root is None:
        return node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    if data>root.data:
        root.right=insert(root.right,data)
    return root 
def minimum(root,arr):
    if not root:
        return
    # minimum value found in left sub tree then need to check on right.
    minimum(root.left,arr) #recursively traversing through left subtree and appending values into the array
    arr.append(root.data)

    # if not found in left then check right at last.
    minimum(root.right,arr) 

def minval(root):
    if root is None:
        return 
    # first need to check left subtree to find smallest
    minval=root.data
    while root.left:
        minval=root.left.data 
        root=root.left 
    return minval

root=None
root =insert(root, 50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)
klargest(root,3)
arr=[]
minimum(root,arr)
print(arr[0])
print(minval(root))


###############################################################
# check if a binary tree is heap
# approach - first need to check method of isheap() satisfying heap properties.
# then next iscompletetree() util, if both are satisfied then it considered as binary tree in heap property.

def count_nodes(root):
    if root is None:
        return 0 
    # 1 for considering root node
    return 1+count_nodes(root.left) + count_nodes(root.right)


def isheap(root):
    # if root is None:
    #     return 
    if root.left is None and root.right is None:
        return True
    if root.right is None:
        return root.data>=root.left.data 
    else:
        if root.data>=root.left.data and root.data>=root.right.data:
            return (isheap(root.left) and isheap(root.right))
        else:
            return False 
def iscompletetree(root,index,node_count):
    if root is None:
        return 
    # complete tree means having both left and right childs
    # and need to check whether index not extending total node counts
    if index>node_count:
        return False 
    return iscompletetree(root.left,2*index+1,node_count) and iscompletetree(root.right,2*index+2,node_count)
def check_if_heap(root):
    node_count=count_nodes(root)
    if isheap(root) and iscompletetree(root,0,node_count):
        return True 
    return False


        
