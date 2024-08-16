# min heap execution.
# min heap need to represent the minimum value in the root position.
# follows heapify property, if new value entered in the heap structure then swap it with the parent node and maintains min-heap property.
# min heap follows insertion, peek and search.
from heapq import heappush,heappop, heapify
class minheap:
    def __init__(self):
        self.heap=[]

    def insert(self,val):
        heappush(self.heap,val)
    def parent(self,i):
        return (i-1)/2
    def heapify(self,i,new_val):
        self.heap[i]=new_val
        while i!=0 and self.heap[self.parent(i)]>self.heap[i]:
            # while if existed parent element is greater than new element then need to swap,
            # if new element is lesser than parent then no need to swap.
            self.heap[self.parent(i)],self.heap[i]= self.heap[i],self.heap[self.parent(i)]
    def extractmin(self):
        return heappop(self.heap)
    def deletekey(self,i):
        self.heapify(i,float('-inf'))
        # now needed element is in root position. just need to call heappop
        self.extractmin()
    def print_tree(self):
        for i in self.heap:
            print(i,end=' ')
    def getmin(self):
        return self.heap[0]
mh=minheap()
mh.insert(10)
mh.insert(4)
mh.insert(12)
mh.insert(7)
mh.insert(5)
mh.insert(14)
mh.insert(2)
mh.insert(17)
# print(mh.extractmin())
mh.print_tree()
print()
print(mh.getmin())
print(mh.parent(10))

#############################################################################################
# heap implementation 
# heap sorting - maintains max heap and min heap

def heapify(arr,i,n):
    n=len(arr)
    largest=i 
    l=2*i+1
    r=2*i+2
    # if l and r child trees of root  are lesser than largest then consider it as heapified.
    if l<n and arr[l]>arr[largest]:
        largest=l 
    if r<n and arr[r]>arr[largest]:
        largest=r 
    if largest!=i:
        # if largest is not associated as actual highest index, then swap them.
        arr[largest],arr[i]=arr[i],arr[largest]
        # and check for the above conditions if satisfied.
        heapify(arr,largest,n)

def heapsort(arr):
    n=len(arr)
    # in the heap data structure above explains the max heap for sorting.
    # only need to consider the root and their left and right childs.
    for i in range(n//2-1,-1,-1):
        heapify(arr,i,n)
    # now for entire array
    for i in range(n-1,0,-1):
        # now need to swap the leaf nodes with root nodes to maintain heap property and call the heapify to check the largest root at top.
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,0,i)

arr=[12, 11, 13, 5, 6, 7]
heapsort(arr)
print(arr)
