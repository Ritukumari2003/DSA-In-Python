from binary_search_tree import BST
import math

# Function to find the maximum depth (height) of the BST
# It calculates the longest path from root to any leaf node
def max_depth_BST(node):
    if node is None:
        return 0
    
    h1 = max_depth_BST(node.left)
    h2 = max_depth_BST(node.right)
    
    return max(h1, h2)+1


# Function to count total number of nodes in the BST
# It recursively counts nodes in left and right subtrees
def no_of_nodes(node):
    if node is None:
        return 0
    
    count_left = no_of_nodes(node.left)
    count_right = no_of_nodes(node.right)

    return count_left+count_right+1 


# Function to calculate sum of all node values in the BST
# It adds values of current node and its left & right subtrees
def sum_of_nodes(node):
    if node is None:
        return 0
    
    sum_left = sum_of_nodes(node.left)
    sum_right = sum_of_nodes(node.right)

    return sum_left + sum_right + node.data


# Function to validate whether a binary tree is a valid BST
# Uses range (min, max) to ensure all nodes satisfy BST property
def validate_BST(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    
    if not (min_val < node.data < max_val):
        return False
    
    return (validate_BST(node.left, min_val, node.data) and
            validate_BST(node.right, node.data, max_val))


# Function to find Lowest Common Ancestor (LCA) of two nodes in BST
# Uses BST property to move left or right based on node values
def lowest_common_ancestor(node, node1, node2):
    
    while node:
        if node1.data < node.data and node2.data < node.data:
            node = node.left
        elif node1.data > node.data and node2.data > node.data:
            node = node.right
        else:
            return node.data
        

# Helper function to perform inorder traversal
# Stores elements in sorted order (specific to BST)
def inorder_traversal(node, lst):
    if not node:
        return
    
    inorder_traversal(node.left,lst)
    lst.append(node.data)
    inorder_traversal(node.right,lst)


# Function to find kth smallest element in BST
# Uses inorder traversal to get sorted list, then returns k-th element
def kth_smallest_ele_BST(node,k):
    if not node:
        return
    
    lst = []
    inorder_traversal(node, lst)
    return lst[k-1]

# Function to find maximum path sum in BST
def max_path_sum_BST(node):
    max_sum = -math.inf

    def helper(node):
        nonlocal max_sum

        if not node:
            return 0
        
        left_sum = max(helper(node.left), 0)
        right_sum = max(helper(node.right), 0)

        current_path = node.data + left_sum + right_sum
        max_sum = max(max_sum, current_path)

        return node.data + max(left_sum, right_sum)
    
    helper(node)
    return max_sum

# Function to find sum of all the left leaf nodes in BST
def sum_of_left_leaf_child(node):
    
    if node is None:
        return 0
    
    leaf_node_sum = 0

    if node.left and not node.left.left and not node.left.right:
        leaf_node_sum += node.left.data
    
    leaf_node_sum += sum_of_left_leaf_child(node.left)
    leaf_node_sum += sum_of_left_leaf_child(node.right)

    return leaf_node_sum
    
# Creating BST object and inserting elements
root = BST()

root.insertion(15)
root.insertion(7)
root.insertion(8)
root.insertion(19)
root.insertion(20)
root.insertion(22)
root.insertion(18)
root.insertion(23)

root.inorder_traversal(root.root)
print()
print("Depth Of the tree: ", max_depth_BST(root.root))
print("Number if nodes in the tree: ", no_of_nodes(root.root))
print("Sum of all nodes in the tree: ", sum_of_nodes(root.root))
print("Validate BST: ", validate_BST(root.root))
print("Lowest common ancestors of nodes: ",lowest_common_ancestor(root.root, root.root.left.right, root.root.right))
print("Kth smallest element in the BST: ", kth_smallest_ele_BST(root.root, 4))
print("Max Path sum: ", max_path_sum_BST(root.root))
print("Sum of all left leaf nodes: ",sum_of_left_leaf_child(root.root))