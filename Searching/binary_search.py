# Binary Search is an efficient searching algorithm used to find an element in a sorted list.
# It works on the Divide and Conquer principle by repeatedly dividing the search space into two halves.
# For Binary Search to work correctly, the input list must be sorted.
# Two pointers are used:
# low  → starting index of the search space
# high → ending index of the search space
# The middle index is calculated using:
# mid = low + (high - low) // 2
# The target element is compared with the middle element:
# - If equal → element found
# - If smaller → search in the left half
# - If greater → search in the right half
# This process continues until the element is found or the search space becomes empty.
# Time Complexity: O(log N)


def binary_search(l, key):

    if len(l) == 0:
        return -1
    
    low = 0
    high = len(l)-1

    l = sorted(l)

    while low<=high:
        mid = low+(high-low)//2

        if l[mid] == key:
            return True
        
        if l[mid] < key:
            low = mid+1
        
        if l[mid] > key:
            high = mid-1
    
    return False

# found = binary_search([4,5,1,2,6,9], 8)
found = binary_search([4,5,1,2,6,9], 2)
print("Element is present in the list") if found == True else print("Element not found")





