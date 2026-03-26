# Merge Sort is an efficient, comparison-based sorting algorithm
# that follows the Divide and Conquer principle.

# It divides the array into smaller subarrays, sorts them recursively,
# and then merges the sorted subarrays to produce the final sorted array.

# Steps:
# 1. Divide the array into two halves
# 2. Recursively apply Merge Sort on both halves
# 3. Merge the two sorted halves into a single sorted array

# The merging step involves comparing elements from both halves
# and placing them in the correct order in a temporary array.

# This process continues until the entire array is sorted

# Time Complexity:
# - Best Case: O(N log N)
# - Average Case: O(N log N)
# - Worst Case: O(N log N)

# Space Complexity:
# - O(N) (requires extra space for merging)

# Stability:
# - Stable (maintains the relative order of equal elements)

def merge(left, right):
    result = []
    i = j = 0

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr
    mid = n//2
    left = merge_sort(arr[ : mid])
    right = merge_sort(arr[mid : ])
    return merge(left, right)

arr = [5,1,4,2,6,7]
print('Sorted Array: ',merge_sort(arr))
