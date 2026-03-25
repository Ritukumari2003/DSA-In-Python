from collections import deque

def reverseElements(q, k):
    
    if k<=0 or k>len(q):
        return q
    count = len(q) - k
    stack = deque()
    while k!=0:
        stack.append(q.popleft())
        k -= 1
    while stack:
        q.append(stack.pop())
    while count!=0:
        q.append(q.popleft())
        count -= 1

    return q

q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

print("Reverse: ", list(reverseElements(q, 5)))