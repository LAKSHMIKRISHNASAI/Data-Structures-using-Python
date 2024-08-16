# class node:
#     def __init__(self,data):
#         self.data=data 
#         self.left=self.right=None 
# convert the binary search tree into max heap
# bringing the maximum value in the tree to the up and maintain the left and right rules of tree property

# finding the max element in the tree and swapping it to the root node.
# swapping the leaves to root and compare the value with childs.
# def bst(root,arr,start,end):
    # while len(arr)>0:
    #     mid=(start+end)//2
    #     root=arr[mid]
    #     root.left=bst(root.left,arr,start,root-1)
    #     root.right=bst(root.right,arr,root+1,end)
    # return root 

# convert binary tree into max heap 
# first need to traverse in inorder traversal
# sort the values in descending order.
# process -  find the inorder traversal of tree
# appending the values into the inorder list 
# now pop the each front element from the arr.
# the pop element is root and check their children nodes attached to it.

# def inorder_traversal(root,inorder_list):
#     if root is None:
#         return 
#     inorder_traversal(root.left,inorder_list)
#     inorder_list.append(root.data,end=' ')
#     inorder_traversal(root.right,inorder_list)

# def convert_to_max_heap(root,max_heap_list):
#     if root is None:
#         return
#     # approach is to find the max heap that means maximum value appear on root node and both left
#     # and right child should be less than root value.
#     root.data=max_heap_list.pop(0)
#     root.left=convert_to_max_heap(root.left,max_heap_list)
#     root.right=convert_to_max_heap(root.right,max_heap_list)

# def construct_bst_to_maxheap(root):
#     inorder_list=[]
#     inorder_traversal(root,inorder_list)
#     max_heap_list=sorted(inorder_list,reverse=True)# inorder_list.sort(reverse=True)
#     convert_to_max_heap(root,max_heap_list)

# root=node(1)
# #  root=node(1)
# root.left=node(2)
# root.right=node(3)
# root.left.left=node(4)
# root.left.right=node(5)
# root.right.left=node(6)
# root.right.right=node(7)
# construct_bst_to_maxheap(root)
#convert bst into max heap
# print the maximum element at top.



# create a heapify_up function to perform max heap operation 
# swapping root node with leaves to follow max heap
#  and then after another method, intialsing array appending all elements into it left and right.
# and then ranging all elements go through with hreapify_up method.
# now the last step is to consider the root at each iteration of upto array end.
# and then verify whether the element less than both left and right child then consider as max heap sorted.

# to find the parent element position in array in heap
# 2*i+1 finds left element
# 2*i+2 finds right element
# class node:
#     def __init__(self):
#         self.data=0
#         self.left=self.right=None
# def getnode(data):
#     Newnode=node()
#     Newnode.data=data 
#     Newnode.left=Newnode.right=None
#     return Newnode
# def parent(i):
#     return (i-1)//2
# def left(i):
#     return (2*i+1)
# def right(i):
#     return (2*i+2)

# def heapify_up(q,i):
#     while i>0 and q[parent(i)].data<q[i].data:
#         q[parent(i)],q[i]=q[i],q[parent(i)]
#         i=parent(i)

# def maxheaputil(root):
#     if root is None:
#         return None 
#     # first need to create a array [] and then appending root to it.
#     # if root left and right childs are not none append to them to queue.
#     # and later heapify up the all elements in the array.
#     # then considering the root and check it with the left and right property then return tree.
#     q=[]
#     q.append(root)
#     i=0
#     while len(q)!=i:
#         if q[i].left is not None:
#             q.append(q[i].left)
#         if q[i].right is not None:
#             q.append(q[i].right)
#         i=i+1
#     for i in range(1,len(q)):
#         heapify_up(q,i)
#     # now need to arrange the left and right child accordingly max heap.
#     root=q[0]
#     i=0
#     while i<len(q):
#         # need to check max heap property where left and right childs should be greater than root.
#         if left(i)<len(q):
#             q[i].left=q[left(i)]
#         else:
#             q[i].left=None 
#         if right(i)<len(q):
#             q[i].right=q[right(i)]
#         else:
#             q[i].right=None 
#     i=i+1
#     return root

# def postorder(root):
#     if root is None:
#         return
#     postorder(root.left)
#     postorder(root.right)
#     print(root.data,end=' ')

# root=getnode(1)
# root.left=getnode(2)
# root.right=getnode(3)
# root.left.left=getnode(4)
# root.left.right=getnode(5)
# root.right.left=getnode(6)
# root.right.right=getnode(7)
# res=maxheaputil(root)
# print(postorder(res))


