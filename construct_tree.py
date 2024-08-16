# # construct a tree from the preorder and inorder arr
class node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None
# preindex=0
def construct_tree(inorder,preorder,start,end):
    # global preindex
    # start and end represents 0 to end of the array of nodes.
    if start>end:
        return None 
    # approach is need to construct a binary tree.
    # now with the help of preorder array, we can find the root in that array and finding that element position in  the inorder.
    # let's create a tree node it contains the root and then making left and child.
    tnode=node(preorder[construct_tree.preindex])
    construct_tree.preindex=construct_tree.preindex+1
    if start==end:
        # it means if it doesn't have children then return node
        return tnode
    # now find the tnode data position in the inorder and to divide the left and right sub trees.
    inIndex= search(inorder, start,end,tnode.data)
    print(inIndex)
    tnode.left=construct_tree(inorder,preorder,start,inIndex-1)
    tnode.right=construct_tree(inorder,preorder,inIndex+1,end)
    return tnode

def search(arr,start,end,value):
    for i in range(start,end+1):
        if arr[i]==value:
            return i
def printinorder(root):
    if root is None:
        return 
    printinorder(root.left)
    print(root.data,end=' ')
    printinorder(root.right)
# def printInorder(node):
#     if node is None:
#         return
     
#     # first recur on left child
#     printInorder(node.left)
     
#     # then print the data of node
#     print (node.data,end=' ')
 
#     # now recur on right child
#     printInorder(node.right)
inorder=['D','B','E','A','F','C']
# static variable
# construct_tree.preindex=0
construct_tree.preindex=0
preorder=['A','B','D','E','C','F']
Node=construct_tree(inorder,preorder,0,len(inorder)-1)
printinorder(Node)
# printInorder(Node)
##########################################################################################################################
# boundary traversal of the binary tree 
# left nodes first then child leaves and then after right nodes.
# boundary of tree prints the root node and left nodes first, then after traverse through leaves nodes
# and last print the right traversal nodes.

class node:
    def __init__(self,data):
        self.data=data
        self.left=None 
        self.right=None 
def print_leaves(root):
    # the nodes to be considered as leaves nodes if there is no children to them.
    # first need to traverse last to the tree
    if root:
        print_leaves(root.left)
        if root.left is None and root.right is None:
            print(root.data)
        print_leaves(root.right)
def printleftboundary(root):
    if root:
        # print(root.data)
        if root.left:
            # it comes on top-down approach to print root data first
            # and again traverse through left and print them.
            print(root.data)
            printleftboundary(root.left)
        elif root.right:
            print(root.data)
            printleftboundary(root.right)
        # here not using else to avoid the duplicates enter into the output.
def printrightboundary(root):
    if root:
        if root.right:
            # here it's traverse from bottom-top as covering the leaf nodes and going to top from right side of the tree.
            # so first traverse the nodes first and printing data next.
            printrightboundary(root.right)
            print(root.data)
    elif root.left:
        printrightboundary(root.left)
        print(root.data)
def print_tree(root):
    if root:
        print(root.data)
        # traversal starts from top of root and left and left most nodes and leaves nodes and then right boundary.
        printleftboundary(root.left)
        print_leaves(root.left)
        print_leaves(root.right)
        printrightboundary(root.right)

root=node(20)
root.left=node(14)
root.left.left=node(7)
root.left.right=node(15)
root.left.left.left=node(3)
root.left.left.right=node(10)
root.left.right.left=node(12)
root.left.right.right=node(17)
root.right=node(27)
root.right.left=node(12)
root.right.right=node(34)
print_tree(root)

