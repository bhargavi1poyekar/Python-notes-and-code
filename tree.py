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

# 144
# def preorder(rootNode): # VLR
#     if rootNode==None:
#         return
#     print(rootNode.data)
#     preorder(rootNode.leftChild)
#     preorder(rootNode.rightChild)

# preorder(newBT)

# 94
# def inorder(rootNode): # LVR
#     if not rootNode:
#         return
#     inorder(rootNode.leftChild)
#     print(rootNode.data)
#     inorder(rootNode.rightChild)

# inorder(newBT)

# 145
# def postorder(rootNode): # LRV
#     if not rootNode:
#         return
#     postorder(rootNode.leftChild)
#     print(rootNode.data)
#     postorder(rootNode.rightChild)

# postorder(newBT)

# def SearchBT(root,val):
    
#     if not root:
#         return
#     if root.data==val:
#         print("Item Found")
#         return
#     SearchBT(root.leftChild,val)
#     SearchBT(root.rightChild,val)

# # preorder(newBT)
# if(SearchBT(newBT,'Drink')==None):
#     print('Not Found')

'''
104. Maximum Depth of Binary Tree
'''
#  def maxDepth(self, root: Optional[TreeNode]) -> int:

#         if not root:
#             return 0
        
#         left_depth=self.maxDepth(root.left)
#         right_depth=self.maxDepth(root.right)
#         return max(left_depth,right_depth)+1

'''
111. Minimum Depth of Binary Tree
'''
# def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         if not root.left:
#             return 1+self.minDepth(root.right)
#         elif not root.right:
#             return 1+self.minDepth(root.left)
#         else:
#             return 1+ min(self.minDepth(root.right),self.minDepth(root.left))

'''
1026. Maximum Difference Between Node and Ancestor
'''
# def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

#         if not root:
#             return 0

#         def dfs(root, cur_max, cur_min):
#             if not root:
#                 return cur_max-cur_min
            
#             cur_max=max(cur_max,root.val)
#             cur_min=min(cur_min,root.val)

#             left=dfs(root.left,cur_max,cur_min)
#             right=dfs(root.right,cur_max,cur_min)

#             return max(left,right)
        
#         return dfs(root,root.val,root.val)
        
'''
102. Binary Tree Level Order Traversal
'''

# def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []

#         queue=deque([root])
#         ans=[]
#         while queue:
#             length=len(queue)
#             level=[]
#             for _ in range(length):
#                 node=queue.popleft()
#                 level.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             ans.append(level)
#         return ans


'''
938. Range Sum of BST

'''
# def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

#         if not root:
#             return 0
        
#         ans=0
#         if root.val >=low and root.val<=high:
#             ans+=root.val

#         if low<root.val:
#             ans+=self.rangeSumBST(root.left,low,high)
#         if root.val<high:
#             ans+=self.rangeSumBST(root.right,low,high)
        
#         return ans

'''
701. Insert into a BST
'''

# def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root:
#             return TreeNode(val)
            

#         if root.val>val:
#             root.left=self.insertIntoBST(root.left,val)
#         elif root.val<val:
#             root.right=self.insertIntoBST(root.right,val)
    
#         return root


'''
1161. Maximum Level Sum of Binary Tree 
'''
# def maxLevelSum(self, root: Optional[TreeNode]) -> int:
#         queue=deque([root])
#         max_sum=float('-inf')
#         max_level=0
#         level=1
#         while queue:
#             nodes=[]
#             for _ in range(len(queue)):
#                 node=queue.popleft()
#                 nodes.append(node.val)

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#             # print(nodes)
#             level_sum=sum(nodes)
#             if level_sum>max_sum:
#                 max_sum=level_sum
#                 max_level=level
#             level+=1

#         return max_level

'''
1609
'''
# def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
#         queue=deque([root])
#         level=0

#         while queue:
            
#             size=len(queue)
#             if level%2==1:
#                 queue.append(TreeNode(float('-inf')))
#             else:
#                 queue.append(TreeNode(float('inf')))
           
#             for _ in range(size):
#                 node=queue.popleft()

#                 if level%2!=0:
#                     if (node.val)%2!=0 or node.val<=queue[0].val:
#                         return False 

#                 if level%2==0:
#                     if (node.val)%2==0 or node.val>=queue[0].val:
#                         return False 
                
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#             queue.popleft()
#             level+=1
            
#         return True


'''
113. Path sum 2
'''

#  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

#         valid_paths=[]
#         self.dfs(root,valid_paths,[],targetSum)
#         return valid_paths

#     def dfs(self, root, valid_paths, curr_path, remain_sum):

#         if not root: # If no root return
#             return
        
#         curr_path.append(root.val) # add current node in curr_path
        
#         # if curr node is equal to remain sum for target, and if lead node
#         if root.val==remain_sum and not root.left and not root.right: 
#             valid_paths.append(list(curr_path)) # append curr path to valid paths
            
#         else:
#             # if not leaf node, go to left or right
#             self.dfs(root.left,valid_paths,curr_path,remain_sum-root.val) 
#             self.dfs(root.right,valid_paths,curr_path,remain_sum-root.val)

#         # Remove curr node from curr_path
#         curr_path.pop()
#         return

        
'''
1372.Longest Zigzag path in binary tree
'''
# def longestZigZag(self, root: Optional[TreeNode]) -> int:

#         longestpath=0

#         def dfs(root,parentLeft,steps):
#             nonlocal longestpath
#             if root:
#                 longestpath=max(longestpath,steps)

#                 if parentLeft:
#                     dfs(root.left,True,1)
#                     dfs(root.right,False,steps+1)
#                 else:
#                     dfs(root.left,True,steps+1)
#                     dfs(root.right,False,1)

        
#         dfs(root,False,0)
#         dfs(root,True,0)
#         return longestpath

'''
700. Search in a Binary Search Tree
'''
# def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

#         if not root:
#             return
        
#         if root.val==val:
#             return root
        
#         if root.val>val:
#             return self.searchBST(root.left,val)
#         else:
#             return self.searchBST(root.right,val)
    
