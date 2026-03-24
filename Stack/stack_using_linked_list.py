# Stack using Linked List 

class Node:
    # Constructor to initialize a node with given data and next pointer as None
    def __init__(self, data):
        self.next = None
        self.data = data


class MyStack:
    # Constructor to initialize stack with top pointer as None (empty stack)
    def __init__(self):
        self.top = None
    
    # Function to check whether the stack is empty
    def is_empty(self):
        return self.top is None
    
    # Function to display all elements of the stack from top to bottom
    def display(self):
        if self.is_empty():
            print("Stack is Empty")
            return
        
        current = self.top
        while current:
            print(current.data)
            current = current.next
        print()

    # Function to push (insert) a new element onto the stack
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        print(f"Pushed {data} successfully")
    
    # Function to pop (remove) the top element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop.")
            return -1
        
        current = self.top
        self.top = current.next
        return current.data
    
    # Function to return the top element without removing it
    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return -1
        return self.top.data
    
    # Function to get size of stack
    def get_size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count


# -------- Menu Driven Program --------
if __name__ == "__main__":
    s = MyStack()

    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter element to push: "))
            s.push(data)

        elif choice == 2:
            print("Popped:", s.pop())

        elif choice == 3:
            print("Top element:", s.peek())

        elif choice == 4:
            s.display()

        elif choice == 5:
            print("Size of stack:", s.get_size())

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")