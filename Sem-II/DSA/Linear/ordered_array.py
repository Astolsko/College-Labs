def insert_value_ordered(array):
    value = int(input("Enter the value to insert: "))
    inserted = False
    for i in range(len(array)):
        if value <= array[i]:
            array.insert(i, value)
            inserted = True
            break
    if not inserted:
        array.append(value)
    print(f"Inserted {value} into the ordered array.")
    print(array)
def delete_value(array):
    value = int(input("Enter the value to delete: "))
    if value in array:
        array.remove(value)
        print(f"Deleted {value} from the array.")
    else:
        print(f"{value} not found in the array.")
def search_value(array):
    value = int(input("Enter the value to search: "))
    if value in array:
        print(f"{value} found at index {array.index(value)}.")
    else:
        print(f"{value} not found in the array.")
def find_min(array):
    if len(array) == 0:
        print("Array is empty.")
    else:
        min_val = min(array)
        print(f"The minimum value in the array is {min_val}.")
def find_max(array):
    if len(array) == 0:
        print("Array is empty.")
    else:
        max_val = max(array)
        print(f"The maximum value in the array is {max_val}.")
array = []
while True:
    print("1. Insert value")
    print("2. Delete value")
    print("3. Search value")
    print("4. Find minimum value")
    print("5. Find maximum value")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        insert_value_ordered(array)
    elif choice == 2:
        delete_value(array)
    elif choice == 3:
        search_value(array)
    elif choice == 4:
        find_min(array)
    elif choice == 5:
        find_max(array)
    elif choice == 6:
        print("Exiting")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
