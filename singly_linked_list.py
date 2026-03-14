# Singly Linked List 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
    
    def display(self):
        if not self.head:
            print('Empty List')
        else:
            current = self.head
            while current:
                print(current.data, end=' ')
                current = current.next
            print()

    def insert_at_beginning(self, val):
        node = Node(val)
        if self.head:
            node.next = self.head
        self.head = node
        return self.head
    
    def insert_at_end(self, val):
        node = Node(val)
        
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
        return self.head   

    def insert_in_middle(self, val, pos):
        n = self.get_length()
        
        if pos<0 or pos>n:
            raise IndexError("Invalid Index")

        if pos == 0:
            self.insert_at_beginning(val)
            return
        
        if pos == n:
            self.insert_at_end(val)  
            return
        
        node = Node(val)
        count = 0
        current = self.head
        while count!=pos-1:
            current = current.next
            count += 1

        node.next = current.next
        current.next = node
        return self.head 
    
sll = SinglyLinkedList()

################## Insertion at beginning ###############

# print('Before Insertion at beginning: ')
# print(sll.get_length())
# sll.display()

# sll.insert_at_beginning(5)
# sll.insert_at_beginning(20)
# sll.insert_at_beginning(7)
# sll.insert_at_beginning(15)

# print("After Insertion at beginning: ")
# print(sll.get_length())
# sll.display()

# print()

################ Insertion at end ###################
# print("Before Insertion at end: ")
# sll.display()

# sll.insert_at_end(9)
# sll.insert_at_end(19)
# sll.insert_at_end(29)

# print("After Insertion at end: ")
# sll.display()

############## Insertion in the middle of the list #############
print("Before Insertion in middle: ")
sll.display()

sll.insert_in_middle(9,0)
sll.insert_in_middle(19,1)
sll.insert_in_middle(29,2)
sll.insert_in_middle(49,1)
sll.insert_in_middle(91,3)

print("After Insertion in middle: ")
sll.display()