# merge two bst's with limited extra space.
# need to combine two trees.
# class node:
#     def __init__(self,data):
#         self.data=data 
#         self.left=self.right=None 
# aim to merge two trees - need to keep root nodes in the middle of array.
# and arrange the tree in sorted.
# def mergebst(root1,root2):
# # approach - need to create two stacks, traversing through trees and appending each value to the stacks.
#     s1=[]
#     s2=[]
#     res=[]
#     # approach is to create two stacks and one res stack to add all elements at last.
#     # each tree should be arranged in ascending order sorting.
#     # so first traverse through left sub tree on both trees.
#     # and then check the right sub childs. 
#     while root1 or root2 or s1 or s2:
#         while root1:
#             s1.append(root1)
#             root1=root1.left
#         while root2:
#             s2.append(root2)
#             root2=root2.left
        
#         if not s2 or (s1 and s1[-1].data<=s2[-1].data):
#             # need to print the res in sorted.
#             root1=s1[-1]
#             res.append(root1.data)
#             del s1[-1]
#             root1=root1.right
#         if not s1 or (s2 and s1[-1].data>=s2[-1].data):
#             root2=s2[-1]
#             res.append(root2.data)
#             del s2[-1]
#             root2=root2.right
#     return res 

# merge two binary search trees 
# def merge(root1,root2):
#     s1=[]
#     s2=[]
#     res=[]
#     while root1 or root2 or s1 or s2:
#         while root1:
#             s1.append(root1)
#             root1=root1.left
#         while root2:
#             s2.append(root2)
#             root2=root2.left
#         # upto now both trees left child are added to the stacks now consider the right childs.
#         if not s2 or (s1 and s1[-1].data<=s2[-1].data):
#             root1=s1[-1]
#             res.append(root1.data)
#             del s1[-1]
#             root1=root1.right
#         else:
#             root2=s2[-1]
#             res.append(root2.data)
#             del s2[-1]
#             root2=root2.right
#     return res
# root1=None 
# root2=None 
# root1=node(3)
# root1.left=node(1)
# root1.right=node(5)

# root2=node(4)
# root2.left=node(2)
# root2.right=node(7)
# print(merge(root1,root2))

# def find_path(root,k):
#     if root is None:
#         return False
#     if root.data==k:
#         return True
#     if root and find_path(root.left,k) and find_path(root.right,k):
#         return True
#     return False
# def sum_k_paths(root,k):
#     if root is None:
#         return [],0
#     # path=[]
#     # curr_sum=0
#     count=0
#     # curr_sum=curr_sum+root.data
#     left_path=[]
#     right_path=[]
#     while root.left:
#         left_path.append(root.left.data)
#         root=root.left
#     # while root.left.right:
#     #     left_path.append(root.left.right.data)
#     #     root=root.left.right
#     while root.right:
#         right_path.append(root.right.data)
#         root=root.right
#     # left_path, left_count= sum_k_paths(root.left,k)
#     # right_path,right_count=sum_k_paths(root.right,k)
#     all_paths=left_path + right_path+[root.data]
#     print(all_paths)
#     for i in range(len(all_paths)):
#         for j in range(i,len(all_paths)):
#             if sum(all_paths[i:j+1])==k:
#                 count=count+1
#     return count,all_paths
# root=node(1)
# root.left=node(3)
# root.left.left=node(2)
# root.left.right=node(1)
# root.left.right.left=node(1)
# root.right=node(-1)
# root.right.left=node(4)
# root.right.right=node(5)
# root.right.left.left=node(1)
# root.right.left.right=node(2)
# root.right.right.right=node(6)
# print(sum_k_paths(root,5))


# def sum(root):
#     if root is None:
#         return 0
#     return sum(root.left) + root.data + sum(root.right)
# def is_sum_tree(root):
#     if root is None:
#         return False
#     if not root or (root.left is None and root.right is None):
#         return False 
#     # need to find sum of all left childrens and right childrens.
#     ls=sum(root.left)
#     rs=sum(root.right)
#     if root.data==(ls+rs) and is_sum_tree(root.left) and is_sum_tree(root.right):
#         return True
#     return False

#  longest consecutive subsequence.

# priority queue in array
# import sys
# class item:
#     value=0
#     priority=0

# class pq:
#     pr=[None]*10000
#     size=-1 #last index empty queue

#     # priority queue works based on the priority elements/values.
#     def enqueue(value,priority):
#         pq.pr[pq.size]=item()
#         pq.pr[pq.size].value=value 
#         pq.pr[pq.size].priority=priority
#     def peek():
#         # need to return highest priority value from the queue
#         highest_priority=-sys.maxsize
#         ind=-1 #index at not initial position

#         i=0
#         while i<=pq.size:
#             if highest_priority==pq.pr[i].priority and ind>-1 and pq.pr[ind].value<pq.pr[i].value:
#                 highest_priority=pq.pr[i].prirority 
#                 ind=i 
#             if highest_priority<pq.pr[i].priority:
#                 highest_priority=pq.priority
#                 ind=i
#         return ind
    
