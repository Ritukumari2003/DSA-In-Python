# Doubly Linked List

# Node class represents each element of the list
# Each node contains:
# 1. prev pointer → points to previous node
# 2. data → stores value
# 3. next pointer → points to next node
class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None


# Main class for Doubly Linked List
class DoublyLinkedList:

    # Initializes an empty list with head = None and size = 0
    def __init__(self):
        self.head = None
        self.size = 0
    
    # Checks whether the list is empty or not
    # Returns True if list is empty, else False
    def is_empty(self):
        return self.head is None

    # Displays all elements of the doubly linked list
    # Traverses from head to last node using next pointers
    def display(self):
        if self.is_empty():
            print('Empty List')
            return

        current = self.head

        while current:
            print(current.data, end=' ')
            current = current.next 
        print()

    # Inserts a node at the beginning of the list
    # Updates head and adjusts prev/next pointers accordingly
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
    
    # Inserts a node at the end of the list
    # Traverses to last node and attaches new node
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
    
    # Inserts a node at a given position (index-based)
    # Handles insertion at beginning, end, and middle
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
            count += 1
        node.next = current.next
        node.next.prev = node
        current.next = node
        node.prev = current
        self.size += 1
        return self.head        
    
    # Searches for a value in the list
    # Returns index if found, else returns -1
    def search(self, val):
        if self.is_empty():
            raise Exception("Empty List")
        current = self.head
        index = 0
        while current:
            if current.data == val:
                return index
            current = current.next
            index += 1
        return -1
    
    # Deletes a node with given value
    # Handles:
    # 1. Single node deletion
    # 2. Head node deletion
    # 3. Middle/last node deletion
    def delete_node(self, val):
        if self.is_empty():
            raise Exception("Empty List")
        
        current = self.head
        
        # single node deletion 
        if current.next is None:
            if current.data == val:
                self.head = None
                self.size -= 1
                return None
            else:
                raise Exception("Key Not Found!!..") 

        # delete head node 
        if current.data == val:
            self.head = current.next
            self.head.prev = None
            current.next = None
            self.size -= 1
            return self.head
        
        # delete other nodes 
        prev = None
        while current:
            if current.data == val:
                prev.next = current.next
                if current.next:
                    current.next.prev = prev
                current.next = None
                self.size -= 1
                return self.head
            prev = current
            current = current.next  

        raise Exception("Key Not Found!!..")   

    # Reverses the doubly linked list
    # Swaps prev and next pointers for each node
    # Finally updates head to the last processed node
    def reverse(self):
        if self.is_empty():
            raise Exception("Empty List")

        if self.head.next is None:
            return self.head
        
        current = self.head

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp

            current = current.prev
        
        self.head = temp.prev
        return self.head      

    def middle_element_of_list(self):
        ############# O(N) Approach ###############
        # if self.head.next is None:
        #     return self.head
        # length = 0
        # temp = self.head 
        # while temp:
        #     length += 1
        #     temp = temp.next
        # temp = self.head
        # count = 0
        # while count != length//2:
        #     count += 1
        #     temp = temp.next
        # return temp

        ######### Two Pointer Approach ########
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow   
    
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
        return max_val, min_val

if __name__ == '__main__':
    dll = DoublyLinkedList()

    while True:
        print("\n===== Doubly Linked List Menu =====")
        print("1. Display")
        print("2. Insert at Beginning")
        print("3. Insert at End")
        print("4. Insert at Position")
        print("5. Search")
        print("6. Delete")
        print("7. Reverse")
        print("8. Get Size")
        print("9. Middle Element of List")
        print("10. Maximum and Minimum Value")
        print("11. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            dll.display()

        elif choice == 2:
            val = int(input("Enter value: "))
            dll.insert_at_beginning(val)
            dll.display()

        elif choice == 3:
            val = int(input("Enter value: "))
            dll.insert_at_end(val)
            dll.display()

        elif choice == 4:
            val = int(input("Enter value: "))
            pos = int(input("Enter position: "))
            try:
                dll.insert_in_middle(val, pos)
                dll.display()
            except Exception as e:
                print(e)

        elif choice == 5:
            val = int(input("Enter value to search: "))
            try:
                res = dll.search(val)
                if res == -1:
                    print("Element not found")
                else:
                    print("Element found at index:", res)
            except Exception as e:
                print(e)

        elif choice == 6:
            val = int(input("Enter value to delete: "))
            try:
                dll.delete_node(val)
                print("Deleted successfully")
                dll.display()
            except Exception as e:
                print(e)

        elif choice == 7:
            try:
                dll.reverse()
                print("List reversed")
                dll.display()
            except Exception as e:
                print(e)

        elif choice == 8:
            print("Size of the Linked List: ", dll.size)

        elif choice == 9:
            print("Middle Element is : ", dll.middle_element_of_list().data)

        elif choice == 10:
            try:
                print("Maximum Element is : ", dll.max_min_ele()[0])
                print("Minimum Element is : ", dll.max_min_ele()[1])
            except Exception as e:
                print(e)                

        elif choice == 11:
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")