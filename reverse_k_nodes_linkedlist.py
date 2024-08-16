class node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
def buildlinkedlist(values):
    if not values:
        return None
    head=node(values[0]) #head intiating with null value position.
    curr=head #curr pointer starts from head 
    for i in values[1:]:
        curr.next=node(i)
        curr=curr.next 
    return head
def printlist(head):
    curr=head 
    values=[]
    while curr:
        values.append(curr.data)
        curr=curr.next 
    print('->'.join(map(str,values)))
###########################################################################        
def reverse_k_nodes(head,k):
    if head is None:
        return None
    curr=head 
    prev=None 
    next=None 
    count=0 
    while curr and count<k:
        # need to reverse the list of nodes
        next=curr.next 
        curr.next=prev 
        prev=curr 
        curr=next 
        count+=1 
    if head:
        head.next=curr 
    #that means k+1 th node will be curr
    count=0 
    while curr and count<k-1:
        curr=curr.next 
        count=count+1 
    if curr:
        curr.next=reverse_k_nodes(curr.next,k)
    return prev 
def push(head,data):
    new_node=node(data)
    new_node.next=head 
    head=new_node
    return head
def printList(head):
    curr=head 
    count=0
    while curr:
        print(curr.data,end='->')
        curr=curr.next
        count=count+1

head=None 
head=buildlinkedlist([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(100,0,10):
    head=push(head,i)

printlist(head)
print()
reverse_k_nodes(head,3)
printlist(head)

######################################################################################
# merge k sorted lists
class node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class mergesortedlists:
    def mergetwolists(self,a,b):
        result=None
        if a is None:
            return b 
        if b is None:
            return a 
        # while a and b:
        if a.val<=b.val:
            result=a 
            result.next=self.mergetwolists(a.next,b)
        else:
            result=b 
            result.next=self.mergetwolists(a,b.next)
        return result
    def mergeklists(self,arr,last):
        # need to merge the all the lists.
        # so consider first pointer and last pointer.
        # compare the first and last pointer values sort them based on the previous function pointer shifts one after another.
        while last!=0:
            i=0 
            j=last 
            while i<j:
                arr[i]=self.mergetwolists(arr[i],arr[j])
                # once values are compared then move the pointers at once.
                i=i+1 
                j=j-1 
                if i>j:
                    last=j 
        return arr[0]

def mergesortedlist(a,b):
    result=None
    # this function is helper function to compare both values in the lists and moves pointer next variable.
    if a is None:
        return b 
    if b is None:
        return a 
    # if a and b:
    if a.data <= b.data:
        result=a
        result.next=mergesortedlist(a.next,b)
    else:
        result=b
        result.next=mergesortedlist(a,b.next)
    return result
def mergeksortedlists(arr,last):
    while last!=0:
        i=0
        j=last 
        while i<j:
            arr[i]=mergesortedlist(arr[i],arr[j])
            i=i+1 
            j=j-1 
            if i>=j:
                last=j 
    return arr[0]
from queue import PriorityQueue 
def mergeklists(arr,k):
    pq=PriorityQueue()

    for i in range(k):
        if arr[i] is not None:
            pq.put((arr[i].data,i))
    head=node(None)
    curr=head 
    while not pq.empty():
        val,i=pq.get()
        curr.next=node(val)
        curr=curr.next 
        if arr[i].next is not None:
            pq.put((arr[i].next.data,i))
            arr[i]=arr[i].next
    return head.next
    # using priority queue.
    # pq=PriorityQueue()

    # put()the all elements of k lists into the arr
    # get the each element and check for next element in arr if available then add to priority queue.
    # for i in range(k):
    #     if arr[i] is not None:
    #         pq.put((arr[i].data,i))
    # dummy=node(None)
    # curr=dummy 
    # while not pq.empty():
    #     val,i=pq.get() 
    #     curr.next=node(val)
    #     curr=curr.next
    #     if arr[i].next is not None:
    #         pq.put((arr[i].next.data,i))
    #         arr[i]=arr[i].next 
    # return dummy.next
    
    # solving using min heap 
    # creating the heapq and then appending the values to it.
    # pop the root minimum and add it to the result. if any next element is present then iterate to it and add it to the queue.
    import heapq 
    queue=[]
    for i in range(k):
        if arr[i] is not None:
            heapq.heappush(queue,(arr[i].data,arr[i]))
    dummy=node(0)
    last=dummy 
    while queue:
        curr=heapq.heappop(queue)[1]
        # here curr is dummy that is not present in result so need to attach the output with next of dummy.
        last.next=curr
        last=last.next
        if curr.next is not None:
            heapq.heappush(queue,(curr.next.data,curr.next))
    return dummy.next
def printlist(head):
    curr=head
    while curr:
        print(curr.data,end='->')
        curr=curr.next 
    print()

if __name__=='__main__':
    k=3 
    n=4
    # ll=mergesortedlists()
    arr=[0 for i in range(k)]
    arr[0]=node(1)
    arr[0].next=node(3)
    arr[0].next.next=node(5)
    arr[0].next.next=node(7)

    arr[1]=node(2)
    arr[1].next=node(4)
    arr[1].next.next=node(6)
    arr[1].next.next.next=node(8)

    arr[2]=node(6)
    arr[2].next=node(8)
    arr[2].next.next=node(10)
    arr[2].next.next.next=node(12)

    # head=mergeksortedlists(arr,k-1)
    head=mergeklists(arr,k)
    printlist(head)
    
