# check if a given binary tree is sum tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 

class BT:
    def __init__(self):
        self.root=None 
    def insert_node(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
        else:
            self.insert_recursively(self.root,data)

    def insert_recursively(self,node,data):
        if data<node.data:
            if not node.left:
                node.left=Node(data)
            else:
                self.insert_recursively(node.left,data)
        else:
            if not node.right:
                node.right=Node(data)
            else:
                self.insert_recursively(node.right,data)
    #check if given binary tree is sum tree
    # where the value of root node eqauls to sum of left and right subtrees.
    #  if tree is empty then said to be 0.
#     def sum(self,node):
#         #In this function sum the all nodes of sub trees.
#         if node is None:
#             return 0 
#         return self.sum(node.left) + node.data+ self.sum(node.right) 
#     def is_sum_tree(self,node):
#         if node.data==None and node.left==None and node.right==None:
#             return 1 #it means it is a leaf node
#         ls=self.sum(node.left)
#         rs=self.sum(node.right)
# need to check the sum of left and right sub tree eqauls to root node data.
#         if node.data==(ls+rs) and self.is_sum_tree(node.left) and self.is_sum_tree(node.right):
#             return 1
#         return 0
#     def is_sum_tree(self,node):
#         if node is None:
#             return 0 
#         if node.left is None and node.right is None:
#             #it means node is a leaf node 
#             return node.data 
#         left_sum=self.is_sum_tree(node.left)
#         right_sum=self.is_sum_tree(node.right)

#         total_sum_tree=(node.data==left_sum+right_sum)
#         if total_sum_tree and self.is_sum_tree(node.left) and self.is_sum_tree(node.right):
#             return left_sum + node.data +right_sum
#         return 0
#     def sum(self,root):
#         if root is None:
#             return 0 
#         else:
#             return self.sum(root.left)+ root.data + self.sum(root.right)
    
#     def is_sum_tree(self,node):
#         if node.data==None and node.left==None and node.right==None:
#             return 1
#         ls=self.sum(node.left)
#         rs=self.sum(node.right)
#         if (node.data==(ls+rs) and self.is_sum_tree(node.left) and self.is_sum_tree(node.right)):
#             return 1 
    #     return 0
    def is_sum_tree(self, node):
        # Helper function to calculate sum of subtree and check if it is a sum tree
        def check_sum_tree(node):
            if node is None:
                return 0, True
            
            if node.left is None and node.right is None:
                return node.data, True
            
            left_sum, is_left_sum_tree = check_sum_tree(node.left)
            right_sum, is_right_sum_tree = check_sum_tree(node.right)
            
            is_current_sum_tree = (node.data == left_sum + right_sum)
            
            return left_sum + right_sum + node.data, is_left_sum_tree and is_right_sum_tree and is_current_sum_tree

        _, is_sum_tree = check_sum_tree(node)
        return is_sum_tree
    def print_order(self,root):
        #  if self.root:
        # printing recursion 
        if root is None:
            return    
       
        print(root.data,end=' ')
        self.print_order(root.left)
        self.print_order(root.right)
t=BT()        
# t.insert_node(62)
# t.insert_node(7)
# t.insert_node(13)
# t.insert_node(5)
# t.insert_node(17)
# t.insert_node(9)
# t.insert_node(11)
t.insert_node(26)
t.insert_node(10)
t.insert_node(3)
t.insert_node(4)
t.insert_node(6)
t.insert_node(3)
t.print_order(t.root)
t.is_sum_tree(t.root)
print()
if t.is_sum_tree(t.root):
    print('given tree is sum tree')
else:
    print('given tree is not sumtree')


                
