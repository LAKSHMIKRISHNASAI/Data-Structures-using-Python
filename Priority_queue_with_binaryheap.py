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
