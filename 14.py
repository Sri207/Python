SIZE = 10
hash_table = [None] * SIZE

def insert(roll, name):
    index = roll % SIZE

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] is None or hash_table[pos] == "DELETED":
            hash_table[pos] = (roll, name)
            print("Student record inserted successfully.")
            return

        if hash_table[pos][0] == roll:
            hash_table[pos] = (roll, name)
            print("Student record updated successfully.")
            return

    print("Hash table is full!")

def search(roll):
    index = roll % SIZE

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] is None:
            break

        if hash_table[pos] != "DELETED" and hash_table[pos][0] == roll:
            print("Student found:", hash_table[pos])
            return

    print("Student not found.")

def delete(roll):
    index = roll % SIZE

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] is None:
            break

        if hash_table[pos] != "DELETED" and hash_table[pos][0] == roll:
            hash_table[pos] = "DELETED"
            print("Student record deleted successfully.")
            return

    print("Student not found.")

def display():
    print("\nHash Table:")
    for i in range(SIZE):
        print(i, ":", hash_table[i])

while True:
    print("\n1. Insert Student Record")
    print("2. Search Student")
    print("3. Delete Student Record")
    print("4. Display Hash Table")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter roll number: "))
        name = input("Enter student name: ")
        insert(roll, name)

    elif choice == 2:
        roll = int(input("Enter roll number to search: "))
        search(roll)

    elif choice == 3:
        roll = int(input("Enter roll number to delete: "))
        delete(roll)

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Try again.")