# Frequency of characters

############# using get() method ##############

data = input("Enter a string: ")
# counts = dict()
# for ch in data:
#     if ch.isalpha():
#         counts[ch] = counts.get(ch,0)+1    
# #     The get keyword is creating a key with ch character and value 0 if does not exist in the dictionary

# print(counts)
    
############# using counter module ##############
from collections import Counter
print(Counter(data))