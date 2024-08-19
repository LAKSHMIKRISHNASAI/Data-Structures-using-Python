
def kthlargest(arr,k):
    arr.sort(reverse=True)
    for i in range(k):
        print(arr[i],end=' ')
arr=[1, 23, 12, 9, 30, 2, 50]
k=3
kthlargest(arr,k)



# kth largest sum contigous subarray
def kthlargestsum(arr,k):
    res=[]
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum=sum+arr[j]
            res.append(sum)
    res.sort(reverse=True)
    print(res)
    return res[k-1]
    
k=3
arr=[20, -5, -1]
# arr=[10, -10, 20, -40]
kthlargestsum(arr,k)



# implementation of priority queue with binary heap
# insert operation
# shift up
# extract max
# shift down
# change priority
# remove
import heapq
class priority_queue:
    def __init__(self):
        self._heapqueue=[]
        self._index=0
    def enqueue(self,item,priority):
        heapq.heappush(self._heapqueue,(priority,self._index,item))
        self._index=self._index+1
    def dequeue(self):
        return heapq.heappop(self._heapqueue)[-1]
    def peek(self):
        return self._heapqueue[-1]
    def count(self):
        return len(self._heapqueue)
    
p=priority_queue()
p.enqueue(1,1)
p.enqueue(10,2)
p.enqueue(-8,3)
p.enqueue(25,4)
p.enqueue(14,5)
# p.dequeue()
# p.dequeue()
p.peek()
# p.count()


# In[70]:


h=[0]*50
size=-1

