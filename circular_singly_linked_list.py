# Circular Singly Linked List 

# Node class represents each element in the list
# It contains the data and a pointer to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Main class for Circular Singly Linked List
class CircularSinglyLinkedList:
    
    # Initializes an empty list with head = None and size = 0
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

        while True:
            print(current.data, end=' ')
            current = current.next 
            if current == self.head:
                break 
        print()

    # Inserts a node at the beginning of the list
    # Updates head and maintains circular connection
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
    
    # Inserts a node at the end of the list
    # Traverses to last node and connects it to new node
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
    
    # Inserts a node at a given position (index-based)
    # Handles insertion at beginning, end, and middle
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
    
    # Searches for a value in the list
    # Returns index if found, else returns -1
    def search(self, val):
        current = self.head
        index = 0
        if self.is_empty():
            raise Exception("List is empty")
        while True:
            if current.data == val:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return -1
    
    # Deletes a node with given value
    # Handles deletion for:
    # 1. Single node
    # 2. Head node
    # 3. Middle/last node
    def delete_node(self, val):
        if self.is_empty():
            raise Exception("List is empty")
        
        current = self.head

        # single node case
        if self.head.next == self.head:
            if current.data == val:
                self.head = None
                self.size -= 1
                return
            else:
                raise Exception("Key not found!!!..")
            
        # deletion at beginning 
        if current.data == val:            
            pointer = self.head
            while pointer.next != self.head:
                pointer = pointer.next
            self.head = self.head.next
            pointer.next = self.head
            current.next = None
            self.size -= 1
            return self.head
        
        prev = None
        while True:
            if current.data == val:
                prev.next = current.next
                current.next = None
                self.size -= 1
                return self.head
            prev = current
            current = current.next
            if current == self.head:
                break
        raise Exception("Key not found!!!..")
    
if __name__ == '__main__':
    cll = CircularSinglyLinkedList()

    while True:
        print("\n===== Circular Linked List Menu =====")
        print("1. Display List")
        print("2. Insert at Beginning")
        print("3. Insert at End")
        print("4. Insert at Position")
        print("5. Search Element")
        print("6. Delete Element")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            cll.display()

        elif choice == 2:
            val = int(input("Enter value: "))
            cll.insert_at_beginning(val)

        elif choice == 3:
            val = int(input("Enter value: "))
            cll.insert_at_end(val)

        elif choice == 4:
            val = int(input("Enter value: "))
            pos = int(input("Enter position: "))
            try:
                cll.insert_in_middle(val, pos)
            except Exception as e:
                print(e)

        elif choice == 5:
            val = int(input("Enter value to search: "))
            try:
                result = cll.search(val)
                if result == -1:
                    print("Element not found")
                else:
                    print("Element found at index:", result)
            except Exception as e:
                print(e)

        elif choice == 6:
            val = int(input("Enter value to delete: "))
            try:
                cll.delete_node(val)
                print("Deleted successfully")
            except Exception as e:
                print(e)

        elif choice == 7:
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again!")