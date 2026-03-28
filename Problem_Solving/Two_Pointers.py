
################ Remove Duplicates from sorted array ##############
# Given a sorted array, remove duplicates in place and return length of the new array

# Approach 1
# def remove_dup(lst):
#     left = 0
#     right = 0
#     if len(lst) == 0:
#         return 0
#     count = 1
#     while right<len(lst):
#         if lst[left] != lst[right]:
#             count += 1
#             left = right
#         right += 1
#     return count

# Approach 2
def remove_dup(lst):
    left = 0

    for right in range(1,len(lst)):
        if lst[right] != lst[left]:
            left += 1
            lst[left] = lst[right]

    return (left+1, lst[:left+1])

################ Find all unique Triplets ##############
# Given array arr, return all unique triplets (a,b,c) such that a+b+c = 0

def find_unique_triplets(nums):
    res = []
    nums = sorted(nums)

    for i in range(len(nums)-2):
        if (i>0) and (nums[i] == nums[i-1]):
            continue
        left, right = i+1, len(nums)-1
        while left<right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                res.append((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
                while left<right and nums[left] == nums[left-1]:
                    left += 1
            elif sum<=0:
                left += 1
            else:
                right -= 1
    return res

################ Find pairs of target sum ##############
# Given array arr, return all pairs with sum = target

def two_sum(nums,target):
    res = []
    nums = sorted(nums)
    left = 0
    right = len(nums) - 1

    while left<right:
        sum = nums[left] + nums[right]
        if sum == target:
            res.append((nums[left], nums[right]))
            left += 1
            right -= 1
            if left>0 and nums[left] == nums[left-1]:
                left += 1
            if right>0 and nums[right] == nums[right+1]:
                right -= 1
        elif sum < target:
            left += 1
        else:
            right -= 1
    return res


print("Remove duplicates: ",remove_dup([1,1,2,2,2,3,4,4,5]))
print("Remove duplicates: ",remove_dup([1]))

print('Find triplets with sum 0: ', find_unique_triplets([-1,1,0,2,-1,-4]))

print("Find taget sum pairs: ",two_sum([-1,1,0,2,-1,-4],6))