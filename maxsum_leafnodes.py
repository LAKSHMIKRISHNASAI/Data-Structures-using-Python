# quikcksort 
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left_arr=[x for x in arr[1:] if x<pivot]
    # print(left_arr)
    right_arr=[x for x in arr[1:] if x>=pivot]
    # print(right_arr)
    return quicksort(left_arr)+[pivot] + quicksort(right_arr)
arr=[12,3,14,7,23,17,8]
res=quicksort(arr)
print(res)

###########################################################################
class Node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 

def maxpath(root,maxsum):
    if root is None:
        return 0 
    
    ls=maxpath(root.left,maxsum)
    rs=maxpath(root.right,maxsum)
    if root.left is None and root.right is None:
        return root.data 
    if root.left is not None and root.right is not None:
        # having both left and right data of the tree nodes.
         #storing this result if needed 
        maxsum[0]=max(maxsum[0],ls+rs+root.data)
        return max(ls,rs) + root.data 
    if root.left is None:
        return rs+root.data
    else:
        return ls+root.data


def wrapfinalpath(root):
    maxsum=[float('-inf')]
    res=maxpath(root,maxsum)
    if root.left and root.right:
        return maxsum[0]
    return max(maxsum[0],res)

    # now possibilites of maximum sum would be from root to left or root to right along with root data is one
    # maximum of left+root+right is one possibility
    # creating a list of maxsum path possibilites from infinity select maximum from all possibilities.
    # maxsingle=max(max(ls,rs)+root.data,root.data)
    # maxtop=max(maxsingle,ls+rs+root.data)

    # maxsum[0]=max(maxsum[0],maxtop)
    # return maxsingle
def final_path(root):
    maxsum=[float('-inf')]
    maxpath(root,maxsum)
    print(maxsum)
    return maxsum[0]


# count all k-sum paths in a binary tree.
# sum elements upto k, need to count the paths of k.
def count_k_sum(root,k):
    count=0
    if root is None:
        return [],0
    leftpath,leftcount=count_k_sum(root.left,k)
    rightpath,rightcount=count_k_sum(root.right,k)
    paths=leftpath+[root.data]+rightpath 
    for i in range(len(paths)):
        for j in range(i,len(paths)):
            if sum(paths[i:j+1])==k:
                count=count+1
    return paths, leftcount+rightcount+count
    
root = Node(-15)
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
print(count_k_sum(root,5))

##################################################################
# lowest common ancestor in tree.
def find_path(root,path,k):
    if root is None:
        return False 
    
    path.append(root.data)
    # print(path)
    if root.data==k:
        return True
    if (root.left is not None and find_path(root.left,path,k)) or\
    (root.right!=None and find_path(root.right,path,k)):
        return True 
    # if not present in subtree rooted with root node then remove root node from path
    path.pop()
    return False 
def LCA(root,k1,k2):
    # in lowest common ancestor, we need to traverse through k1 path and k2 path.
    # in both of paths stored, start moving from starting index compare both if any mismatch found then return previously matched index.
    path1=[]
    path2=[]
    if not find_path(root,path1,k1) or not find_path(root,path2,k2):
        return -1 
    p1=find_path(root,path1,k1)
    p2=find_path(root,path2,k2)
    print(p1)
    print(p2)
    i=0
    j=0
    while i<len(path1) and j<len(path2):
        if path1[i]!=path2[j]:
            break 
        i=i+1
        j=j+1
        return path1[i-1]
  
    # just need to find the route from root node to k1 and k2
    # if root is None:
    #     return None 
    # leftlca=LCA(root.left,k1,k2)
    # rightlca=LCA(root.right,k1,k2)
    # if root.data==k1 or root.data==k2:
    #     return root 
    # if leftlca and rightlca:
    #     return root 
    # return leftlca if rightlca is None else rightlca
# convert linkedlist into binary search tree.
# first inserting values as linkedlist node values and then those will convert as tree nodes.
class node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class conversion:
    def __init__(self):
        self.root=None 
        self.head=None 

    def push(self,data):
        new_node=node(data)
        new_node.next=self.head 
        self.head=new_node
    def printlist(self):
        curr=self.head
        while curr:
            print(curr.data,end='->')
            curr=curr.next
    def convert_ll_to_bst(self,arr,start,end):
        # approach is take the middle element of list as root node in the bst.
        # and then do recursively for left and right nodes of list.
        if self.head is None:
            root=None 
        # curr=self.head 
        # while curr.next and curr.next.next:
        #     curr=curr.next 
        if start>end:
            return None 
        mid=(start+end)//2
        root=Node(arr[mid]) 
        # print(root.data)
        root.left=self.convert_ll_to_bst(arr,start,mid-1)
        root.right=self.convert_ll_to_bst(arr,mid+1,end)
        return root
    def sorted_ll_to_bst(self):
        vec=[]
        curr=self.head
        while curr:
            vec.append(curr.data)
            curr=curr.next 
        # print(vec)
        vec.sort(reverse=True)
        print(vec)
        return self.convert_ll_to_bst(vec,0,len(vec)-1)
    def preorder(self,root):
        if root:
            print(root.data,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

ll=conversion()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
ll.push(7)
ll.printlist()
print()
ll.root=ll.sorted_ll_to_bst()
ll.preorder(ll.root)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(LCA(root,5,6))

# if we can throw eggs from xth floor if not breaks then check for higher floors for possibility k-x floors.
# if it breaks on x th floor, then need to check down floors.



