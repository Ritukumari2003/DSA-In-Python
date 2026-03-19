# Singly Linked List 

# CLASS: Node
# PURPOSE:
# Represents a single node in the singly linked list.
# Each node stores the data value and a reference (pointer)
# to the next node in the list.
# The 'size' variable is defined but not actively used
# for managing the linked list size.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# CLASS: SinglyLinkedList
# PURPOSE:
# Represents the singly linked list structure.
# It maintains the 'head' pointer which always refers
# to the first node in the linked list.
# All operations such as insertion, deletion,
# searching and traversal are handled through this class.
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # FUNCTION: get_length()
    # PURPOSE:
    # Calculates and returns the total number of nodes
    # currently present in the linked list.
    #
    # WORKING:
    # Starts traversal from the head node and moves through
    # each node until reaching the end (None).
    # A counter variable keeps track of how many nodes are visited.
    #
    # RETURN:
    # Integer representing the number of nodes in the list.
    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
    

    # FUNCTION: display()
    # PURPOSE:
    # Prints all elements present in the linked list.
    #
    # WORKING:
    # If the list is empty, it prints "Empty List".
    # Otherwise it traverses from the head node and prints
    # each node's data value until the end of the list.
    #
    # OUTPUT:
    # Displays the linked list values in sequence.
    def display(self):
        if not self.head:
            print('Empty List')
        else:
            current = self.head
            while current:
                print(current.data, end=' ')
                current = current.next
            print()


    # FUNCTION: insert_at_beginning(val)
    # PURPOSE:
    # Inserts a new node at the beginning (head) of the linked list.
    #
    # PARAMETER:
    # val -> value to be stored in the new node.
    #
    # WORKING:
    # A new node is created.
    # The new node's next pointer is set to the current head node.
    # Then the head pointer is updated to the new node.
    #
    # RETURN:
    # Updated head of the linked list.
    def insert_at_beginning(self, val):
        node = Node(val)
        if self.head:
            node.next = self.head
        self.head = node
        self.size += 1  
        return self.head
    

    # FUNCTION: insert_at_end(val)
    # PURPOSE:
    # Inserts a new node at the end of the linked list.
    #
    # PARAMETER:
    # val -> value that will be stored in the new node.
    #
    # WORKING:
    # If the linked list is empty, the new node becomes the head.
    # Otherwise the list is traversed until the last node is found.
    # The last node's next pointer is updated to point to the new node.
    #
    # RETURN:
    # Updated head of the linked list.
    def insert_at_end(self, val):
        node = Node(val)
        
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1  
        return self.head   


    # FUNCTION: insert_in_middle(val, pos)
    # PURPOSE:
    # Inserts a node at a specific position inside the linked list.
    #
    # PARAMETERS:
    # val -> value to insert
    # pos -> position/index where the node should be inserted
    #
    # WORKING:
    # First the length of the list is calculated.
    # If the position is invalid, an exception is raised.
    # If position is 0 → node is inserted at the beginning.
    # If position equals the length → node is inserted at the end.
    # Otherwise traversal continues until reaching the node
    # just before the target position.
    # The new node is inserted by adjusting the next pointers.
    #
    # RETURN:
    # Updated head of the linked list.
    def insert_in_middle(self, val, pos):
        n = self.get_length()
        
        if pos<0 or pos>n:
            raise Exception("Invalid Index Error")

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
        self.size += 1  
        return self.head 
    

    # FUNCTION: search(val)
    # PURPOSE:
    # Searches for a specific value in the linked list.
    #
    # PARAMETER:
    # val -> value to search for.
    #
    # WORKING:
    # If the list is empty, "Empty List" is returned.
    # Otherwise traversal starts from the head.
    # Each node's data is compared with the target value.
    # If a match is found, the index of that node is returned.
    # If traversal finishes without finding the value,
    # the function returns -1.
    #
    # RETURN:
    # Index of the node if found
    # -1 if the value is not present
    # "Empty List" if the list has no nodes
    def search(self, val):
        if not self.head:
            return "Empty List"
        current = self.head
        index = 0
        while current:
            if current.data == val:
                return index
            current = current.next
            index += 1
        return -1
    

    # FUNCTION: delete_node(val)
    # PURPOSE:
    # Deletes the first node that contains the specified value.
    #
    # PARAMETER:
    # val -> value of the node that should be removed.
    #
    # WORKING:
    # If the list is empty, an exception is raised.
    # If the value exists in the head node,
    # the head pointer moves to the next node.
    # Otherwise the list is traversed using two pointers:
    # prev and current.
    # When the target node is found,
    # prev.next is updated to skip the current node,
    # effectively removing it from the list.
    #
    # RETURN:
    # Updated head of the linked list.
    def delete_node(self, val):

        # WE CAN TRY DELETING THE NODE USING THE DUMMY NODE TOO WHICH WILL BE BEFORE THE HEAD AND THE PREV NODE WILL POINT TO DUMMY
        # dummy = Node(0)
        # dummy.next = self.head
        # prev = dummy

        if self.head is None:
            raise Exception("List is empty")
        
        current = self.head

        # deletion at beginning 
        if current.data == val:
            self.head = current.next
            current.next = None
            self.size -= 1
            return self.head
        
        prev = None
        while current:
            if current.data == val:
                prev.next = current.next
                current.next = None
                self.size -= 1
                return self.head
            prev = current
            current = current.next
        raise Exception("Value not found in list")
    

    # FUNCTION: reverse_list(): ############ O(N) time, O(N) space ##############
    # PURPOSE:
    # Reverses the linked list by reversing the values stored in the nodes.
    # Instead of changing the node pointers, this method stores all node
    # values in a Python list, reverses that list, and then writes the
    # reversed values back into the linked list nodes.
    #
    # WORKING:
    # 1. First it checks whether the linked list is empty.
    #    If the list is empty, reversing is not possible.
    #
    # 2. If the list contains only one node, no reversal is needed,
    #    so the head is returned directly.
    #
    # 3. The function then traverses the linked list and stores
    #    each node's data into a Python list.
    #
    # 4. The built-in reversed() function is used to reverse the list.
    #
    # 5. The linked list is traversed again from the head and each
    #    node's data is replaced with the reversed values from the list.
    #
    # RETURN:
    # Returns the head of the modified linked list after reversal.    
    # def reverse_list(self):
    #     if self.head is None:
    #         raise Exception("List is empty, No reverse possible!!!")
        
    #     if not self.head.next:
    #         return self.head

    #     current = self.head
    #     l = []
    #     while current:
    #         l.append(current.data)
    #         current = current.next

    #     rev_list = reversed(l)
    #     current = self.head
    #     for i in rev_list:
    #         current.data = i
    #         current = current.next
        
    #     return self.head

    # FUNCTION: reverse_list() : ############ O(N) time, O(1) space ##############
    # PURPOSE:
    # Reverses the linked list by changing the node links (pointers)
    # instead of reversing the node values.
    #
    # WORKING:
    # The function uses three pointers:
    # prev, current and next.
    #
    # prev keeps track of the previous node,
    # current represents the node currently being processed,
    # and next temporarily stores the next node so that the
    # list is not lost when links are reversed.
    #
    # In each iteration:
    # 1. Store the next node
    # 2. Reverse the current node's pointer
    # 3. Move prev and current one step forward
    #
    # After the loop finishes, prev becomes the new head
    # of the reversed linked list.
    #
    # RETURN:
    # Returns the new head of the reversed linked list.
    
    def reverse_list(self):
        if self.head is None:
            raise Exception("List is empty, No reverse possible!!!")
        
        if not self.head.next:
            return self.head

        prev = None
        current = self.head
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        self.head = prev

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
        
