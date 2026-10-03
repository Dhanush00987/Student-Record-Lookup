# Student Record Lookup Using Binary Search

## Description

Student Record Lookup is a Python-based project that uses the Binary Search algorithm to efficiently search student records using unique roll numbers. A university maintains thousands of student records, and searching for a particular student's information quickly is important, especially during examinations.

This project uses Binary Search to determine whether a particular roll number exists in the sorted list. It also counts the number of comparisons required when searching for multiple roll numbers.

## Problem Statement

A university maintains thousands of student records identified by unique roll numbers. During examinations, the system frequently needs to determine whether a particular roll number exists and retrieve the student's information quickly.

The main task is to design an efficient searching system using Binary Search and compare the number of operations required when searching for multiple roll numbers.

## Objectives

* To implement Binary Search using Python.
* To search student roll numbers efficiently.
* To reduce the number of comparisons.
* To search multiple roll numbers.
* To compare searching operations.

## Algorithm Used

**Binary Search (Divide and Conquer)**

Binary Search works by dividing a sorted list into two halves.

1. Find the middle element.
2. Compare it with the target roll number.
3. If both are equal, the element is found.
4. If the target is greater, search the right half.
5. If the target is smaller, search the left half.
6. Repeat until the element is found or the search area becomes empty.

## Technologies Used

* Programming Language: Python
* Algorithm: Binary Search
* Data Structure: List
* IDE: Python IDLE / VS Code

## Python Code

```python
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


roll_numbers = [101, 105, 110, 115, 120,
                125, 130, 135, 140]

print("Student Roll Numbers:", roll_numbers)

n = int(input("Enter number of roll numbers to search: "))

total_comparisons = 0

for i in range(n):
    target = int(input("Enter roll number to search: "))

    result, comparisons = binary_search(
        roll_numbers, target
    )

    total_comparisons += comparisons

    if result != -1:
        print("Roll Number Found at position:", result + 1)
    else:
        print("Roll Number Not Found")

    print("Number of comparisons:", comparisons)

print("Total Comparisons:", total_comparisons)
```

## Sample Output

```text
Student Roll Numbers: [101, 105, 110, 115, 120, 125, 130, 135, 140]

Enter number of roll numbers to search: 3

Enter roll number to search: 120
Roll Number Found at position: 5
Number of comparisons: 1

Enter roll number to search: 140
Roll Number Found at position: 9
Number of comparisons: 4

Enter roll number to search: 150
Roll Number Not Found
Number of comparisons: 4

Total Comparisons: 9
```

## Complexity Analysis

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(1)            |
| Average Case | O(log n)        |
| Worst Case   | O(log n)        |

**Space Complexity:** O(1)

## Advantages

* Fast searching for sorted records.
* Reduces the number of comparisons.
* Efficient for large datasets.
* Easy to implement using Python.

## Future Enhancements

* Store complete student details such as name, department and marks.
* Connect the application to a database.
* Add student record insertion and deletion.
* Develop a graphical user interface.

## Conclusion

This project demonstrates the use of Binary Search to search student roll numbers efficiently. It reduces searching time and comparisons by repeatedly dividing the sorted list into two halves. It is useful for managing and searching large student record datasets.

## References

1. T. H. Cormen et al., *Introduction to Algorithms*, 4th ed., MIT Press, 2022.
2. Python Documentation: https://docs.python.org/3/
3. Programiz – Binary Search: https://www.programiz.com/dsa/binary-search
