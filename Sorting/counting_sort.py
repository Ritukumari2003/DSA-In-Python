# Counting Sort is a non-comparison-based sorting algorithm.
# It works by counting the number of occurrences of each element
# and using this information to place elements in their correct positions.

# It is suitable when the range of input values is limited (not very large) and particularly elements are integer.

# Steps:
# 1. Find the maximum (and minimum, if needed) element in the array
# 2. Create a count array of size (max + 1) to store frequency of each element
# 3. Traverse the input array and count occurrences of each element
# 4. Modify the count array to store cumulative counts (prefix sums)
# 5. Place elements into the output array based on their positions
# 6. Copy the sorted output back to the original array (if required)

# Time Complexity:
# - Best Case: O(N + K)
# - Average Case: O(N + K)
# - Worst Case: O(N + K)
# (where N = number of elements, K = range of input values)

# Space Complexity:
# - O(N + K)

# Stability:
# - Stable (when implemented using cumulative count array)

# Limitations:
# - Works only for integers (or discrete values)
# - Not efficient when the range (K) is very large compared to N

def count_sort(arr):
    max_val = max(arr)
    count_arr = [0]*(max_val + 1)
    
    for ele in arr:
        count_arr[ele] += 1
    
    result = []
    for i in range(len(count_arr)):
        result.extend([i]*count_arr[i])

    return result

arr = [5,1,4,2,6,7]
print('Sorted Array: ',count_sort(arr))
