
def binary_search(roll_numbers, target):
    low = 0
    high = len(roll_numbers) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if roll_numbers[mid] == target:
            return mid, comparisons
        elif roll_numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# Student records
roll_numbers = [101, 105, 110, 115, 120, 125, 130, 135, 140]

print("Student Roll Numbers:", roll_numbers)

n = int(input("Enter number of roll numbers to search: "))

total_comparisons = 0

for i in range(n):
    target = int(input("Enter roll number to search: "))

    result, comparisons = binary_search(roll_numbers, target)

    total_comparisons += comparisons

    if result != -1:
        print("Roll Number Found at position:", result + 1)
    else:
        print("Roll Number Not Found")

    print("Number of comparisons:", comparisons)

print("\nTotal Comparisons:", total_comparisons)