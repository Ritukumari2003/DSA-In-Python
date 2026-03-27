# ================== CHAINING METHOD IN HASHING ==================
# Chaining is a collision resolution technique used in hash tables.
# When multiple keys hash to the same index, instead of replacing the value,
# we store all elements in that index using a list (called a bucket).
#
# Each index of the hash table stores a list of (key, value) pairs.
#
# Example:
# If hash("a") = 2 and hash("b") = 2,
# then both will be stored at index 2:
# table[2] = [("a", val1), ("b", val2)]
#
# Advantages:
# 1. Simple and easy to implement
# 2. Efficient for handling collisions
# 3. No need for probing
#
# Disadvantages:
# 1. Extra memory is required for storing lists
# 2. Worst-case time complexity becomes O(n)
#
# Time Complexity:
# Average case:
#   Insert: O(1)
#   Search: O(1)
# Worst case:
#   Insert/Search: O(n)
# ===============================================================


class chaining_hash_table:

    # Constructor to initialize the hash table with given size
    def __init__(self, size = 5):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    # Hash function to convert key into an index
    def hash_fn(self, key):
        return sum(ord(ch) for ch in key) % self.size
    
    # Function to display the entire hash table
    def display(self):
        for i, bucket in enumerate(self.table):
           print(f'{i}: {bucket}')

    # Function to insert a key-value pair into the hash table
    def insert(self, key, value = None):
        index = self.hash_fn(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
        
    # Function to search for a key in the hash table
    def search(self, key):
        index = self.hash_fn(key)
        for (k, v) in self.table[index]:
            if k == key:
                return (k, v)
        return None

if __name__=='__main__':
    ht = chaining_hash_table()

    while True:
        print("\n------ CHAINING HASH TABLE MENU ------")
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
            value = input("Enter value: ")
            ht.insert(key, value)
            print("Inserted successfully!")

        elif choice == 2:
            key = input("Enter key to search: ")
            result = ht.search(key)
            if result:
                print("Found:", result)
            else:
                print("Key not found")

        elif choice == 3:
            ht.display()

        else:
            print("Invalid choice! Try again.")
