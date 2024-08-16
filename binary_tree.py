class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None 
        
class BT:
    def __init__(self):
        self.root=None 
    def insert_node(self,val):
        if self.root is None:
            self.root=Node(val)
        else:
            self.insert(self.root,val)
    def insert(self,node,val):
        if val<node.data:
            if not node.left:
                node.left=Node(val)
            else:
                self.insert(node.left,val)
        else:
            if not node.right:
                node.right=Node(val)
            else:
                self.insert(node.right,val)
    def print_tree(self,root):
        # if node is None:
        #     return
        # #lets print in inorder 
        # print_tree(node.left)
        # print(self.root.data,end=' ')
        # print_tree(node.right)
        if root is None:
            return 
        self.print_tree(root.left)
        print(root.data,end=' ')
        self.print_tree(root.right)
    def printcurrentlevel(self,node,level):
        if node is None:
            return 
        if level==1:
            print(node.data,end=' ')
        elif level>1:
            self.printcurrentlevel(node.left,level-1)
            self.printcurrentlevel(node.right,level-1)
    def print_order(self):
        h=self.height_of_tree(self.root)
        for i in range(1,h+1):
            self.printcurrentlevel(self.root,i)
            
            print(' ',end='\n')
    def height_of_tree(self,node):
        # length=0 
        if node is None:
            return 0
        else:
            lheight= self.height_of_tree(node.left)
            rheight=self.height_of_tree(node.right)
            if lheight>rheight:
                return lheight+1 
            else:
                return rheight+1 

t=BT()
# node=None
t.insert_node(10)
t.insert_node(12)
t.insert_node(4)
t.insert_node(7)
t.insert_node(11)
t.insert_node(14)
t.insert_node(3)
t.print_order()
t.print_tree(t.root)
# d=t.print_tree(t)
# for i in d:
#     print(i,end=' ')
# insertion in binary tree inorder traversal
# left to right insertion 
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None 
def insert_node(node,data):
    if node is None:
        node=Node(data)
        return
    # insert the nodes in the level order traversal
    q=[]
    q.append(node)
    while q:
        # need to traverse from left to right 
        temp_node=q[0]
        q.pop(0)
        if not temp_node.left:
            temp_node.left=Node(data)
            break 
        else:
            q.append(temp_node.left)
        if not temp_node.right:
            temp_node.right=Node(data)
            break
        else:
            q.append(temp_node.right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=' ')
        inorder(root.right)

root=Node(10)
root.left=Node(7)
root.right=Node(12)
root.left.left=Node(3)
root.left.right=Node(14)
root.right.left=Node(4)
root.right.right=Node(17)
insert_node(root,27)
inorder(root)

# the above program used to maintain the binary tree structure if any new element inserted into it.

