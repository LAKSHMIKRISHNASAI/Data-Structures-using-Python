class node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class linkedlist:
    def __init__(self):
        self.head=None 
    def swap_nodes(self):
        # prev=None
        # curr=self.head 
        # # count=0
        # # next=None
        # while curr2:
        #     count=count+1
        #     next=curr.next #this stores the next node 
        #     curr.next=prev 
        #     prev=curr 
        #     curr=next 

        # swapping just adjacent pair of nodes.

        curr=self.head 
        # need to check curr and next element both are present is list.
        if curr is None:
            return
        while curr and curr.next:
            if curr.data!=curr.next.data:
                # if both nodes are same then no need to swap.
                curr.data,curr.next.data=curr.next.data,curr.data 
            curr=curr.next.next #traverse two nodes far at every iteration.
    def insert_node(self,data):
        new_node=node(data)
        new_node.next=self.head 
        self.head=new_node 
    def print_list(self):
        curr=self.head 
        while curr:
            print(curr.data,end='->')
            curr=curr.next 
    # reverse a sublist in the linked list from m to n.
    # def reversesublist(self,m,n):
        # m and n represents the position/index of linkedlist.
        # need to keep track of indices.
        # curr=self.head 
        # dummy=node(0)
        # dummy.next=self.head
        # prev=dummy
        # # # visited=[True]
        # # prev=None
        # # count=0
        # # first traverse through the m index position.
        # for _ in range(m-1):
        #     prev=prev.next 
        
        # reverse_start=prev.next 
        # curr=reverse_start.next
        # for _ in range(n-m):
        #     reverse_start.next=curr.next
        #     curr.next=prev.next
        #     prev.next=curr 
        #     curr=reverse_start.next 
        # return dummy.next
        
            # return
#         dummy=node(0)
#         dummy.next=self.head
#         prev=dummy 
# # 0,1,2 3-prev, 4-curr
#         for _ in range(m-1):
#             prev=prev.next 
#         start_reversed=prev.next #points to next node 
#         curr=start_reversed.next #prev.next.next
#         for _ in range(n-m):
#             start_reversed.next=curr.next 
#             curr.next=prev.next 
#             prev.next=curr 
#             curr=start_reversed.next 
#         return dummy.next
    def reverse_k_alt_nodes(self,head,k):
        if head is None:
            return None
        # approach -  first need to starts the counter till kth all nodes will reverse.
        # and need to remain same the next k nodes and again call the recursively revrsing k nodes.
        # to reverse the k nodes needs prev pointer, current pointer points on head, next pointer and count variable.
        prev=None 
        curr=head 
        next=None 
        count=0
        while curr and count<k:
            next=curr.next #it always stores the next node
            curr.next=prev #curr address connecting to previous node.
            prev=curr #prev is assigned as current node.
            curr=next #and after that moving to the next node it looks like curr=curr.next.
            count=count+1 
        # now from 0 to k-1 nodes are reversed, and then need to make the head points to the kth node and assigning current node as k+1 th node.
        if head is not None:
            head.next=curr
        # now again starts the counter until it skips k nodes without reversing.
        count=0 
        while curr and count<k-1:
            curr=curr.next 
            count=count+1 
        if curr is not None:
            curr.next=self.reverse_k_alt_nodes(curr.next,k)
        # at final prev stores the current nodes.
        return prev
    def buildlinkedlist(self,values):
        if not values:
            return None
        head=node(values[0])
        curr=head
        for i in values[1:]:
            curr.next=node(i)
            curr=curr.next 
        return head
    def printList(self):
        curr=self.head 
        values=[]
        while curr:
            values.append(curr.data)
            curr=curr.next 
        print('->'.join(map(str,values)))

def printlist(head):
    curr=head 
    values=[]
    while curr:
         values.append(curr.data)
         curr=curr.next
    print('->'.join(map(str,values)))
ll=linkedlist()
head=None
# ll.insert_node(10)
# ll.insert_node(20)
# ll.insert_node(30)
# ll.insert_node(40)
# ll.insert_node(50)
# ll.insert_node(60)
# ll.insert_node(70)
# ll.insert_node(80)
# values=[]
ll.head=ll.buildlinkedlist([1, 2, 3, 4, 5, 6, 7, 8, 9])
printlist(ll.head)
# for i in range(100,0,10):
#     print(ll.insert_node(i))
# print(head)

# ll.printList()
# print()
# ll.swap_nodes()
# ll.print_list()  
# print()
# # ll.reversesublist(2,6) 
# # head=None
ll.reverse_k_alt_nodes(ll.head,3)
ll.print_list()  
