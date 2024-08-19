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

            
            
        
        
