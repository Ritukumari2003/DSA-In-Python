from collections import deque

class MyQueue:

    # Constructor: Initializes queue using two stacks (stack1 and stack2)
    # stack1 is used for enqueue (insertion operation)
    # stack2 is used for dequeue (removal operation)
    # This approach helps simulate FIFO (queue) using LIFO (stack)
    # Time Complexity: O(1)
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()


    # is_empty: Checks whether the queue is empty
    # Queue is empty only when both stack1 and stack2 are empty
    # Returns True if empty, otherwise False
    # Time Complexity: O(1)
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
    

    # display: Prints all elements of the queue from front to rear
    # Does NOT modify the queue
    # Time Complexity: O(N)
    def display(self):
        if self.is_empty():
            print("Queue is empty!..")
            return
        
        # Print elements from stack2 (front part)
        for i in range(len(self.stack2) - 1, -1, -1):
            print(self.stack2[i], end=' ')
        
        # Print elements from stack1 (rear part)
        for i in range(0, len(self.stack1)):
            print(self.stack1[i], end=' ')
        
        print()
        

    # enqueue: Inserts an element into the queue
    # Time Complexity: O(1)
    def enqueue(self, data):
        self.stack1.append(data)


    # dequeue: Removes and returns the front element of the queue
    # Time Complexity: Amortized O(1)
    def dequeue(self):
        if self.is_empty():
            print("Queue is already empty!..")
            return
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2.pop()
    

    # front_peek: Returns the front element without removing it
    # Time Complexity: Amortized O(1)
    def front_peek(self):
        if self.is_empty():
            print("Queue is empty!..")
            return
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop()) 
        
        return self.stack2[-1]
    

    # rear_peek: Returns the last inserted element (rear of queue)
    # Time Complexity: Amortized O(1)
    def rear_peek(self):
        if self.is_empty():
            print("Queue is empty!..")
            return
        
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())        
        
        return self.stack1[-1]
    

if __name__ == "__main__":
    q = MyQueue()

    while True:
        print("\n--- Queue (Using Two Stacks) ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front Peek")
        print("4. Rear Peek")
        print("5. Display")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter element to enqueue: "))
            q.enqueue(data)

        elif choice == 2:
            print("Dequeued:", q.dequeue())

        elif choice == 3:
            print("Front element:", q.front_peek())

        elif choice == 4:
            print("Rear element:", q.rear_peek())

        elif choice == 5:
            q.display()  

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")