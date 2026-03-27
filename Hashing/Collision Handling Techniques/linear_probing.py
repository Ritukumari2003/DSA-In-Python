# ================== LINEAR PROBING IN HASHING ==================
# Linear Probing is a collision resolution technique used in hash tables.
#
# When two keys hash to the same index (collision),
# instead of storing them in a list (like chaining),
# we search for the next available empty slot in the table.
#
# This is done sequentially (linearly), hence the name "Linear Probing".
#
# Formula:
#   index = (hash(key) + i) % table_size
# where i = 0, 1, 2, 3, ... until an empty slot is found
#
# Example:
# Suppose table size = 5
# hash("a") = 2 → placed at index 2
# hash("b") = 2 → collision
# Try next:
#   index = (2 + 1) % 5 = 3 → if empty, place here
#
# So final table:
# index 2 → ("a", val1)
# index 3 → ("b", val2)
#
# Advantages:
# 1. Simple to implement
# 2. No extra memory needed (unlike chaining)
# 3. Cache-friendly (stored in contiguous memory)
#
# Disadvantages:
# 1. Clustering problem (primary clustering)
#    → consecutive filled slots increase search time
# 2. Performance degrades as table becomes full
# 3. Deletion is tricky (requires special handling like "tombstones")
#
# Time Complexity:
# Average case:
#   Insert: O(1)
#   Search: O(1)
#
# Worst case (when clustering occurs):
#   Insert/Search: O(n)
#
# Load Factor (Important Concept):
#   load_factor = number_of_elements / table_size
#
# If load factor becomes high (> 0.7 approx),
# performance decreases significantly → need rehashing
# ===============================================================

class LinearProbingHashing:
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

    # Function to insert a key using linear probing
    def insert(self, key):
        h = self.hash_fn(key)
        for i in range(self.size):
            index = (h + i) % self.size
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
            index = (h + i) % self.size
            if self.table[index] is None:
                return False
            if self.table[index] == key:
                return index
        return False

if __name__ == '__main__':
    lp_hash = LinearProbingHashing()

    while True:
        print("\n------ LINEAR PROBING MENU ------")
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
                lp_hash.insert(key)
            except Exception as e:
                print(e)

        elif choice == 2:
            key = input("Enter key to search: ")
            result = lp_hash.search(key)
            if result is not False:
                print(f"Key found at index: {result}")
            else:
                print("Key not found")

        elif choice == 3:
            lp_hash.display()

        else:
            print("Invalid choice! Try again.")
    