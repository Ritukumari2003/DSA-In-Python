
class MaxHeap:
    def __init__(self):
        self.heap = []

    # Insert element
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    # Using iteration 
    # def heapify_up(self, index):
    #     while index > 0:
    #         parent = (index - 1) // 2

    #         if self.heap[parent] < self.heap[index]:
    #             self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
    #             index = parent
    #         else:
    #             break

    # Recursive Heapify Up
    def heapify_up(self, index):
        if index == 0:
            return

        parent = (index - 1) // 2

        if self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]

            self.heapify_up(parent)

    # Remove maximum element
    def remove_max(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify_down(0)

        return root
    
    # Using iteration 
    # def heapify_down(self, index):
    #     size = len(self.heap)

    #     while True:
    #         largest = index
    #         left = 2 * index + 1
    #         right = 2 * index + 2

    #         if left < size and self.heap[left] > self.heap[largest]:
    #             largest = left

    #         if right < size and self.heap[right] > self.heap[largest]:
    #             largest = right

    #         if largest != index:
    #             self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
    #             index = largest
    #         else:
    #             break


    # Recursive Heapify Down
    def heapify_down(self, index):
        largest = index

        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]

            self.heapify_down(largest)

    # Print heap
    def print_heap(self):
        print(self.heap)


# Main Function
def main():
    h = MaxHeap()

    h.insert(10)
    h.insert(5)
    h.insert(20)
    h.insert(30)
    h.insert(8)

    print("Heap after insertion:")
    h.print_heap()

    print("Removed Maximum Element:", h.remove_max())

    print("Heap after deletion:")
    h.print_heap()


# Driver Code
if __name__ == "__main__":
    main()