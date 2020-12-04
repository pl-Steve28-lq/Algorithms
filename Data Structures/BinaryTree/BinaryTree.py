class BinaryTree:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def inorder(N):
    if type(N) == int: print(N)
    elif N: inorder(N.left); print(N.item); inorder(N.right)

def preorder(N):
    if type(N) == int: print(N)
    elif N: print(N.item); preorder(N.left); preorder(N.right)

def postorder(N):
    if type(N) == int: print(N)
    elif N: postorder(N.left); postorder(N.right); print(N.item)