def parent(i):
#     the parent in the heap in (i-1)//2
    return ((i-1)//2)
    
def left(i):
    return (2*i+1)
def right(i):
    return (2*i+2)    
def insert(val):
    global size
    size=size+1
    h[size]=val
   
#     to correct the heap property need to check the inserted value with shift up heap property
    shift_up(size)
    return val
def shift_up(i):
    curr_index=i
    while curr_index>0 and (h[curr_index]>h[parent(curr_index)]):
        
        h[curr_index],h[parent(curr_index)]=h[parent(curr_index)],h[curr_index]
        current_index=parent(curr_index)   
    
def shift_down(i):
    largest=i
    l=left(i)
    if l<len(h) and h[l]>h[largest]:
        largest=l
    r=right(i)
    if r<len(h) and h[r]>h[largest]:
        laregst=r
    if largest!=i:
        h[largest],h[i]=h[i],h[largest]
        shift_down(largest)
    
def extract_max():
    global size
    res=h[0]
#     need to store removing root node in some where
#     h[0] #it is the root node of tree
#     h[-1]#leaf node of tree
    h[0]=h[size]
    size=size-1
#     now leaf node occupies the root node position now need to correct the max heap property within the tree
    shift_down(0)
    return res
def change_priority(i,p):
#     (old index,new index priority)
    oldp=h[i]
    h[i]=h[p]
#     now need to correct the heap structure
    if (p>oldp):
        shift_up(i)
    else:
        shift_down(i)
        
def remove(i):
#     depends on priority need to remove priority value first
    h[i]=h[0]+1
    shift_up(i)
    extract_max()
def get_max():
    return h[0]


insert(40)
insert(12)
insert(30)
insert(27)
insert(10)
insert(7)
insert(8)
insert(19)
insert(7)

i=0
while i<=size:
    print(h[i],end=' ')
    i=i+1
print()
extract_max()
j=0
while (j<=size):
    print(h[j],end=' ')
    j=j+1
print()
get_max()
# change_priority(2,49)
# change_priority(3,21)

# j=0
# while (j<=size):
#     print(h[j],end=' ')
#     j=j+1
# print()
# change_priority(4,13)
# k=0
# while (k<=size):
#     print(h[k],end=' ')
#     k=k+1
# print()
# remove(3)
# l=0
# while l<=size:
#     print(h[l],end=' ')
#     l=l+1
# print()


# In[91]:


# implementing the priority queue using arrays
import sys
class item:
    priority=0
    value=0
class pq:
    pr=[None]*500
    ind=-1 #last index of the queue
    
    def enqueue(value,priority):
        pq.ind=pq.ind+1
        pq.pr[pq.ind]=item()
        pq.pr[pq.ind].value=value
        pq.pr[pq.ind].priority=priority
        
    def peek():
#         to find the top-most element from the queue
        highestpriority=-sys.maxsize
        index=-1
        
        i=0
        while (i<pq.ind):
            if (highestpriority==pq.pr[i].priority) and index>-1 and pq.pr[index].value<pq.pr[i].value:
                highestpriority=pq.pr[i].priority
                index=i
            elif (highestpriority<pq.pr[i].priority):
                highestpriority=pq.pr[i].priority
                index=i
            i=i+1
        return index
    def dequeue():
        ind=pq.peek()
        i=ind
        while i<pq.ind:
            pq.pr[i]=pq.pr[i+1]
            i=i+1
        pq.ind=pq.ind-1
# p=pq()

pq.enqueue(10,3)
pq.enqueue(12,2)
pq.enqueue(24,1)
pq.enqueue(7,4)
pq.enqueue(15,5)
pq.enqueue(18,6)
pq.enqueue(17,7)
pq.dequeue()

# pq.peek()
i=0
while i<pq.ind:
    print(f'{pq.pr[i].value}:{pq.pr[i].priority}',end=', ')
    i=i+1
print()

pq.peek()
# j=0

            
            
        
        


# In[101]:


# priority queue with array
# need to give priority along with value
class item:
    priority=0
    value=0
class prqu:
    pr=[None]*(500000)
    size=-1#last index
    
    def enqueue(value,priority):
        prqu.size=prqu.size+1
        prqu.pr[prqu.size]=item()
        prqu.pr[prqu.size].value=value
        prqu.pr[prqu.size].priority=priority
        
    def peek():
#         aim to find the highest priority element from the queue
# to access that indxe, we will intiate with highest priority as max size of queue and last index of queue.
        highestpriority=-sys.maxsize
        index=-1
        
        i=0
        while (i<prqu.size):
            if (highestpriority==prqu.pr[i].priority) and (prqu.pr[index].value < prqu.pr[i].value) and index>-1:
                highestpriority=prqu.pr[i].priority
                index=i
                
            elif highestpriority<prqu.pr[i].priority:
                highestpriority=prqu.pr[i].priority
                index=i
            i=i+1
        return index
    def dequeue():
        ind=prqu.peek()
        i=ind
        while i<prqu.size:
            prqu.pr[i]=prqu.pr[i+1]
            i=i+1
        prqu.size=prqu.size-1

prqu.enqueue(40,1)
prqu.enqueue(21,2)
prqu.enqueue(42,3)
prqu.enqueue(10,4)
prqu.enqueue(14,5)
prqu.enqueue(4,6)
prqu.enqueue(27,7)
i=0
while(i<prqu.size):
    print(prqu.pr[i].value,end=' ')
    i=i+1
print()

ind=prqu.peek()
print(prqu.pr[ind].value)


# In[108]:


# implementation of priority queue using linked list
class node:
    def __init__(self,val,priority):
        self.val=val
        self.priority=priority
        self.next=None
class queue_list:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return True if self.head==None else False
    
    def push_node(self,val,priority):
        
        if self.isEmpty()==True:
            self.head= node(val,priority)
            return 1
    
        else:
            
            if self.head.priority < priority:
                new_node= node(val,priority)
                new_node.next=self.head
                self.head=new_node
                return 1
        
            else:
                #traversing the node until it find the next smaller priority node
                curr=self.head
                while curr.next is not None:
                    if priority>=curr.next.priority:
                        break
                    curr=curr.next
                new_node= node(val,priority)
                new_node.next=curr.next
                curr.next=new_node
                return 1
    def pop(self):
        if self.isEmpty()==True:
            return
        else:
            self.head=self.head.next
            return 1
    def peek(self):
        if self.isEmpty()==True:
            return
        else:
            return self.head.val
    def traverse(self):
        curr=self.head
        while curr:
            print(f'{curr.priority}:{curr.val}',end=' ')
            curr=curr.next
pq=queue_list()
pq.push_node(4, 1)
pq.push_node(5, 2)
pq.push_node(6, 3)
pq.push_node(7, 0)
pq.traverse()
pq.peek()        
        


# In[1]:


# searching the two elements which gives sum to the required value.
def binarysearch(arr,low,high,searchkey):
    m=0
    while (low<=high):
        m=(low+high)//2
        if (searchkey==arr[m]):
            return 1
        elif (searchkey<arr[m]):
            low=m+1
        else:
            high=m-1
    return 0
def checktwosum(arr,sum):
    l=0
    r=len(arr)-1
    arr.sort()
    i=0
    while i<len(arr):
        searchkey=sum-arr[i]
        if (binarysearch(arr,i+1,r,searchkey)==1):
            return 1
        i=i+1
    return 0
        


# In[1]:


def bubble_sort(arr):
#     used to swap the adjacent elements by comparing with each other
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[12,2,14,7,16,27,3]
bubble_sort(arr)
            
        


# In[12]:


def sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j+1]>arr[j]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr
            
