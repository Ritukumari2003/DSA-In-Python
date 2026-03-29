
from collections import Counter

################# Print top k frequent element #################
def top_freq_ele(arr,k):
    freq = Counter(arr)

    return sorted(freq, key = lambda x: freq[x], reverse=True)[:k]

arr = [3,1,2,2,3,3,1,3,2]
print(top_freq_ele(arr,2))

################# Valid Anagram #################
def check_anagrams(s1,s2):
    if len(s1) != len(s2):
        return False
    
    return Counter(s1) == Counter(s2)

s1 = 'listen'
s2 = 'silent'
print("Valid Anagrams", (s1,s2), check_anagrams(s1,s2))

################# Isomorphic Strings #################
def is_isomorphic(s1,s2):
    if len(s1) != len(s2):
        return False
    
    map1 = dict()
    map2 = dict()

    for c1, c2 in zip(s1, s2):
        if c1 in map1 and map1[c1] != c2:
            return False
        if c2 in map2 and map2[c2] != c1:
            return False
        map1[c1] = c2
        map2[c2] = c1
    return True

print("Is Isomorphic: ", (s1,s2), is_isomorphic(s1,s2))
