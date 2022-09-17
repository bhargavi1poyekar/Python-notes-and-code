'''
Trees
'''

# class TreeNode:
#     def __init__(self, data, children=[]):
#         self.data=data
#         self.children=children
    
#     def __str__(self,level=0):
#         ret=' '*level+str(self.data)+'\n'
#         for child in self.children:
#             ret+=child.__str__(level+1)
#         return ret
    
#     def addChild(self, TreeNode):
#         self.children.append(TreeNode)

# tree=TreeNode('Drinks',[])

# cold=TreeNode('Cold',[])

# hot=TreeNode('Hot',[])

# tree.addChild(cold)
# tree.addChild(hot)

# tea=TreeNode('Tea',[])
# coffee=TreeNode('Coffee',[])

# cola=TreeNode('Cola',[])

# cold.addChild(cola)
# hot.addChild(tea)
# hot.addChild(coffee)
# print(tree)

'''
Binary Tree- Tree in which each node has atmost 2 children, left and right

--> BST, Heap Tree, AVL Tree, Red black tree, Syntax tree, all are binary trees

Types: 

Full Binary Tree - Each node has either 2 or 0 children
Perfect Binary Tree - Each node has 2 children, all leaf nodes on same level
Complete Binary Tree - All levels are completely filled except last level
Balanced Binary Tree- All leaf nodes at same level


# Create Binary Tree:
# - With linked list: Node has 3 components- data, left child and right child 
# - With list: Leave index 0 blank, to make calculations easier.
# - Store left and right child-with formula - left(2x), right->(2X+1) , X=> root nodes location

# Operations on Binary Tree:
# - Creation of Binary Tree
# - Insertion of Node
# - Deletion of Node
# - Search for a value
# - Traverse all Nodes
# - Deletion of tree 

# Traversal Of Binary Tree:

DFS:
Preorder - vlr
Inorder - lvr
Postorder- lrv

BFS: 
LevelOrder Traversal

'''

class TreeNode:
    def __init__(self, data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

newBT=TreeNode('Drinks') #---------> O(1)  
Hot=TreeNode('Hot')
Cold=TreeNode('Cold')
newBT.leftChild=Hot
newBT.rightChild=Cold
Tea=TreeNode('tea')
Coffee=TreeNode('coffee')
Hot.leftChild=Tea
Hot.rightChild=Coffee

def preorder(rootNode): # VLR
    if rootNode==None:
        return
    print(rootNode.data)
    preorder(rootNode.leftChild)
    preorder(rootNode.rightChild)

# preorder(newBT)

# def inorder(rootNode): # LVR
#     if not rootNode:
#         return
#     inorder(rootNode.leftChild)
#     print(rootNode.data)
#     inorder(rootNode.rightChild)

# inorder(newBT)

# def postorder(rootNode): # LRV
#     if not rootNode:
#         return
#     postorder(rootNode.leftChild)
#     print(rootNode.data)
#     postorder(rootNode.rightChild)

# postorder(newBT)

def SearchBT(root,val):
    
    if not root:
        return
    if root.data==val:
        print("Item Found")
        return
    SearchBT(root.leftChild,val)
    SearchBT(root.rightChild,val)

# preorder(newBT)
if(SearchBT(newBT,'Drink')==None):
    print('Not Found')