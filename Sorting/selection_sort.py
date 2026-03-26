# Selection Sort is a simple comparison-based sorting algorithm.
# It repeatedly selects the smallest (or largest) element from the unsorted portion
# of the array and places it at its correct position.

# The array is divided into two parts:
# 1. Sorted portion (left side)
# 2. Unsorted portion (right side)

# Steps:
# 1. Assume the first element is the minimum
# 2. Compare it with the remaining elements to find the actual minimum
# 3. Swap the minimum element with the first element
# 4. Move the boundary of the sorted portion one step to the right
# 5. Repeat the process for the remaining unsorted elements

# After each pass, one element is placed at its correct sorted position

# Time Complexity:
# - Best Case: O(N^2)
# - Average Case: O(N^2)
# - Worst Case: O(N^2)

# Space Complexity:
# - O(1) (in-place sorting algorithm)

# Stability:
# - Not Stable (may change the relative order of equal elements)

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_ind = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]

    return arr

arr = [5,1,4,2,6,7]
print('Sorted Array: ',selection_sort(arr))
