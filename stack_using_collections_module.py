# Implemented using data structure called 'deque' which is a doubly linked list from python built in module named collections, so we can use it to implement both stack and queue
# deletion and insertion of elements using deque takes O(1) Time

from collections import deque

class MyStack:
    def __init__(self):
        self.stack = deque()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def get_size(self):
        return len(self.stack)
    
    def display(self):
        if self.is_empty():
            print("Stack is Empty")
            return
        print("Stack elements:", list(self.stack))
    
    def push(self, data):
        self.stack.append(data)
        print(f'Pushed {data} successfully')
    
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop.")
            return -1
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return -1
        return self.stack[-1]


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