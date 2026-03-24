# Queue follows First In First Out (FIFO) principle
# The element inserted first is removed first
# Queue has two ends:
# FRONT -> deletion (dequeue)
# REAR  -> insertion (enqueue)

# Ways to implement Queue in Python:
# 1. Using Lists
# 2. Using Linked Lists
# 3. Using Collections (deque)
# 4. Using Heaps
# 5. Using queue module (not preferred for DSA)
# 6. Using asyncio (not used in DSA)

class MyQueue:

    # Constructor: Initializes an empty queue using a Python list
    # This function is automatically called when an object is created.
    # It creates an empty list which will store queue elements.
    # Time Complexity: O(1)
    def __init__(self):
        self.queue = []
    

    # is_empty: Checks whether the queue is empty or not
    # Returns True if queue has no elements, otherwise False.
    # Useful before performing dequeue or peek operations.
    # Time Complexity: O(1)
    def is_empty(self):
        return len(self.queue) == 0
    

    # display: Prints all elements of the queue
    # If queue is empty, prints a message.
    # Otherwise, displays elements from front to rear.
    # Time Complexity: O(N)
    def display(self):
        if self.is_empty():
            print("Queue is Empty!!")
            return 
        print("Queue elements:", self.queue)    
    

    # enqueue: Inserts an element at the rear (end) of the queue
    # Uses append() which adds element at the end of list.
    # Time Complexity: O(1)
    def enqueue(self, data):
        self.queue.append(data)
        print(f"Enqueued {data} successfully")
    

    # dequeue: Removes and returns the front element of the queue
    # Uses pop(0) which removes the first element.
    # Note: pop(0) takes O(N) time because elements shift left.
    # Time Complexity: O(N)
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!!")
            return 
        return self.queue.pop(0)
    

    # front_peek: Returns the front element without removing it
    # Helps to see which element will be dequeued next.
    # Time Complexity: O(1)
    def front_peek(self):
        if self.is_empty():
            print("Queue is Empty!!")
            return 
        return self.queue[0]
    

    # rear_peek: Returns the last element of the queue
    # Helps to see the most recently added element.
    # Time Complexity: O(1)
    def rear_peek(self):
        if self.is_empty():
            print("Queue is Empty!!")
            return 
        return self.queue[-1]


# Main driver code: Menu-driven implementation
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