class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val=key
def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def search(root,key):
    if root.val==key:
        print("found")
    elif key<root.val:
        if root.left==None:
            print("not found")
        else:
            root.left=search(root.left,key)
    elif key>root.val:
        if root.right==None:
            print("not found")
        else:
            root.right=search(root.right,key)
    else:
        print("not found")
def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.val,end=" ")
        Inorder(root.right)
r=Node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
Inorder(r)
search(r,20)