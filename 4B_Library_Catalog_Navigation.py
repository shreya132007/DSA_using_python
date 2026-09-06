"""
TOPIC ;- Library Catalog Navigation

A university library stores book records in a hierarchical structure, where each book category is connected to
its subcategories and individual books. To efficiently navigate and organize the catalog, the library represents
the records using a Binary Tree.
Develop a Binary Tree to represent the library catalog and implement the following recursive traversal
techniques:
1. Inorder Traversal - Displays book categories in sorted navigation order.
2. Preorder Traversal - Displays the root category before its subcategories, useful for creating a catalog
structure.
3. Postorder Traversal - Displays subcategories before the parent category, useful for safely deleting or
archiving catalog entries.
"""

# Library Catalog Navigation using Binary Tree
# Inorder, Preorder and Postorder Recursive Traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    n = input("Enter category/book (0 to stop): ")

    if n == "0":
        return None

    root = Node(n)

    print(f"Enter left of {n}:")
    root.left = create()

    print(f"Enter right of {n}:")
    root.right = create()

    return root


# Preorder: Root -> Left -> Right
def preorder(root):
    if root is not None:
        print(root.data, end=" -> ")
        preorder(root.left)
        preorder(root.right)


# Inorder: Left -> Root -> Right
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" -> ")
        inorder(root.right)


# Postorder: Left -> Right -> Root
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" -> ")


# Main Program
root = create()

print("\nPreorder Traversal:")
preorder(root)

print("\n\nInorder Traversal:")
inorder(root)

print("\n\nPostorder Traversal:")
postorder(root)