# Circular Doubly Linked List 

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def display(self):
        if self.is_empty():
            print("Empty List")
            return
        
        current = self.head

        while True:
            print(current.data, end=' ')
            current = current.next
            if current == self.head:
                break
        print()

    def insert_at_beginning(self, val):
        node = Node(val)

        if self.is_empty():
            self.head = node
            node.next = node
            node.prev = node
            self.size += 1
            return self.head
        
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = node
        node.prev = current
        node.next = self.head
        self.head.prev = node
        
        self.head = node

        self.size += 1
        return self.head    

    def insert_at_end(self, val):
        node = Node(val)

        if self.is_empty():
            self.head = node
            node.next = node
            node.prev = node
            self.size += 1
            return self.head
        
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = node
        node.prev = current
        node.next = self.head
        self.head.prev = node

        self.size += 1
        return self.head
    
    def insert_in_middle(self, val, pos):
        node = Node(val)

        if self.is_empty():
            if pos != 0:
                raise Exception("Invalid Index")
            self.head = node
            node.next = node
            node.prev = node
            self.size += 1
            return self.head
        
        if pos<0 or pos>self.size:
            raise Exception("Invalid Index")
        elif pos == 0:
            return self.insert_at_beginning(val)
        elif pos == self.size:
            return self.insert_at_end(val)
        else:        
            current = self.head
            index = 0
            while index != pos-1:
                current = current.next
                index += 1
            node.next = current.next
            node.next.prev = node
            current.next = node
            node.prev = current
            self.size += 1
        return self.head
    
cdll = CircularDoublyLinkedList()
cdll.display()

cdll.insert_at_end(5)
cdll.insert_at_end(51)
cdll.insert_at_end(52)
cdll.insert_at_end(53)
cdll.insert_at_end(54)

cdll.display()

cdll.insert_at_beginning(10)
cdll.insert_at_beginning(20)

cdll.display()

cdll.insert_in_middle(56,0)
cdll.insert_in_middle(56,1)
cdll.insert_in_middle(56,9)
# cdll.insert_in_middle(56,10) # Invalid Index

cdll.display()

        