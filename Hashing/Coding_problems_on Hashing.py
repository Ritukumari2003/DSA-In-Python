# Problems on Hashing

# Count number of each character in a string
def char_count(s):
    freq = dict()
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


# Find the first non-repeating character in the string 
def first_non_repeating_ch(s):
    freq = dict()
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for (k, v) in freq.items():
        if v == 1:
            return (k, v)
    return None


# Two Sum problem
def two_sum(sequence, target_sum):
    diff_map = dict()
    count = 0
    for x in sequence:
        diff = target_sum - x
        if diff in diff_map:
            count += diff_map[diff]
            print((x, diff), end=' ')
        diff_map[x] = diff_map.get(x, 0) + 1
    print()
    return count


def main():
    while True:
        print("\n--- SELECT ---")
        print("1. Count frequency of characters")
        print("2. First non-repeating character")
        print("3. Two Sum problem")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            s = input("Enter a string: ")
            result = char_count(s)
            print("Character Frequency:", result)

        elif choice == 2:
            s = input("Enter a string: ")
            result = first_non_repeating_ch(s)
            if result:
                print("First non-repeating character:", result)
            else:
                print("No non-repeating character found")

        elif choice == 3:
            nums = list(map(int, input("Enter numbers (space separated): ").split()))
            target = int(input("Enter target sum: "))
            count = two_sum(nums, target)
            print("Total pairs:", count)

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")

main()