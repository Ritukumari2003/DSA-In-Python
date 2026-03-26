# Bubble Sort is a simple comparison-based sorting algorithm.
# It repeatedly steps through the list, compares adjacent elements,
# and swaps them if they are in the wrong order.

# In each pass, the largest (or smallest) element "bubbles up"
# to its correct position at the end of the list.

# Steps:
# 1. Start from the first element and compare it with the next element
# 2. If the current element is greater than the next, swap them
# 3. Move to the next pair and repeat until the end of the list
# 4. After each pass, the last element is in its correct sorted position
# 5. Repeat the process for the remaining unsorted portion

# Optimization:
# - If no swaps occur in a pass, the array is already sorted,
#   and the algorithm can terminate early

# Time Complexity:
# - Best Case: O(N) (when array is already sorted with optimization)
# - Average Case: O(N^2)
# - Worst Case: O(N^2)

# Space Complexity:
# - O(1) (in-place sorting algorithm)

# Stability:
# - Stable (does not change the relative order of equal elements)

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        swapped = False
        for j in range(0, n-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [5,1,4,2,6,7]
print('Sorted Array: ',bubble_sort(arr))
