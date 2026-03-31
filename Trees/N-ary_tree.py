# N-ary Tree:
# A tree data structure where each node can have zero or more children

# Unlike Binary Tree:
# A binary tree allows at most 2 children (left and right)
# An N-ary tree allows any number of children

# Structure:
# Each node contains:
# 1. Data (value of the node)
# 2. A list of children nodes

from collections import deque
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

# Preorder Traversal (Root → Children)
# Visit the current node first, then recursively visit all its children
def preorder_traversal(node):
    if not node:
        return None
    
    print(node.data, end = ' ')

    for child in node.children:
        preorder_traversal(child)

# Postorder Traversal (Children → Root)
# Recursively visit all children first, then visit the current node
def postorder_traversal(node):
    if not node:
        return None

    for child in node.children:
        postorder_traversal(child)
    
    print(node.data, end = ' ')

# Level Order Traversal (Breadth-First Search)
# Traverse the tree level by level using a queue
# Add all children of a node to the queue for processing
def levelorder_traversal(node):
    if not node:
        return None
    
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        print(curr.data, end=' ')

        for child in curr.children:
            queue.append(child)
    
# Creating a N-Ary tree 
root = TreeNode(10)
node1 = TreeNode(20)
node2 = TreeNode(30)
node3 = TreeNode(40)
root.children = [node1, node2, node3]
node1.children = [TreeNode(50), TreeNode(60)]
node2.children = [TreeNode(70)]
node3.children = [TreeNode(80), TreeNode(90), TreeNode(100)]

preorder_traversal(root)
print()
postorder_traversal(root)
print()
levelorder_traversal(root)
print()

