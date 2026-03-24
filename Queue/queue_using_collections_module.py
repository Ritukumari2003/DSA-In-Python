from collections import deque

class MyQueue:

    # Constructor: Initializes an empty queue using deque
    # deque (double-ended queue) allows fast insertion and deletion from both ends.
    # It is more efficient than a list for queue operations.
    # Time Complexity: O(1)
    def __init__(self):
        self.queue = deque()


    # is_empty: Checks whether the queue is empty
    # Returns True if there are no elements, otherwise False
    # Useful before performing dequeue or peek operations
    # Time Complexity: O(1)
    def is_empty(self):
        return len(self.queue) == 0
    

    # display: Prints all elements of the queue
    # If queue is empty, prints a message
    # Otherwise, converts deque to list for better readability
    # Elements are displayed from front to rear
    # Time Complexity: O(N)
    def display(self):
        if self.is_empty():
            print("Queue is Empty!!")
            return 
        print("Queue elements:", list(self.queue)) 


    # enqueue: Inserts an element at the rear (end) of the queue
    # Uses append() which adds element to the right end of deque
    # Time Complexity: O(1)
    def enqueue(self, data):
        self.queue.append(data)
        print(f"Enqueued {data} successfully")


    # dequeue: Removes and returns the front element of the queue
    # NOTE: Using pop(0) here, which is not optimal for deque
    # Ideally, deque.popleft() should be used for O(1) removal
    # Current implementation behaves like list-based removal
    # Time Complexity: O(N)
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!!")
            return
        return self.queue.popleft() 


    # front_peek: Returns the front element without removing it
    # The front element is at index 0
    # Time Complexity: O(1)
    def front_peek(self):
        if self.is_empty():
            print("Queue is Empty!!")
            return 
        return self.queue[0]


    # rear_peek: Returns the last element of the queue
    # The rear element is at the end of deque
    # Time Complexity: O(1)
    def rear_peek(self):
        if self.is_empty():
            print("Queue is Empty!!")
            return 
        return self.queue[-1]


# Main driver code: Menu-driven program for queue operations
if __name__ == "__main__":
    q = MyQueue()

    while True:
        print("\n--- Queue Menu ---")
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