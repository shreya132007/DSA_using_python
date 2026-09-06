#create binary tree and perform inorder, preorder and postorder recursive traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    n = int(input("enter data to create node (0 to stop):"))

    if n == 0:
        return None

    root = Node(n)

    print(f"enter left of {n}:")
    root.left = create()

    print(f"enter right of {n}:")
    root.right = create()

    return root


# Root -> Left -> Right
def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


# Left -> Root -> Right
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


# Left -> Right -> Root
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


root = create()

print("preorder traversal is:\n")
preorder(root)

print("inorder traversal is:\n")
inorder(root)

print("postorder traversal is:\n")
postorder(root)