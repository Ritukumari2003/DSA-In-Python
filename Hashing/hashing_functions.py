# Hashing functions 

# Simple Hash 
def simple_hash(key):
    total = 0
    for ch in key:
        total += ord(ch)
    return total

# Multiplicative Hash 
def multiplicative_hash(key):
    h = 1
    for ch in key:
        h = (h * 31) + ord(ch)
    return h

# DJB2 Hash 
def djb2(s):
    h = 5381
    for ch in s:
        h = (h << 31) + ord(ch)   
    return h

# Menu Driven Program
def main():
    while True:
        print("\n------ HASH FUNCTIONS MENU ------")
        print("1. Simple Hash")
        print("2. Multiplicative Hash")
        print("3. DJB2 Hash")
        print("4. Built-in Hash")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 5:
            print("Exiting program...")
            break

        key = input("Enter a string: ")

        if choice == 1:
            print("Simple Hash Value:", simple_hash(key))

        elif choice == 2:
            print("Multiplicative Hash Value:", multiplicative_hash(key))

        elif choice == 3:
            print("DJB2 Hash Value:", djb2(key))

        elif choice == 4:
            print("Built-in Hash Value:", hash(key))

        else:
            print("Invalid choice! Try again.")

# Run program
main()