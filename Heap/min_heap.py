
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    # Using iteration 
    # def heapify_up(self, index):
    #     while index > 0:
    #         parent = (index - 1) // 2

    #         if self.heap[parent] > self.heap[index]:
    #             self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
    #             index = parent
    #         else:
    #             break

    # Using Recursion 
    def heapify_up(self, index):
        if index == 0:
            return

        parent = (index - 1) // 2

        if self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)
    
    
    def remove_min(self):
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
    #         smallest = index
    #         left = 2 * index + 1
    #         right = 2 * index + 2

    #         if left < size and self.heap[left] < self.heap[smallest]:
    #             smallest = left

    #         if right < size and self.heap[right] < self.heap[smallest]:
    #             smallest = right

    #         if smallest != index:
    #             self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
    #             index = smallest
    #         else:
    #             break

    # Recursive Heapify Down
    def heapify_down(self, index):
        smallest = index

        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]

            self.heapify_down(smallest)


    def print_heap(self):
        print(self.heap)

# Main Function
def main():
    h = MinHeap()

    h.insert(10)
    h.insert(5)
    h.insert(20)
    h.insert(2)
    h.insert(8)

    print("Heap after insertion:")
    h.print_heap()

    print("Removed Minimum Element:", h.remove_min())

    print("Heap after deletion:")
    h.print_heap()


# Driver Code
if __name__ == "__main__":
    main()