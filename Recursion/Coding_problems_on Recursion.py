# Print Numbers from N to 1
def print_n_to_1(n):
    if n == 0:
        return 
    print(n, end=' ')
    return print_n_to_1(n-1)


# Print sum of first N natural numbers 
def print_sum(n):
    if n == 0:
        return 0
    return n + print_sum(n-1)


# Count digits in a given number
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n//10)


# Power Function 
def power(n, e):
    if e == 0:
        return 1
    return n * power(n, e-1)

if __name__ == "__main__":

    while True:
        print("\n--- Recursion Menu ---")
        print("1. Print numbers from N to 1")
        print("2. Sum of first N natural numbers")
        print("3. Count digits in a number")
        print("4. Power (n^e)")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter value of N: "))
            print_n_to_1(n)
            print()   # for new line

        elif choice == 2:
            n = int(input("Enter value of N: "))
            print("Sum:", print_sum(n))

        elif choice == 3:
            n = int(input("Enter number: "))
            print("Number of digits:", count_digits(n))

        elif choice == 4:
            n = int(input("Enter base: "))
            e = int(input("Enter exponent: "))
            print("Result:", power(n, e))

        elif choice == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")