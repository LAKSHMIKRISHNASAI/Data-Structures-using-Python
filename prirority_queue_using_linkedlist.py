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
        
