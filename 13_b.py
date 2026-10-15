n = int(input("Enter the number of students: "))
marks = []

for i in range(n):
    mark = int(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)

print("\nOriginal marks:", marks)

def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        least = i

        for j in range(i + 1, n):
            if arr[j] < arr[least]:
                least = j

        arr[i], arr[least] = arr[least], arr[i]

    return arr

print("Bubble Sort:", bubble_sort(marks))
print("Insertion Sort:", insertion_sort(marks))
print("Selection Sort:", selection_sort(marks))