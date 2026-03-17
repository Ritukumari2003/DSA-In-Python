# Circular Singly Linked List 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def display(self):
        if self.is_empty():
            print('Empty List')
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
            node.next = self.head
            self.size += 1
            return self.head
        
        current = self.head
        while current.next != self.head:
            current = current.next 

        node.next = self.head
        current.next = node
        self.head = node
        self.size += 1
        return self.head
    
    def insert_at_end(self, val):
        node = Node(val)

        if self.is_empty():
            self.head = node
            node.next = self.head
            self.size += 1
            return self.head 
        
        current = self.head

        while current.next != self.head:
            current = current.next
        
        current.next = node
        node.next = self.head
        self.size += 1
        return self.head
    
    def insert_in_middle(self, val, pos):
        node = Node(val)

        if pos<0 or pos > self.size:
            raise Exception("Invalid Index")
        elif self.is_empty():
            self.head = node
            node.next = self.head
        elif pos == 0:
            self.insert_at_beginning(val)
        elif pos == self.size:
            self.insert_at_end(val)
        else:
            current = self.head
            index = 0
            while index != pos-1:
                current = current.next
                index += 1
            node.next = current.next
            current.next = node
        self.size += 1
        return self.head
    
cll = CircularSinglyLinkedList()
cll.display()

############## Insertion at beginning ###############
cll.insert_at_beginning(5)
cll.insert_at_beginning(51)
cll.insert_at_beginning(15)
cll.insert_at_beginning(25)
cll.insert_at_beginning(35)

################ Insertion at End ####################
cll.insert_at_end(5)
cll.insert_at_end(51)
cll.insert_at_end(15)
cll.insert_at_end(25)
cll.insert_at_end(35)

################ Insertion in middle ####################
cll.insert_in_middle(1,2)
cll.insert_in_middle(2,3)
cll.insert_in_middle(3,4)
cll.insert_in_middle(4,5)
cll.insert_in_middle(5,6)

cll.display()
            
