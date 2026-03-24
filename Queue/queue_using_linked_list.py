# Queue using Linked List 

class Node:

    # Constructor: Initializes a node for the linked list
    # Each node contains:
    # 1. data -> stores the value
    # 2. next -> pointer to the next node in the queue
    # Initially, next is set to None because the node is not linked yet.
    # Time Complexity: O(1)
    def __init__(self,data):
        self.data = data
        self.next = None


class MyQueue:

    # Constructor: Initializes an empty queue using linked list
    # front -> points to the first element (for dequeue)
    # rear  -> points to the last element (for enqueue)
    # Initially both are None since queue is empty
    # Time Complexity: O(1)
    def __init__(self):
        self.front = None
        self.rear = None


    # is_empty: Checks whether the queue is empty
    # Queue is empty when front is None
    # Returns True if empty, otherwise False
    # Time Complexity: O(1)
    def is_empty(self):
        return self.front == None
    

    # display: Prints all elements of the queue from front to rear
    # Traverses the linked list starting from front
    # If queue is empty, prints a message
    # Time Complexity: O(N)
    def display(self):
        if self.is_empty():
            print("Queue is Empty!!")
            return 
        current = self.front
        while current:
            print(current.data, end = ' ')
            current = current.next 
        print()


    # enqueue: Inserts a new element at the rear of the queue
    # Steps:
    # 1. Create a new node
    # 2. If queue is empty, set both front and rear to new node
    # 3. Otherwise, link new node at the end and update rear
    # Time Complexity: O(1)
    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.front = node
            self.rear = node
            return self.front
        
        self.rear.next = node
        self.rear = node
        return self.front


    # dequeue: Removes and returns the front element of the queue
    # Steps:
    # 1. If queue is empty → underflow condition
    # 2. If only one element → reset both front and rear to None
    # 3. Otherwise, move front to next node and unlink old node
    # Time Complexity: O(1)
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!!")
            return 
        
        if self.front is self.rear:
            self.front = None
            self.rear = None
            return self.front
        
        current = self.front
        self.front = self.front.next
        current.next = None

        return current.data


    # front_peek: Returns the front element without removing it
    # Gives the element which will be dequeued next
    # Assumes queue is not empty
    # Time Complexity: O(1)
    def front_peek(self):
        return self.front.data


    # rear_peek: Returns the last element of the queue
    # Gives the most recently added element
    # Assumes queue is not empty
    # Time Complexity: O(1)
    def rear_peek(self):
        return self.rear.data
    

# Main driver code: Menu-driven program to perform queue operations
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