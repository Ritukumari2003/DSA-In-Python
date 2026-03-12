# Anagrams

########### Using sorted ##########
s1 = "listen"
s2 = "silent"

anagram = True

for a, b in zip(sorted(s1), sorted(s2)):
    if a != b:
        anagram = False
        break
        
if anagram:
    print('Anagram')
else:
    print('Not an anagram')

# more simpler:
print(sorted(s1) == sorted(s2))

######## Using dictionary #############