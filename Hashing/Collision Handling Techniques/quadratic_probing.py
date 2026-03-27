# ================== QUADRATIC PROBING IN HASHING ==================
# Quadratic Probing is a collision resolution technique used in hash tables.
#
# When a collision occurs (i.e., two keys map to the same index),
# instead of checking the next index sequentially (like linear probing),
# we jump using a quadratic function.
#
# Formula:
#   index = (hash(key) + i^2) % table_size
# where i = 0, 1, 2, 3, ... until an empty slot is found
#
# Example:
# Suppose table size = 7
# hash("a") = 2 → placed at index 2
# hash("b") = 2 → collision
#
# Try:
#   i = 1 → (2 + 1^2) % 7 = 3
#   i = 2 → (2 + 2^2) % 7 = 6
#   i = 3 → (2 + 3^2) % 7 = 4
#
# So probing sequence: 2 → 3 → 6 → 4 → ...
#
# Advantages:
# 1. Reduces primary clustering (better than linear probing)
# 2. Spreads keys more uniformly
#
# Disadvantages:
# 1. Secondary clustering still exists
#    → keys with same initial hash follow same probe sequence
# 2. May not check all slots (depends on table size)
# 3. Requires careful table size selection (preferably prime)
#
# Time Complexity:
# Average case:
#   Insert: O(1)
#   Search: O(1)
#
# Worst case:
#   Insert/Search: O(n)
#
# Load Factor:
#   load_factor = number_of_elements / table_size
#
# For good performance:
#   load_factor < 0.5 (recommended for quadratic probing)
#
# Note:
# If table becomes too full, rehashing is required.
# ===============================================================


class QuadraticProbingHashing:
    def __init__(self, size = 5):
        self.size = size
        self.table = [None] * self.size
    
    # Hash function to convert key into an index
    def hash_fn(self, key):
        return sum(ord(ch) for ch in key) % self.size
    
    # Function to display the hash table
    def display(self):
        print("Hash Table:", self.table)
        print()

    # Function to insert a key using quadratic probing
    def insert(self, key):
        h = self.hash_fn(key)
        for i in range(self.size):
            index = (h + i*i) % self.size
            if self.table[index] is None:
                self.table[index] = key
                print(f'Key: {key}, Original Index: {h}, New Index: {index}')
                self.display()
                return True
        raise Exception("Hash table is full!!")

    # Function to search a key in the hash table
    def search(self, key):
        h = self.hash_fn(key)
        for i in range(self.size):
            index = (h + i*i) % self.size
            if self.table[index] is None:
                return False
            if self.table[index] == key:
                return index
        return False


if __name__ == '__main__':
    qp_hash = QuadraticProbingHashing()

    while True:
        print("\n------ QUADRATIC PROBING MENU ------")
        print("1. Insert")
        print("2. Search")
        print("3. Display")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 4:
            print("Exiting program...")
            break

        elif choice == 1:
            key = input("Enter key: ")
            try:
                qp_hash.insert(key)
            except Exception as e:
                print(e)

        elif choice == 2:
            key = input("Enter key to search: ")
            result = qp_hash.search(key)
            if result is not False:
                print(f"Key found at index: {result}")
            else:
                print("Key not found")

        elif choice == 3:
            qp_hash.display()

        else:
            print("Invalid choice! Try again.")