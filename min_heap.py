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
