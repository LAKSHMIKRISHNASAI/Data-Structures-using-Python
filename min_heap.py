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
#####################################################################################################################
# Min heap without using heap in-built functions.
# min heap used to follows the rule of having minimum value on the root and both child of root should be maximum than root.
# need to check min-heap property if new entered value is smaller than, if root is greater than that new i value then swap the parent value with entered value.
# using an array constructing a tree or either finding the task of maximum element or sorting the elements
# that means in min heap esch time the minimum value pops out so that it used to form an sort the any array from the popped elements
# or else this min heap tree used to find k largest values by popping the all minimum elements from the tree so that needed k maximum elements remains in the tree.
def parent(i):
    return (i-1)//2
def left_child(i):
    return 2*i+1 
def right_child(i):
    return 2*i+2
def heapify(arr,n,i):
    # this heapify is helper function to maintain heap property for every chages in the tree.
    # after every swapping or popping of elements need to call heapify to place back the tree into heap structure.
    # in heap data structure all parent elements are at the starting part of array.
    # and remaining are placed as leafs.
    # first lets heapify the parent values in the array into min heap tree format such that from those parent values smaller value should be at root position
    # and childs are greater than root.
    # once they are placed then traversing through entire array from backwards i.e. leaf values, such that swapping each ith element with root value and call heapify to maintain heap property back for the changes.
    # similary all smaller elements places to leaves and larger elements left at root and its child, then return the array.
    # this minheap helps to get k largest elements in the array and sorting the array in increasing order with less time complexity.
    smallest=i
    
    if left_child(i)<n and arr[left_child(i)]<arr[smallest]:
        smallest=left_child(i)
    if right_child(i)<n and arr[right_child(i)]<arr[smallest]:
        smallest=right_child(i)
    # smallest
    if smallest!=i:
        arr[smallest],arr[i]=arr[i],arr[smallest]
        heapify(arr,n,smallest)
def min_heap(arr,n):
    # here our aim is to sort the array so that each value from min heap which pops out store that popped value.
    # building heap tree with parent values first, and then start with entire array.
    for i in range((n-1)//2,-1,-1):
        heapify(arr,n,i)
    
    for i in range(n-1,-1,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
        # here swapping every ith value with 0th root
        # such that bringing smaller elements down and checking heap property at each iteration.
        
def kth_largest(arr,k):
    for i in range(k):
        print(arr[i],end=' ')

arr=[12,3,14,1,35,17,7,6,26,4,15,27]
n=len(arr)
min_heap(arr,n)
print(arr)
kth_largest(arr,3)
