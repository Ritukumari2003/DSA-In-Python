
################ Subarray Sum equals to k ################

def subarray_sum_eql_k(arr, target):
    ########### Brute force Approach ############
    # count = 0
    # for i in range(0,len(arr)):
    #     sum = 0
    #     for j in range(i,len(arr)):
    #         sum += arr[j]
    #         if sum == target:
    #                 count+=1
    # return count
    
    ########### Optimal Approach ###########
    i = 0
    count = 0
    prefix_sum = 0
    freq_dict = {0: 1} 
    while i<len(arr):
        prefix_sum += arr[i]
        diff = prefix_sum - target
        if diff in freq_dict:
            count += freq_dict[diff]
        freq_dict[prefix_sum] = freq_dict.get(prefix_sum, 0) + 1
        i += 1
    return count

################ Longest Subarray with equal 0s and 1s ################

def longest_subarray(arr):
    i = 0
    longest = 0
    prefix_sum = 0
    first_sum_zero_dict = {0: -1} 
    
    while i < len(arr):
        prefix_sum += 1 if arr[i] == 1 else -1
        
        if prefix_sum in first_sum_zero_dict:
            longest = max(longest, i - first_sum_zero_dict[prefix_sum])
        else:
            first_sum_zero_dict[prefix_sum] = i
        
        i += 1
        
    return longest

################ Count Subarrays Divisible by K ################
def count_sub_arrays(arr, k):
    count = 0
    prefix_sum = 0
    freq = {0: 1}

    for num in arr:
        prefix_sum += num
        mod = prefix_sum % k

        if mod in freq:
            count += freq[mod]
        
        freq[mod] = freq.get(mod, 0) + 1
    
    return count 

print(subarray_sum_eql_k([1,2,3,-3,1,1,1,4,2,-3],3))
print(longest_subarray([1,1,0,1,0,1,0,0,0,0,1]))
print(count_sub_arrays([1,2,3,-3,1,1,1,4,2,-3], 3))
