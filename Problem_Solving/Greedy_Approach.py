
################# Activity Scheduling ################
# Select maximum number of overlapping activities
def activity_selection(intervals):
    intervals.sort(key = lambda val: val[1])

    count = 0
    last_end = -float('inf')

    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    
    return count

print("No. of activities that can be completed without overlapping:",activity_selection([[1,2],[2,3],[3,4],[1,3]]))

# ---------------------------------------------------------------------------------

################## Minimum platforms (Railway Station Problem) #################
# Given arrival and departure times of trains, find the minimum platforms needed so no train waits

def calculateMinPatforms(at, dt):
    # Write your code here.
    at.sort()
    dt.sort()

    i = j = 0
    curr_platforms = 0
    res = 0

    while i<len(at):
        if at[i] < dt[j]:
            curr_platforms += 1
            res = max(res, curr_platforms)
            i += 1
        else:
            curr_platforms -= 1
            j += 1
    
    return res


at = [900,940,950,1100]
dt = [910,1200,1120,1130]
print("Minimum Plaforms:", calculateMinPatforms(at, dt))

# ------------------------------------------------------------------------------

################## Jump Game #################
# Given an array arr, each element represents max jump length
# Return wether you can reach last index 

def can_jump(nums):
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
    return True

print("Is possible to reach last index:", can_jump([2,3,1,1,4]))
