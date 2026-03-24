from collections import *

def isBalanced(S : str) -> bool:
    # Write your code here.
    stack = deque()
    i = 0
    while i in range(len(S)):
        if S[i] in '({[':
            stack.append(S[i])
        else:
            if not stack:
                return False
            popped = stack.pop()
            if ((S[i] == ')' and popped != '(') or 
               (S[i] == ']' and popped != '[') or
               (S[i] == '}' and popped != '{')):
                return False
        i += 1
    
    return len(stack) == 0

print(isBalanced('(([[{}]]))'))
print(isBalanced('(([[{}]])])'))