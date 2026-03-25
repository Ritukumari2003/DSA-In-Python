# Linear Search also called as sequential search

# Searching elements one by one
# will traverse the whole list
# if match found, it will return true or the index where element is present and terminate the search
# if no match found, it will return false or -1

def linear_search(l, key):
    if len(l) == 0:
        return -1
    
    for i in range(0, len(l)):
        if l[i] == key:
            return i
    
    return -1

# index = linear_search([4,5,1,2,6,9], 8)
index = linear_search([4,5,1,2,6,9], 2)
print("Element is present at index", index) if index != -1 else print("Element not found")




