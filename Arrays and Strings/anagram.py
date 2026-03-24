# Anagrams

########### Using sorted ########## O(nlogn) ##########
s1 = "listen"
s2 = "silent"

anagram = True

for a, b in zip(sorted(s1), sorted(s2)):
    if a != b:
        anagram = False
        break
        
print("O(nlogn): ")
if anagram:
    print('Anagrams')
else:
    print('Not anagrams')

# more simpler:
# print(sorted(s1) == sorted(s2))

######## Using dictionary mapping ############# O(n) ##########
mapping = [0]*26

for ch in s1:
    index = ord(ch)-97
    mapping[index] += 1

for ch in s2:
    index = ord(ch)-97
    mapping[index] -= 1

print()
print("O(n): ")
if all(list(m==0 for m in mapping)):
    print("Anagrams")
else:
    print("Not Anagrams")
    
