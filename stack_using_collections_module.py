# Implemented using data structure called 'deque' which is a doubly linked list 
# from Python's built-in module 'collections'.
# deque allows fast insertion and deletion from both ends in O(1) time,
# making it suitable for implementing both stack and queue.

from collections import deque

class MyStack:

    # Constructor: Initializes the stack using deque
    # This function is automatically called when an object of MyStack is created.
    # It creates an empty deque which will store stack elements.
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __init__(self):
        self.stack = deque()
    

    # is_empty: Checks whether the stack is empty or not
    # Returns True if the stack has no elements, otherwise returns False.
    # This is useful before performing pop or peek to avoid errors.
    # Time Complexity: O(1)
    def is_empty(self):
        return len(self.stack) == 0
    

    # get_size: Returns the number of elements currently in the stack
    # Helps in understanding how many elements are present at any point.
    # Time Complexity: O(1)
    def get_size(self):
        return len(self.stack)
    

    # display: Prints all elements present in the stack
    # If the stack is empty, it prints a message.
    # Otherwise, it converts deque to list and prints elements.
    # Note: Elements are shown from bottom to top (left to right).
    # Time Complexity: O(N)
    def display(self):
        if self.is_empty():
            print("Stack is Empty")
            return
        print("Stack elements:", list(self.stack))
    

    # push: Inserts a new element at the top of the stack
    # Uses append() which adds element to the right end of deque.
    # This represents the top of the stack.
    # Time Complexity: O(1)
    def push(self, data):
        self.stack.append(data)
        print(f'Pushed {data} successfully')
    

    # pop: Removes and returns the top element of the stack
    # If the stack is empty, it handles underflow condition.
    # Uses pop() which removes element from the right end (top).
    # Time Complexity: O(1)
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop.")
            return -1
        return self.stack.pop()
    

    # peek: Returns the top element without removing it
    # Accesses the last element of deque using indexing.
    # If stack is empty, returns -1.
    # Time Complexity: O(1)
    def peek(self):
        if self.is_empty():
            return -1
        return self.stack[-1]


# Main driver code: Provides a menu-driven interface to interact with stack
if __name__ == '__main__':
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