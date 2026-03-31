
# Binary Search Tree (BST)
# A BST is a binary tree where for every node:
# - All elements in the left subtree are smaller than the node
# - All elements in the right subtree are greater than the node

# This property must be true for every node recursively

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def inorder_traversal(self, node):
        if not node:
            return
        
        self.inorder_traversal(node.left)
        print(node.data, end=' ')
        self.inorder_traversal(node.right)

    # Without using Recursion 
    def insertion(self, val):
        node = TreeNode(val)

        if self.root == None:
            self.root = node
            return self.root
        
        current = self.root
                
        while True:
            if node.data >= current.data:
                if not current.right:
                    current.right = node
                    break
                current = current.right
            else:
                if not current.left:
                    current.left = node
                    break
                current = current.left
        
        return self.root

    # -----------------------------------------------------------------------
    # Using Recursion 
     
    # def insertion(self, node, val):
    #     if not node:
    #         return TreeNode(val)
        
    #     if val < node.data:
    #         node.left = self.insertion(node.left, val)
    #     else:
    #         node.right = self.insertion(node.right, val)
        
    #     return node
    # -----------------------------------------------------------------------

    # Searching a node 
    # Without using Recursion 
    def search_node(self, val):
        if self.is_empty():
            return False
        
        current = self.root
        while current:
            if val == current.data:
                return True
            elif val < current.data:
                current = current.left
            else:
                current = current.right
        
        return False
    
    # -----------------------------------------------------------------------
    # Using Recursion 
    # def search_node(self, node, val):
    #     if not node:
    #         return False    
        
    #     if node.data == val:
    #         return True        
        
    #     if val < node.data:
    #         return self.search_node(node.left, val)
        
    #     return self.search_node(node.right, val)
    # -----------------------------------------------------------------------

    # Without using recursion 
    def deletion(self, val):
        
        # Check Empty
        if self.is_empty():
            raise Exception("Tree is already empty!!")
        
        # Deletion in single node tree 
        if not self.root.right and not self.root.left:
            if self.root.data == val:
                self.root = None
                return self.root
            print("Node not found!!!..")

        # Deletion in multiple node tree 
        parent = None
        current = self.root

        while current:
            if current.data == val:
                break
            parent = current
            if val < current.data:
                current = current.left
            else:
                current  = current.right

        if current is None:
            print("Node Not Found!!")
            return self.root
        
        # Deleting root node
        if parent is None:
            # Only root exists OR root has one child
            if current.left is None:
                self.root = current.right
                return self.root
            elif current.right is None:
                self.root = current.left
                return self.root
                
        # Deletion of leaf node 
        if current.left is None and current.right is None:
            if parent:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
            return self.root
        
        # Deletion of Node with One child
        if current.left is None or current.right is None:
            child = current.left if current.left else current.right

            if parent:
                if parent.left == current:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

            return self.root
        
        # Double child Node Deletion 
        parent = current
        child = current.right

        while child.left:
            parent = child
            child = child.left
        
        current.data = child.data

        # Delete successor node
        if parent.left == child:
            parent.left = child.right
        else:
            parent.right = child.right

        return self.root
    
    # -----------------------------------------------------------------------
    # Using Recursion 
    # def deletion(self, node, val):
    #     if not node:
    #         return None
        
    #     if val<node.data:
    #         node.left = self.deletion(node.left, val)
    #     elif val>node.data:
    #         node.right = self.deletion(node.right, val)
    #     else:
    #         if not node.left:
    #             return node.right
    #         if not node.right:
    #             return node.left  

    #         succ = node.right
    #         while succ.left:
    #             succ = succ.left

    #         node.val = succ.val
    #         node.right = self.deletion(node.right, succ.data)
        
    #     return node
    # -----------------------------------------------------------------------

        
if __name__ == '__main__':
    bst = BST()

    while True:
        print("\n--- BST MENU ---")
        print("1. Insert")
        print("2. Search")
        print("3. Inorder Traversal")
        print("4. Delete")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter value to insert: "))
            bst.insertion(val)

        elif choice == 2:
            val = int(input("Enter value to search: "))
            print("Found!" if bst.search_node(val) else "Not Found!")

        elif choice == 3:
            print("Inorder Display:", end=' ')
            bst.inorder_traversal(bst.root)
            print()

        elif choice == 4:
            val = int(input("Enter value to delete: "))
            bst.deletion(val)

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")




