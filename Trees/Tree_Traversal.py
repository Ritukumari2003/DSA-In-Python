from collections import deque

# Class to create a node of the binary tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    # Preorder Traversal (Root -> Left -> Right)
    def preorder_traversal(self, node):
        if not node:
            return
        
        print(node.data, end=' ')
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)
    
    # Inorder Traversal (Left -> Root -> Right)
    def inorder_traversal(self, node):
        if not node:
            return
        
        self.inorder_traversal(node.left)
        print(node.data, end=' ')
        self.inorder_traversal(node.right)
    
    # Postorder Traversal (Left -> Right -> Root)
    def postorder_traversal(self, node):
        if not node:
            return
        
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.data, end=' ')
    
    # Level Order Traversal (Breadth-First Search)
    def levelorder_traversal(self, node):
        if not node:
            return
        
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            print(curr.data, end=' ')
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:   
                queue.append(curr.right)

tree = Tree()

tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)

print("Preorder:")
tree.preorder_traversal(tree.root)

print("\nInorder:")
tree.inorder_traversal(tree.root)

print("\nPostorder:")
tree.postorder_traversal(tree.root)

print("\nLevel Order:")
tree.levelorder_traversal(tree.root)