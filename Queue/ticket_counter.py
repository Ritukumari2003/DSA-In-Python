from collections import deque

def last_ticket_code(q, k):
    if k<=0 or k>len(q):
        return None
    
    if len(q) == 1:
        return q[0]
    
    while True:
        # Pop element from left
        for _ in range(k):
            q.popleft()
            if len(q) == 1:
                return q[0]
            
        # Pop element from right 
        for _ in range(k):
            q.pop()
            if len(q) == 1:
                return q[0]

q = deque()
n = int(input('Enter n: '))
# Populating the Queue
for i in range(1,n+1):
    q.append(i)
k = int(input("Enter k: "))
print(last_ticket_code(q, k))   



