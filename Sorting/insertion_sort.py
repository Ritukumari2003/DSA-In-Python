# Insertion Sort is a simple comparison-based sorting algorithm.
# It builds the sorted array one element at a time by inserting each element
# into its correct position in the already sorted portion of the array.

# The array is divided into two parts:
# 1. Sorted portion (left side)
# 2. Unsorted portion (right side)

# Steps:
# 1. Assume the first element is already sorted
# 2. Pick the next element from the unsorted portion
# 3. Compare it with elements in the sorted portion (from right to left)
# 4. Shift all elements greater than the current element one position to the right
# 5. Insert the current element at its correct position
# 6. Repeat the process for all remaining elements

# After each pass, the sorted portion increases by one element

# Time Complexity:
# - Best Case: O(N) (when array is already sorted)
# - Average Case: O(N^2)
# - Worst Case: O(N^2)

# Space Complexity:
# - O(1) (in-place sorting algorithm)

# Stability:
# - Stable (maintains the relative order of equal elements)

def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        ele = arr[i]
        j = i-1
        while j>=0 and arr[j]>ele:
            arr[j+1] = arr[j]
            j -= 1           
        arr[j+1] = ele 
    return arr

arr = [5,1,4,2,6,7]
print('Sorted Array: ',insertion_sort(arr))
