
################# Find first and last occurence in Sorted Array #################
# Given a sorted array arr and a target, find the first and last index of the target 

def first_last_idx(arr, target):
    low = 0
    high = len(arr) - 1
    start_ind = -1
    
    while low <= high:
        mid = low+(high-low)//2

        if arr[mid] == target:
            start_ind = mid
            high = mid-1
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1

    end_ind = -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low+(high-low)//2

        if arr[mid] == target:
            end_ind = mid
            low = mid+1
        elif arr[mid] > target:
            high = mid-1
        else:
            low = mid+1
    
    return (start_ind, end_ind)

arr = [1,1,2,2,2,4,4,4,4,4,5,6]
target = 4
print("Start and End Index of the array: ",first_last_idx(arr, target))

# ------------------------------------------------------------------------------

################# Minimum Days to make bouquets #################
# bloomDay[i] = day i-th flower blooms 
# Need to make m bouquets 
# Each bouquets needs k adjacent flowers
# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.


def is_possible_day(day, bloomDay, m, k):

    no_of_flower = 0
    no_of_bouquet = 0
        
    for j in bloomDay:
        if j <= day:
            no_of_flower += 1
            if no_of_flower == k:
                no_of_bouquet += 1
                no_of_flower = 0
        else:
            no_of_flower = 0   
        
    if no_of_bouquet >= m:
        return True
    
    return False


################# Using Linear Search - Brute Force approach #############
# def minDays(bloomDay, m, k):
#     if m * k > len(bloomDay):
#         return -1
        
#     min_day = min(bloomDay)
#     max_day = max(bloomDay)
    
#     for day in range(min_day, max_day + 1):
#         if is_possible_day(day, bloomDay, m, k):
#             return day
            
#     return -1

################## Using Binary Search ################3
def minDays(bloomDay, m, k):
    if m * k > len(bloomDay):
        return -1
        
    low = min(bloomDay)
    high = max(bloomDay)

    while low<=high:
        mid = low+(high-low)//2

        if is_possible_day(mid, bloomDay, m, k):
            high = mid-1
        else:
            low = mid+1
    return low

print("Min no of days required to make m bouquets: ", minDays([1,10,3,10,2], 3, 1))

# ---------------------------------------------------------------------------------------------

################# Aggressive Cows #################
# You are given an array with unique elements of stalls[], which denote the positions of stalls. You are also given an integer k which denotes the number of aggressive cows. The task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

def can_we_place(dis, stalls, cows):
    count = 1
    last_placed_cow_stall = 0

    for stall_no in range(1, len(stalls)):
        if stalls[stall_no]-stalls[last_placed_cow_stall] >= dis:
            last_placed_cow_stall = stall_no
            count += 1
        if count>=cows:
            return True
    return False

# Using Linear Search  - Brute Force
# def aggressive_cows(stalls, cows):
#     n = len(stalls)
#     stalls = sorted(stalls)
#     max = stalls[n-1]
#     min = stalls[0]

#     for dis in range(1, max-min+1):
#         if(can_we_place(dis,stalls,cows) == True):
#             continue
#         else:
#             return dis-1
        
# Using Binary Search
def aggressive_cows(stalls, cows):
    stalls.sort()
    n = len(stalls)
    low = min(stalls)
    high = max(stalls)

    while low <= high:
        mid = low+(high-low)//2

        if can_we_place(mid, stalls, cows):
            low = mid+1
        else:
            high = mid-1
    return high


print("Max of the min distance between the cows: ", aggressive_cows([0,3,4,7,9,10],4))