arr=[12,2,14,7,16,27,3]
sort(arr)
# print(arr)
            


# In[17]:


def sorting(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j+1]>arr[j]:
                 arr[j+1],arr[j]=arr[j],arr[j+1]
#     arr.sort()
    return arr
           
arr=[12,2,14,7,16,27,3]
sorting(arr)     
            


# In[27]:


def selection_sort(arr):
    for i in range(len(arr)):
        min=arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]<min:
                min=arr[j]
                arr[i],arr[j]=arr[j],arr[i]
    return arr
            
arr=[12,2,14,7,16,27,3]
selection_sort(arr)
        
        


# In[33]:


arr=[12,2,14,7,16,27,3]
for i in range(len(arr)):
    min_val=min(arr[i:])
    min_index=arr.index(min_val)
    if arr[i]!=arr[min_index]:
        arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)
    


# In[34]:


# approaches of selection sort - to find the minimum index or selecting the first value as minimum
for i in range(len(arr)):
    min_val= min(arr[i:])
    min_index= arr.index(min_val)
    if arr[i]!=min_val:
        min_val,arr[i]=arr[i],min_val
print(arr)


# In[64]:


n=7
for i in range(n):
    for j in range(0,n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

    
for i in range(n,-1,-1):
    for j in range(n-i):
        print('*',end=' ')
    for j in range(i):
        print(end=' ')
    print()
    
for i in range(n):
    for j in range(n-i):
        print(end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
    
for i in range(n,-1,-1):
    for j in range(n-i):
        print(end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()


# In[66]:


# longest subarray with sum divisible by k
def longsubarr(arr,k):
    maxsum=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum=sum+arr[j]
            if sum%k==0:
                maxsum=max(maxsum,j-i+1)
    return maxsum
        
arr=[2, 7, 6, 1, 4, 5]
k=3
longsubarr(arr,k)


# In[1]:


# # moore's algoithm voting system
# # implementation of algorithm-
# # starts with votes=0, and candidate =-1 last index
# # if votes==0 then consider current value as candidate and make count 1 
# # if while traversing the loop, if arr of value equals to candidatethen increments the votes 
# # else decrements the votes by 1 at each mismath
# # if candidate count reaches more than half of an array then considers its  an majority element in the array/

# def find_majority_ele(arr):
#         votes=0
#         candidate=-1
#         for i in range(len(arr)):
#             if (votes==0):
#                 candidate=arr[i]
#                 votes=1 
#             else:
#                 if arr[i]==candidate:
#                     votes=votes+1 
#                 else:
#                     votes-=1
#         count=0
#         for i in range(len(arr)):
#             if (arr[i]==candidate):
#                 count=count+1 
#                 # votes=votes+1 
#         if count>len(arr)//2:
#             return candidate
#         else:
#             return -1
 
# arr = [ 1, 1, 1, 1, 2, 3, 4 ]
# print(find_majority_ele(arr))
# def find_majority_element(arr):
#     count=1 
#     maj_index=0 
#     for i in range(len(arr)):
#         if arr[maj_index]==arr[i]:
#             count=count+1 
#         else:
#             count=count-1
#         if count==0:
#             maj_index=i 
#             count=1
#     return arr[maj_index]
# def majority(arr):
#     cand=find_majority_element(arr)
#     count=0
#     for i in range(len(arr)):
#         if arr[i]==cand:
#             count=count+1 
#     if count>len(arr)//2:
#         return cand

# arr = [ 1, 1, 1, 1, 2, 3, 4 ]  
# print(majority(arr))

# using hashing
# def find_major_element(arr):
#     hash_map={}
    
#     for i in range(len(arr)):
#         if arr[i] in hash_map:
#             hash_map[arr[i]]=hash_map[arr[i]]+1
#         else:
#             hash_map[arr[i]]=1
#     for key in hash_map:
#         if hash_map[key]>len(arr)/2:
#             return key
#         else:
#             print('majority element not found')
# arr = [ 1, 1, 1, 1, 2, 3, 4 ]  
# print(find_major_element(arr))

class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
        self.count=1
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        out=None
        if self.root is None:
            self.root=node(data)
        else:
            out=self.insertnode(self.root,data)
        return out
        
    def insertnode(self,root, data):
        if root.data==data:
            root.count=root.count+1 
            if root.count >len(arr)//2:
                return root.data
            else:
                return None
        elif root.data<data:
            if root.right:
                self.insertnode(root.right,data)
                #if root.right sub tree exists then just need to insert within itself.
            else:
                root.right=node(data)
        elif root.data>data:
            if root.left:
                self.insertnode(root.left,data)
            else:
                root.left=node(data)
tree=BST()

arr= [ 1, 1, 1, 1, 2, 3, 4 ] 

i=0
while i<len(arr):
    # print(arr[i])
    out=tree.insert(arr[i])
    if (out !=None):
        print(arr[i])
        break
  


# In[5]:


# leaders in the array
# need to find maximum values from the array 
# and the rightmost element is always leader
def find_leaders(arr):
    max_val=0
    max_val2=arr[-1]
    res=set()
    for i in range(len(arr)-1):
        max_val=max(arr[i:])
        res.add(max_val)
    res.add(max_val2)
    return res
arr=[1, 2, 3, 4, 5, 2]
find_leaders(arr)  


# In[15]:


# finding the missing number from the array
# brute-force approach
def find_missing(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if (arr[i+1]-arr[i])>1:
            result= (arr[i+1]+arr[i])/2
    return int(result)
# arr=[1, 2, 4, 6, 3, 7, 8]
arr=[1, 2, 3, 5]
find_missing(arr)
#     for i in range(len(arr)
        
        
    


# In[16]:


def get_missing(arr):
    n=len(arr)
    total=(n+1)*(n+2)/2
    sum_of_all=sum(arr)
    return total-sum_of_all
arr=[1,2,3,5]
get_missing(arr)


# In[ ]:


# formula to find the missing value is (n+1)(n+2)/2+


# In[21]:


def find_missing(arr,n):
    n=len(arr)
    temp=[0]*(n+1)
    for i in range(n):
        temp[arr[i]-1]=1
    for i in range(n+1):
        if (temp[i]==0):
            ans=i+1
    return ans
arr=[1, 2, 4, 6, 3, 7, 8]
find_missing(arr,len(arr))


# In[64]:


# rotation of array
def reverse_array(arr,k):
    k=k%len(arr) #to handle the case where k is greater than len(arr)
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left=left+1
        right=right-1
#     return arr
    left=0
    right=k-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left=left+1
        right=right-1
    left=k
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left=left+1
        right=right-1
    return arr
# def rotate_arr(arr,k):
#     if k==0:
#         return
#     k=k%len(arr)
#     reverse_array(arr,0,k-1)
#     reverse_array(arr,k,len(arr)-1)
#     reverse_array(arr,0,len(arr)-1)

# def print_arr(arr):
#     for i in range(len(arr)):
#         print(arr[i],end=' ')
arr=[1, 2, 3, 4, 5, 6, 7]
k=2
reverse_array(arr,k)
# rotate_arr(arr,k)
# print_arr(arr)


# In[69]:


n=len(arr)
k=2
def rev_arr(arr,k):
    k=k%n
    arr[:n]=arr[0:n][::-1]
    arr[0:k]=arr[0:k][::-1]
    arr[k:n]=arr[k:n][::-1]
    return arr
arr=[1, 2, 3, 4, 5, 6, 7]
# print(arr)
rev_arr(arr,2)


# In[80]:


from collections import deque
d=deque(arr)
d.rotate(-2)


# In[79]:


arr=[1,2,3,4,5]


# In[81]:


d


# In[82]:


from collections import deque
arr2=[1, 2, 3, 4, 5, 6, 7]
d=deque(arr2)
d.rotate(-2)


# In[84]:


list(d)


# In[141]:


# reverse the linked list in the k-groups
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class reverse_nodes:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
        
    def reverse_k_nodes(self,head,k):
        if head==None:  
            return None  
        curr=head  
        next=None  
        prev=None  
        count=0
        while (curr is not None and count<k):
            count=count+1
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
#             count=count+1
        if next is not None:
            head.next=self.reverse_k_nodes(next,k)
        return prev
    def reverse(self):
        curr=self.head
        prev=None
        while curr.next is not None:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data,end=' ') 
            temp = temp.next
        print()
        
llist = reverse_nodes() 
llist.push(9) 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1)
# k=3
# llist.reverse_k_nodes(k)
# llist.reverse()
llist.printList()

llist.head=llist.reverse_k_nodes(llist.head,3)
llist.printList()
# print()
# llist.reverse()
# llist.printList()


# In[138]:


class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    def reverse(self, head, k): 
        
        if head == None: 
          return None
        current = head 
        next = None
        prev = None
        count = 0
  
        # Reverse first k nodes of the linked list 
        while(current is not None and count < k): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
            count += 1
  
        # next is now a pointer to (k+1)th node 
        # recursively call for the list starting 
        # from current. And make rest of the list as 
        # next of first node 
        if next is not None: 
            head.next = self.reverse(next, k) 
  
        # prev is new head of the input list 
        return prev 
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data,end=' ') 
            temp = temp.next
  
  
# Driver program 
llist = LinkedList() 
llist.push(9) 
llist.push(8) 
llist.push(7) 
llist.push(6) 
llist.push(5) 
llist.push(4) 
llist.push(3) 
llist.push(2) 
llist.push(1) 
  
print("Given linked list") 
llist.printList() 
llist.head = llist.reverse(llist.head, 3) 
  
print ("\nReversed Linked list") 
llist.printList() 


# In[41]:


# 1-2-3-4-5
# 1-4-3-2-5

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class llist:
    def __init__(self):
        self.head=None
    def insert_node(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_at_position(self,data,position):
        # prev=None
        curr=self.head
        count=0
        if position==0:
            new_node=node(data)
            new_node.next=self.head
            self.head=new_node
            return self.head
        while curr is not None and count<position-1:
            count=count+1 
            curr=curr.next 
        new_node=node(data)
        new_node.next=curr.next
        curr.next=new_node
    def reverse_k_nodes(self,head,k):
        if head is None:
            return None
        curr=head
#         next=None
        prev=None
        next=None
        count=0
        while (curr is not None and count<k):
#             count=count+1
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            count=count+1
            
        if next is not None:
            head.next=self.reverse_k_nodes(next,k)
            
        return prev
    
    def reverse_nodes(self):
        # dummy=node(0)
        prev=None
        curr=self.head
        # next=None
        # curr=self.head 
        while curr is not None:
            next_node=curr.next 
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev
        # return dummy.next
    def rotate_list(self,k):
        curr=self.head
        count=0
        while curr is not None and count<k-1:
            count=count+1
            curr=curr.next
        if curr is None:
            return
        kthnode=curr
        while curr.next is not None:
            curr=curr.next
        curr.next=self.head 
        self.head=kthnode.next
        kthnode.next=None 
    def print_list(self):
        curr=self.head
        while curr is not None:
            print(curr.data,end='->')
            curr=curr.next 
        print()
l=llist()
l.insert_node(1)
l.insert_node(2)
l.insert_node(3)
l.insert_node(4)
l.insert_node(5)
l.print_list()
# l.reverse_nodes()
# l.print_list()
# l.insert_at_position(15,2)
# l.insert_at_position(20,3)
# l.insert_at_position(25,4)
# l.insert_at_position(30,5)
# l.print_list()
# l.rotate_list(2)
# l.print_list()
l.head=l.reverse_k_nodes(l.head,2)
l.print_list()


# In[65]:


# merge two sorted linked lists
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def add_node(head,data):
    new_node=node(data)
    if head is None:
        return new_node
    else:
        curr=head
        while curr.next is not None:
            curr=curr.next
        curr.next=new_node
    return head
def merge_lists(l1,l2):
    dummy=node(0)
    tail=dummy
#     if l1 is None:
#         tail.next=l2
#     if l2 is None:
#         tail.next=l1
    while l1 is not None and l2 is not None:
        if l1.data<l2.data:
            tail.next=l1
            l1=l1.next
        else:
            tail.next=l2
            l2=l2.next
        tail=tail.next
    if l1 is not None:
        tail.next=l1
    else:
        tail.next=l2
    return dummy.next
def print_list(head):
    curr=head
    while curr:
        print(curr.data,end='->')
        curr=curr.next


if __name__=='__main__':
    head=None
    a=None
    a=add_node(a,1)
    a=add_node(a,3)
    a=add_node(a,4)
    a=add_node(a,6)
    a=add_node(a,8)
#     a.next.next.next=node(a,6)
                     
    b=None
    b=add_node(b,2)
    b=add_node(b,4)
    b=add_node(b,5)
    b=add_node(b,7)
    b=add_node(b,9)
#     b.next=node(b,5)
#     b.next.next=node(b,7)
#     b.next.next.next=node(b,9)
    res=merge_lists(a,b)
    print_list(res)
    


# In[ ]:





# In[80]:


class node:
    def __init__(self, data):
        self.data = data
        self.next = None
def append(head,data):
    new_node=node(data)
    if head is None:
        return new_node
    else:
        curr=head
        while curr.next:
            curr=curr.next
        curr.next=new_node
def sort_two_lists(l1,l2):
#     dummy=node(0)
#     tail=dummy
    temp=None
    
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    while l1 and l2:
        if l1.data<=l2.data:
            temp=l1
            temp.next= sort_two_lists(l1.next,l2)
        else:
            temp=l2
            temp.next=sort_two_lists(l1,l2.next)
        temp=temp.next
    return temp
def merge_lists(a,b):
    dummy=node(0)
    tail=dummy
    if a is None:
        tail.next=b
    if b is None:
        tail.next=a
    while a and b:
        if a.data<=b.data:
            tail.next=a
            a=a.next
        else:
            tail.next=b
            b=b.next
        tail=tail.next
    return dummy.next
def print_list(head):
    curr=head
    while curr:
        print(curr.data,end='->')
        curr=curr.next

        
head=None
a=None
append(a,1)
append(a,3)
append(a,5)
append(a,7)
b=None
append(b,2)
append(b,4)
append(b,6)
append(b,8)
new_res= sort_two_lists(a,b)
print_list(new_res)
r=merge_lists(a,b)
print_list(r)


# In[87]:


class node:
    def __init__(self, data):
        self.data = data
        self.next = None
# class llist:
#     def __init__(self):
#         self.head=None
# def add_node(data):
#     return node(data)

a=node(1)
a.next=node(3)
a.next.next=node(5)
a.next.next.next=node(7)
a.next.next.next.next=node(9)

b=node(2)
b.next=node(4)
b.next.next=node(6)
b.next.next.next=node(8)
b.next.next.next.next=node(10)
v=[]
while a is not None:
    v.append(a.data)
    a=a.next
# v2=
while b is not None:
    v.append(b.data)
    b=b.next
v.sort()
# need to convert list into linkedlist

dummy=node(-1)
temp=dummy
# add values to the list
for i in range(len(v)):
    dummy.next= node(v[i])
    dummy=dummy.next
temp=temp.next
while temp is not None:
    print(temp.data,end='->')
    temp=temp.next


# In[97]:


# swap pair of nodes
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class llist:
    def __init__(self):
        self.head=None
    def pairwise_swap(self):
        curr=self.head
        if curr is None:
            return
        
        while curr and curr.next:
            if curr.data!=curr.next.data:
                curr.data,curr.next.data=curr.next.data,curr.data
            curr=curr.next.next
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        curr=self.head
        while curr:
            print(curr.data,end='->')
            curr=curr.next
        print()
l=llist()
l.push(10)
l.push(20)
l.push(30)
l.push(40)
l.push(50)
l.push(60)
l.print_list()

l.pairwise_swap()
l.print_list()


# In[16]:


# reverse the stack recursively
# steps-- pop element first, add it to down  
def reverse(s):
    if not s:
        return 
    top=s.pop()
    reverse(s)
    insert_at_bottom(s,top) 

def insert_at_bottom(s,ele):
    if not s:
        s.append(ele)
        return
    top=s.pop()
    insert_at_bottom(s,ele)
    s.append(top)
stack=[1,2,3,4]
print(stack)
reverse(stack)
print(stack)
    


# In[19]:


# reverse stack recursively

# first pop the top recursively and add it to down.
# 1 2 3 4
# 4 3 2 1 return
def reverse_(s):
    if not s:
        return 
    top=s.pop()
    reverse(s)
#     now need a function to insert them back in reverse  or bottom of stack.
    insert_at_bottom(s,top)
def insert_at_bottom(s,ele):
    if not s:
        s.append(ele)
        return
    top=s.pop()
    insert_at_bottom(s,ele)
    s.append(top)
    
s=[1,2,3,4,5]
print(s)
reverse_(s)
print(s)


# In[21]:


# checking for balanced brackets in an expression
def check_balanced_brackets(exp):
#     s={']':'[','}':'{',')':'('}
    s=[]
    for char in exp:
        if char in ['[','(','{']:
            s.append(char)
        else:
#             if current insertion is not opening bracket and need to find closing bracket
# then searching in the stack.
            if not s:
                return False
            curr_char=s.pop()
            if char==')':
                if curr_char=='(':
                    return True
            if char==']':
                if curr_char=='[':
                    return True
            if char=='}':
                if curr_char=='{':
                    return True
#             if char==')':
#                 if curr_char!='(':
#                     return False
#             if char==']':
#                 if curr_char!='[':
#                     return False
#             if char=='}':
#                 if curr_char!='{':
#                     return False
    if len(s)==0:
        return True
    return False


exp='[()]{}{[()()]()}'

res=check_balanced_brackets(exp)
if res== True:
    print('Balanced')
else:
    print('not balanced')
          


# In[31]:


def find_second_largest(arr):
    if len(arr)<2:
        return None
    first=float('-inf')
    second=float('-inf')
    
    for num in arr:
        if num>first:
            second=first
            first=num
            
        elif num>second and num!=first:
            second=num
    return second if second!=float('-inf') else None
arr=[2,14,5,7,23,12,10,17,9]
find_second_largest(arr)
                


# In[1]:


# find maximum from neighbors in the array 
# if array in ascending order then strictly increasing element will be peak 
# if elements in decreasing order then the first element is peak 
# if not sorted, then find peak from neighbors.
def find_peak(arr):
    n=len(arr)
    if arr[0]>=arr[1]:
        return arr[0]
        
    if arr[n-1]>=arr[n-2]:
        return arr[n-1]
    for i in range(1,n-1):
        peak=arr[i]
        if peak>arr[i-1] and peak>arr[i+1]:
            return arr[i]

# arr = [ 1, 3, 20, 4, 1, 0 ]
arr=[10, 20, 15, 2, 23, 90, 67]
print(find_peak(arr))
# find the mid value in the array, if mid value is peak element then check neighbors if
# arr[0] or arr[mid] > arr[mid-1] and arr[n-1] or arr[mid]>arr[mid+1] then break and return mid 
#############################################################################
# each time mid length will changes.
def find_peak_ele(arr):
    l=0 
    r=len(arr)-1 
    while l<=r:
        mid= (l+r)//2 
        
        if (mid==0 or arr[mid-1]<=arr[mid]) and (arr[mid]>=arr[mid+1] or mid==len(arr)-1):
            break 
        if arr[mid]<arr[mid-1]:
            r=mid-1
        else:
            l=mid+1
    return arr[mid]
arr=[10, 20, 15, 2, 23, 90, 67]
print(find_peak_ele(arr))
#######################################################################
def count_pairs(arr,k):
    # k_sum=0 
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(i+1,n):
            # count=0
            k_sum=arr[i]+arr[j]
            if k_sum==k:
                count=count+1 
            # if k_sum>k:
            #     count=a 
    return count 
arr=[1, 5, 7, -1]
k=6
print(count_pairs(arr,k))
# binary search to count pairs of sum 
# if k-arr[i] in arr then count.
#########################################################################
def count_k_pairs(arr,k):
    count=0
    temp=[]
    for i in range(len(arr)):
        if k-arr[i] in temp:
            count=count+1 
        temp.append(arr[i])
    return count 
arr=[1, 5, 7, -1,5]
k=6
print(count_k_pairs(arr,k))
###########################################################################
def find_pairs_count(arr,k):
    map={}
    count=0 
    for i in range(len(arr)):
        if k-arr[i] in map:
            count=count+ map[k-arr[i]]
        if arr[i] in map:
            map[arr[i]]+=1 
        else:
            map[arr[i]]=1 
    return count
arr=[1, 5, 7, -1,5]
k=6
print(find_pairs_count(arr,k))
#################################################################################
# stock buy and sell 
def buy_and_sell(arr):
    n=len(arr)
    # first need to find the lowest price to buy and finding profit day to sell. 
    # loop to consume the price 
    # for i in range(n):
    #     # consume=arr
    #     if arr[i]<arr[i+1]:
    #         consume=arr[i]
    # for i in range(n):
    #     if arr
    max_profit=0
    i=0
    while i<n-1:
        
        while i<n-1 and arr[i+1]<=arr[i]:
            i=i+1 
        consume=arr[i]
        i=i+1
        if i==n-1:
            break
        
        while i<n and arr[i]>=arr[i-1]:
            i=i+1 
        sell=arr[i-1]
        print('consume:',consume, '\t'
                'sell:',sell)
        max_profit=max_profit + (sell-consume)
    return max_profit
    
price=[100, 180, 260, 310, 40, 535, 695]
n=len(price)
print(buy_and_sell(price))
# start to find less price day 
# end to find the maximum profit day.
###########################################################################
def stocks_profit(arr,start,end):
    if end<=start:
        return 0
    max_profit=0
    n=len(arr)
    for i in range(start,end):#loop to find day for consuming
        for j in range(i+1,end+1):#loop to sell the stock
            if arr[j]>arr[i]:
                curr_profit=arr[j]-arr[i] + stocks_profit(arr,start,i-1)\
                +stocks_profit(arr,j+1,end)
                max_profit=max(max_profit,curr_profit)
    return max_profit
price=[100, 180, 260, 310, 40, 535, 695]
# n=len(price)
start=0 
end=len(price)-1
print(stocks_profit(price,start,end))
# choclate distribution problem 


# In[8]:


# count distinct elements in each window of size k 
def count_distinct_win(window,k):
#     h_map={}
#     collect=0
# iteration of arr with window size 
# first function to count distinct values in the window size array
# another function to maintain window and iterate over the array.
    distinct_count=0
    for i in range(k):
        j=0
        while j<=i:
            if (window[j]==window[i]):
                break 
            else:
                j=j+1 
        if (j==i):
            distinct_count=distinct_count+1 
    return distinct_count, arr[i:i+distinct_count]

def count_elements(arr,k):
    n=len(arr)
    for i in range(n-k+1):
        print(count_distinct_win(arr[i:k+i],k))
#     print()
    
        
arr=[2,3,1,4,3,2,1,3,2,1,3,4]
k=4
count_elements(arr,k)






