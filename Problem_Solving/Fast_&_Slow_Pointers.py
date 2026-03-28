
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class Solution:

    ################ Detect Cycle ################
    def has_cycle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    ################ Find Cycle Start ################
    def cycle_start(self, head):
        slow, fast = head, head

        # Step 1: detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None   # no cycle

        # Step 2: find start
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
    
################ Find duplicate numbers (Floyd Cycle Detection on Arrays) ################
# We will assume index in arrays as nodes in linked list and values as next pointers
def find_duplicates(arr):
    slow = arr[0]
    fast = arr[arr[0]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    slow = 0
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow 


# Creating Linked List
head = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(20)
n5 = Node(25)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n2   # cycle here

sol = Solution()
print(sol.has_cycle(head))         
start = sol.cycle_start(head)
print(start.data if start else None)  

# Cycle in array
print("Duplicate in Array: ",find_duplicates([2, 1, 4, 5, 3, 4]))