if __name__ == '__main__':
    sll = SinglyLinkedList()

    while True:
        print("\n----- Singly Linked List Menu -----")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Delete Node")
        print("5. Search Node")
        print("6. Display List")
        print("7. Get Size")
        print("8. Reverse List")
        print("9. Middle Element of List")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter value to insert: "))
            sll.insert_at_beginning(val)
            print("Node inserted at beginning.")
            sll.display()

        elif choice == 2:
            val = int(input("Enter value to insert: "))
            sll.insert_at_end(val)
            print("Node inserted at end.")
            sll.display()

        elif choice == 3:
            val = int(input("Enter value to insert: "))
            pos = int(input("Enter position: "))
            try:
                sll.insert_in_middle(val, pos)
                print("Node inserted at position.")
                sll.display()
            except Exception as e:
                print(e)

        elif choice == 4:
            val = int(input("Enter value to delete: "))
            try:
                sll.delete_node(val)
                print("Node deleted successfully.")
                sll.display()
            except Exception as e:
                print(e)

        elif choice == 5:
            val = int(input("Enter value to search: "))
            result = sll.search(val)

            if result == -1:
                print("Node does not exist.")
            elif result == "Empty List":
                print("List is empty.")
            else:
                print("Node found at index:", result)
            sll.display()

        elif choice == 6:
            print("Linked List:")
            sll.display()

        elif choice == 7:
            print("Size of list:", sll.size)
            sll.display()

        elif choice == 8:
            try:
                sll.reverse_list()
                print("List reversed successfully.")
                sll.display()
            except Exception as e:
                print(e)
        
        elif choice == 9:
            print("Middle Element is : ", sll.middle_element_of_list().data)

        elif choice == 10:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")