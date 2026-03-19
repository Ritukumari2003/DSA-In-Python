# Circular Doubly Linked List 

class Node:
    # Creates a node with given data and initializes
    # previous and next pointers to None
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class CircularDoublyLinkedList:
    # Initializes an empty circular doubly linked list
    # head points to first node, size tracks number of nodes
    def __init__(self):
        self.head = None
        self.size = 0

    # Checks whether the list is empty
    # Returns True if head is None, else False
    def is_empty(self):
        return self.head is None

    # Traverses and prints all elements in the list
    # Stops when it reaches the head again (circular condition)
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

    # Inserts a new node at the beginning of the list
    # Updates head and maintains circular links
    def insert_at_beginning(self, val):
        node = Node(val)

        # If list is empty, new node points to itself
        if self.is_empty():
            self.head = node
            node.next = node
            node.prev = node
            self.size += 1
            return self.head
        
        # Traverse to last node
        current = self.head
        while current.next != self.head:
            current = current.next

        # Adjust pointers to insert before head
        current.next = node
        node.prev = current
        node.next = self.head
        self.head.prev = node
        
        # Update head to new node
        self.head = node

        self.size += 1
        return self.head    

    # Inserts a new node at the end of the list
    # Maintains circular structure by linking last node to head
    def insert_at_end(self, val):
        node = Node(val)

        # If list is empty, initialize circular node
        if self.is_empty():
            self.head = node
            node.next = node
            node.prev = node
            self.size += 1
            return self.head
        
        # Traverse to last node
        current = self.head
        while current.next != self.head:
            current = current.next

        # Insert node after last node
        current.next = node
        node.prev = current
        node.next = self.head
        self.head.prev = node

        self.size += 1
        return self.head
    
    # Inserts a node at a specific position (0-based index)
    # Handles insertion at beginning, end, and middle
    def insert_in_middle(self, val, pos):
        node = Node(val)

        # If list is empty, only position 0 is valid
        if self.is_empty():
            if pos != 0:
                raise Exception("Invalid Index")
            self.head = node
            node.next = node
            node.prev = node
            self.size += 1
            return self.head
        
        # Validate position
        if pos<0 or pos>self.size:
            raise Exception("Invalid Index")

        # Insert at beginning
        elif pos == 0:
            return self.insert_at_beginning(val)

        # Insert at end
        elif pos == self.size:
            return self.insert_at_end(val)

        # Insert in between nodes
        else:        
            current = self.head
            index = 0

            # Traverse to (pos-1)th node
            while index != pos-1:
                current = current.next
                index += 1

            # Adjust pointers to insert node
            node.next = current.next
            node.next.prev = node
            current.next = node
            node.prev = current

            self.size += 1

        return self.head
    
    # Searches for a given value in the list
    # Returns index if found, else returns -1
    def search(self, val):
        if self.is_empty():
            raise Exception("Empty List")
        
        current = self.head
        index = 0

        # Traverse entire circular list
        while True:
            if current.data == val:
                return index
            index += 1
            current = current.next
            if current == self.head:
                break            

        return -1
    
    # Deletes a node with the given value
    # Handles deletion at beginning, middle, and single node case
    def delete_node(self, val):
        # Case 1: Empty list
        if self.is_empty():
            raise Exception("Empty List")
        
        # Case 2: Only one node
        if self.head.next == self.head:
            if self.head.data == val:
                self.head = None
                self.size -= 1
                return self.head
            else:
                raise Exception("Key Not Found!!..")
            
        current = self.head

        # Case 3: Deleting head node
        if current.data == val:
            temp = self.head   

            # Find last node
            while temp.next != current:
                temp = temp.next
            
            # Update head and fix links
            self.head = current.next
            temp.next = self.head
            self.head.prev = temp

            # Remove current node
            current.next = None
            current.prev = None

            self.size -= 1
            return self.head  
        
        current = self.head.next

        # Case 4: Deleting node in middle or end
        while current != self.head:
            if current.data == val:
                current.prev.next = current.next
                current.next.prev = current.prev

                # Disconnect node
                current.prev = None
                current.next = None

                self.size -= 1
                return self.head
            current = current.next

        # Value not found
        raise Exception("Key Not Found!!..")
    
    # Reverses the circular doubly linked list
    # Swaps next and prev pointers for each node
    # Updates head to maintain correct starting point
    def reverse(self):
        if self.is_empty():
            raise Exception("Empty List")
        
        # If only one node, no change needed
        if self.head.next == self.head:
            return self.head
        
        current = self.head

        # Traverse and swap next and prev for each node
        while True:
            temp = current.next
            current.next = current.prev
            current.prev = temp

            current = current.next
            if current == self.head:
                break

        # Update head to new starting node
        self.head = self.head.next
        return self.head   

    def max_min_ele(self):
        
        if self.head is None:
            raise Exception("Empty List")
        
        max_val = float('-inf')
        min_val = float('inf')
        current = self.head
        while current:
            if current.data > max_val:
                max_val = current.data
            if current.data < min_val:
                min_val = current.data
            current = current.next
            if current == self.head:
                break
        return max_val, min_val
    
    def middle_element_of_list(self):
        
        if self.is_empty():
            raise Exception("List is empty")
        
        if self.head.next is None:
            return self.head
        
        ############# O(N) Approach ###############
        # temp = self.head
        # count = 0
        # while count != self.size//2:
        #     count += 1
        #     temp = temp.next
        # return temp

        ######### Two Pointer Approach ########
        slow = self.head
        fast = self.head

        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next

        return slow       

if __name__ == '__main__':
    cdll = CircularDoublyLinkedList()

    while True:
        print("\n===== Circular Doubly Linked List Menu =====")
        print("1. Display List")
        print("2. Insert at Beginning")
        print("3. Insert at End")
        print("4. Insert at Position")
        print("5. Search Element")
        print("6. Delete Element")
        print("7. Reverse List")
        print("8. Get Size")
        print("9. Middle Element of List")
        print("10. Maximum and Minimum Value")
        print("11. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            cdll.display()

        elif choice == 2:
            val = int(input("Enter value: "))
            cdll.insert_at_beginning(val)
            cdll.display()

        elif choice == 3:
            val = int(input("Enter value: "))
            cdll.insert_at_end(val)
            cdll.display()

        elif choice == 4:
            val = int(input("Enter value: "))
            pos = int(input("Enter position: "))
            try:
                cdll.insert_in_middle(val, pos)
                cdll.display()
            except Exception as e:
                print(e)

        elif choice == 5:
            val = int(input("Enter value to search: "))
            try:
                result = cdll.search(val)
                if result == -1:
                    print("Element not found")
                else:
                    print("Element found at index:", result)
            except Exception as e:
                print(e)

        elif choice == 6:
            val = int(input("Enter value to delete: "))
            try:
                cdll.delete_node(val)
                print("Deleted successfully")
                cdll.display()
            except Exception as e:
                print(e)

        elif choice == 7:
            try:
                cdll.reverse()
                cdll.display()
            except Exception as e:
                print(e)

        elif choice == 8:
            print("Size of list:", cdll.size)
            cdll.display()

        elif choice == 9:
            try:
                print("Middle Element is : ", cdll.middle_element_of_list().data)
            except Exception as e:
                print(e)

        elif choice == 10:
            try:
                print("Maximum Element is : ", cdll.max_min_ele()[0])
                print("Minimum Element is : ", cdll.max_min_ele()[1])
            except Exception as e:
                print(e)                

        elif choice == 11:
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again!")