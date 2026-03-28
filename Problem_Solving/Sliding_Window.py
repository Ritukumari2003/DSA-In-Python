
################ Maximum Sum Subarray ##############

# ==================================
# Brute Force approach
# Time Complexity = O(n × k)
# ==================================

# def max_sum_subarray(lst, window_size):
#     left = 0
#     right = 0
#     max_sum = float('-inf')

#     while left<len(lst):
#         current_sum = 0
#         right = left
#         while right<len(lst) and right-left+1 <= window_size:
#             current_sum += lst[right]
#             right += 1

#         if (right - left) == window_size:
#             print('Current Sum:', current_sum)
#             max_sum = max(max_sum, current_sum)

#         left += 1
        
#     return max_sum

# ==================================
# Optimized Approach
# Time Complexity = O(n)
# ==================================

def max_sum_subarray(lst, window_size):
    left = 0
    right = 0
    w_sum = 0
    max_sum  = float('-inf')

    if window_size > len(lst):
        return None

    while right<len(lst):
        w_sum += lst[right]
        if right-left+1 == window_size:
            print('Window Sum:', w_sum)
            max_sum = max(max_sum, w_sum)
            w_sum -= lst[left]
            left += 1
        right += 1

    return max_sum

################ Longest Substring without repeating Characters ##############

def substring_len(s):
    char_set = set()
    max_len = 0
    left = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[right])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right-left+1)
    return max_len


################ Find all anagrams in a string ##############

# Given strings s and p, find all starting indices in s where the substring is an anagram of p

from collections import Counter

def anagram_indices(s, p):
    p_counts = Counter(p)
    w_counts = Counter()
    res = []
    left = 0

    for right in range(len(s)):
        w_counts[s[right]] += 1
        if right-left+1 == len(p):
            if w_counts == p_counts:
                res.append(left)
            w_counts[s[left]] -= 1
            if w_counts[s[left]] == 0:
                del w_counts[s[left]]
            left += 1

    return res

print('Maximum sum:',max_sum_subarray([-2, -3, 4, -1, -2, 1, 5], 3))
        
print('Length of longest substring without repeating characters:',substring_len('abcccabcdefacbdabcde'))    

print('Anagram Indices:',anagram_indices('abcccabcdefacbdabcde', 'abc'))