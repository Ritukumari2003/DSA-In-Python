# Common operations in Stack 
# Push
# Pop 
# Peek 
# isEmpty()

# Implementation of stack in python is done in three ways 
# using 'lists' to behave like a stack
# collections : dequeue :::: Meant to be the optimal way of implementing a stack
# using 'linked list' to behave like a stack

# Implement Stack Using List
# Implementation of Stack using Python List (Menu Driven)

class MyStack:
    
    # Constructor to initialize the stack
    def __init__(self):
        self.stack = []

    # Function to return size of stack
    def get_size(self):
        return len(self.stack)
    
    # Function to check if stack is empty
    def is_empty(self):
        return self.get_size() == 0
    
    # Function to display stack elements (Top to Bottom)
    def display(self):
        if self.is_empty():
            print("Empty Stack")
            return
        print("Stack elements:")
        for ele in self.stack[::-1]:
            print(ele)
    
    # Function to push element into stack
    def push(self, data):
        self.stack.append(data)
        print(f"{data} pushed into stack")
    
    # Function to pop element from stack
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop.")
            return
        popped = self.stack.pop()
        print(f"{popped} popped from stack")
    
    # Function to get top element without removing it
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print(f"Top element is: {self.stack[-1]}")

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
            s.pop()

        elif choice == 3:
            s.peek()

        elif choice == 4:
            s.display()

        elif choice == 5:
            print("Size of stack:", s.get_size())

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")
