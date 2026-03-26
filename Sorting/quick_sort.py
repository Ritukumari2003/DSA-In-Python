# Quick Sort is an efficient, comparison-based sorting algorithm
# that follows the Divide and Conquer principle.

# It works by selecting a "pivot" element and partitioning the array
# such that:
# - Elements smaller than the pivot are placed on the left
# - Elements greater than the pivot are placed on the right

# Steps:
# 1. Choose a pivot element (commonly first, last, or middle element)
# 2. Rearrange (partition) the array so that:
#    - All elements less than pivot come before it
#    - All elements greater than pivot come after it
# 3. Recursively apply Quick Sort on the left subarray
# 4. Recursively apply Quick Sort on the right subarray

# After partitioning, the pivot is placed at its correct sorted position

# Time Complexity:
# - Best Case: O(N log N)
# - Average Case: O(N log N)
# - Worst Case: O(N^2) (when pivot selection is poor, e.g., already sorted array)

# Space Complexity:
# - O(log N) (due to recursion stack)

# Stability:
# - Not Stable (may change the relative order of equal elements)

def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    pivot = arr[n//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [5,1,4,2,6,7]
print('Sorted Array: ',quick_sort(arr))
