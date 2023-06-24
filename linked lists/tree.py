'''to implement hierarchical data or info we use tree DS
In a tree , every node can have n number of children
height of a node = countlevels 
depth of a node = count up levels
if a parent having two children we call them as left child or right child
three can be divided into two parts -  we call them as left subtree and right
subtree 
Note - whenever we perform any operation in tree we have to complete left first
and move to right
leaf node has no children
        o                 -  -   -  1
      /   \               -  -   -  2
     o      o            
    / \    /  \
   o   o  o    o          -  -   - 3
   
   any node can only have 2 nodes
   
   perfect binary tree is binary tree where interior nodes have two children 
   and all leaves are all of same level.
   
   Binary tree traversals
   
   Level order
   Depth order
   Inorder
   Preorder
   Postorder
   
                           Binary Search Tree
Every node that is less than its parent lies its left side and vice versa
50 10 15 16 500 300 200 1 2 3 



    '''
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
      else:
         self.data = data
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))      