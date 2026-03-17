# Doubly Linked List
class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    # Checks whether the list is empty or not
    def is_empty(self):
        return self.head is None

    # Displays all elements of the circular linked list
    # Traverses until it comes back to the head
    def display(self):
        if self.is_empty():
            print('Empty List')
            return

        current = self.head

        while current:
            print(current.data, end=' ')
            current = current.next 
        print()

    def insert_at_beginning(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
            node.prev = None
            node.next = None
            self.size += 1
            return self.head
        
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
        return self.head
    
    def insert_at_end(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
            node.prev = None
            node.next = None
            self.size += 1
            return self.head

        current = self.head
        while current.next:
            current = current.next
        current.next = node
        node.prev = current
        self.size += 1
        return self.head
    
    def insert_in_middle(self, val, pos):
        n = self.size
        
        if pos<0 or pos>n:
            raise Exception("Invalid Index Error")

        if pos == 0:
            self.insert_at_beginning(val)
            return
        
        if pos == n:
            self.insert_at_end(val)  
            return
        
        node = Node(val)
        current = self.head
        count = 0
        while count != pos-1:
            current = current.next
        node.next = current.next
        node.next.prev = node
        current.next = node
        node.prev = current
        self.size += 1
        return self.head        

dll = DoublyLinkedList()
# dll.insert_at_beginning(4)
# dll.insert_at_beginning(14)
# dll.insert_at_beginning(42)
# dll.insert_at_beginning(43)
# dll.display()

# dll.insert_at_end(12)
# dll.insert_at_end(22)
# dll.insert_at_end(32)
dll.insert_at_end(42)
dll.display()

dll.insert_in_middle(42,1)
dll.display()
dll.insert_in_middle(2,0)
dll.display()
dll.insert_in_middle(21,1)
dll.display()
dll.insert_in_middle(12,1)
dll.display()