#     def dequeue():
#         ind=pq.peek()
#         i=ind 
#         while i<pq.size:
#             pq.pr[i]=pq.pr[i+1]
#             i+=1 
#         pq.size-=1

# if __name__=='__main__':
#     pq.enqueue(10,1)
#     pq.enqueue(20,2)
#     pq.enqueue(7,3)
#     pq.enqueue(11,4)
#     pq.enqueue(18,5)

#     ind=pq.peek()
#     print(pq.pr[ind].value)

#     pq.dequeue()
#     ind2=pq.peek()
#     print(pq.pr[ind2].value)
#     print(pq.pr[ind2].priority)



# longest consecutive subsequence
# using priority used to find, queue sorting the elements



###################################################################################################################################################
# convert binary search tree to max heap 
class node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
        
def insert_node(root,data):
    if root is None:
        return node(data)
    if root.data==data:
        return root
    if data<root.data:
        root.left=insert_node(root.left,data)
    else:
        root.right=insert_node(root.right,data)
    return root
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.data,end=' ')
        print_tree(root.right)
# convert binary search tree to max heap 
# to convert into heap, need parent element, left child and right child.
def parent(i):
    return (i-1)//2 
def left(i):
    return 2*i+1 
def right(i):
    return 2*i+2 
# def inorder_traversal(root,arr):
#     if root:
#         inorder_traversal(root.left,arr)
#         arr.append(root.data)
        
#         inorder_traversal(root.right,arr)
# def heapfiy(root,maxheap_list):
#     if root is None:
#         return 
#     root.data=maxheap_list.pop(0)
#     root.left=heapfiy(root.left,maxheap_list)
#     root.right=heapfiy(root.right,maxheap_list)
#     return root
# def maxheap(root):
#     arr=[]
#     inorder_traversal(root,arr)
#     maxheap_list=sorted(arr,reverse=True)
#     heapfiy(root,maxheap_list)

# def print_heap(root):
#     if root:
#         # print(root.data,end=' ')
#         print_heap(root.right)
#         print(root.data,end=' ')
#         print_heap(root.left)
    # print()
# another approach to convert bst to maxheap.

def heapify(q,i):
    # here heap property according to maxheap is if any new value found greater than parent then need to swap both.
    
    while i>0 and q[parent(i)].data<q[i].data:
        q[parent(i)],q[i]=q[i],q[parent(i)]
        # and update that value as parent 
        i=parent(i)
    
def maxheap(root):
    # instead of using inorder traversal to print all the values into the arry 
    # another approach is defining a array and appending all the root children values.
    if root is None:
        return None 
    q=[]
    q.append(root)
    i=0 
    while i!=len(q):
        if q[i].left is not None:
            q.append(q[i].left)
            # print(q[i].left.data)
        if q[i].right is not None:
            q.append(q[i].right)
            # print(q[i].right.data)
        i=i+1 
    for i in range(1,len(q)):
        heapify(q,i)
    # print(q)
    root=q[0]
    # now arr is sorted with heapify property having max value at root.
    # now all the values at left and right are minimum than heap value.
    # 20 9 10 12 15 17 elements are sorted according to max heap now need to make them heap arr with 2*i+! as left child and 2*i+2 as rigjt chidl/
    # just consider root as q[0] element and arange the left and right sub childs.
    
    i=0 
    while i<len(q):
        if left(i)<len(q):
            q[i].left=q[left(i)]
        else:
            q[i].left=None 
        if right(i)<len(q):
            q[i].right=q[right(i)]
        else:
            q[i].right=None 
    i=i+1 
    return root
def print_heap(root):
    if root:
        # print(root.data,end=' ')
        print_heap(root.right)
        print(root.data,end=' ')
        print_heap(root.left)
    # print()

    # root=q[0]
    # i=0 
    # while i<len(q):
    #     if left(i)<len(q):
    #         q[i].left=q[left(i)]
    #     else:
    #         q[i.left=None]
    #     if right(i)<len(q):
    #         q[i].right=q[right(i)]
    #     else:
    #         q[i].right=None 
    # i=i+1 
    # return root
    # print(q)
    # now array q filled with bst nodes. now need to set them in heap property and find maxheap.
    # first make them all values in the heap property.
    
# def maxheap_util(root):
    
root=node(14) 
insert_node(root,10)
insert_node(root,20)
insert_node(root,15)
insert_node(root,12)
insert_node(root,9)
insert_node(root,19)
print_tree(root)
# maxheap(root)
print()
# print_heap(root)
res=maxheap(root)
print_heap(res)