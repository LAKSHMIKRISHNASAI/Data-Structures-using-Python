# # count the level/height of tree.
class node:
    def __init__(self,data):
        self.data=data 
        self.left=self.right=None 

def count_levels(root,data,level):
    if root is None:
        return 0 
    if root.data==data:
        return level 
    downlevel=count_levels(root.left,data,level+1)
    if downlevel!=0:
        return downlevel
    downlevel=count_levels(root.right,data,level+1)
    return downlevel

root=node(3)
root.left=node(2)
root.right=node(5)
root.left.left=node(1)
root.left.right=node(4)
for i in range(1,6):
    level=count_levels(root,i,1)
    if level:
        print('level of:',i,'is',count_levels(root,i,1))
    else:
        print(i,'not present in tree')
def count_nodes(root):
    if root is None:
        return 0 
    return 1+ count_nodes(root.left)+count_nodes(root.right)
def heaputil(root):
    if root is None:
        return True 
    if root.right is None:
        return root.data>=root.left.data
    else:
        if root.data>=root.left.data and root.data>=root.right.data:
            return heaputil(root.left) and heaputil(root.right)
        else:
            return False 
def complete_tree_util(root,index,number_nodes):
    if root is None:
        return True 
    if index>=number_nodes:
        return False 
    return complete_tree_util(root.left,2*index+1,number_nodes) and complete_tree_util(root.right,2*index+2,number_nodes)
def isheap(root):
    number_nodes=count_nodes(root)
    if heaputil(root) and complete_tree_util(root,0,number_nodes):
        return True 
    return False
##################################################################################################################################
