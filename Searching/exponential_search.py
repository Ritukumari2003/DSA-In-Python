# Exponential Search is an efficient searching algorithm used for sorted arrays.
# It is especially useful for very large or unbounded arrays.
# The algorithm works in two main stages:

# 1. Finding the range:
#    - Start from index 1 and keep doubling the index (1, 2, 4, 8, ...)
#    - Continue until the element at that index is greater than or equal to the target
#    - This helps identify a range [low, high] where the target may exist

# 2. Applying Binary Search:
#    - Once the range is found, perform Binary Search within that range only

# Important points:
# - The array must be sorted
# - Reduces search space quickly by exponential jumps

# Time Complexity:
# - O(log i) for range finding (where i is position of target)
# - O(log i) for binary search
# - Overall: O(log i)

def binary_search(l, low, high, key):

    while low<=high:
        mid = low+(high-low)//2

        if l[mid] == key:
            return mid
        
        if l[mid] < key:
            low = mid+1
        
        if l[mid] > key:
            high = mid-1
    
    return -1

def exponential_search(l, key):
    n = len(l)

    if l[0] == key:
        return 0
    
    i = 1
    while i<n and l[i] <= key:
        i *= 2

    low = i//2
    high = min(n-1, i)
    print("Applied Binary search in the range", (low, high))
    search = binary_search(l, low, high, key)
    return search
    
# index = exponential_search([1,2,3,4,5,6], 8)
index = exponential_search([1,2,3,4,5,6], 4)
print("Element is present at index", index) if index != -1 else print("Element not found")
