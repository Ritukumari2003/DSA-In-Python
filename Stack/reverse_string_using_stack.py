from collections import *

def reverseString(string):
    # Write your code here.
    # return string[::-1]

    # using stack
    stack = deque()
    res = ''
    for i in string:
        stack.append(i)
    while stack:
        res += stack.pop()
    return res

string = input('Enter a string: ')
print('Reversed String: ', reverseString(string))