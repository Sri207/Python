n = int(input("Enter the number of students: "))

roll_numbers = []

for i in range(n):
    roll = int(input(f"Enter roll number {i + 1}: "))
    roll_numbers.append(roll)


roll_numbers.sort()

print("\nRegistered roll numbers:", roll_numbers)
3
target = int(input("Enter the roll number to search: "))

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


linear_result = linear_search(roll_numbers, target)

if linear_result != -1:
    print("Linear Search: Roll number found")
else:
    print("Linear Search: Roll number not found")

binary_result = binary_search(roll_numbers, target)

if binary_result != -1:
    print("Binary Search: Roll number found")
else:
    print("Binary Search: Roll number not found")