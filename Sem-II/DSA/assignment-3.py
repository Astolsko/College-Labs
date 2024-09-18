# performing insertion deletion searching min max in sorted array
def print_menu():
    print("\nOperations on Sorted Array:")
    print("1. Display Array")
    print("2. Insert Element")
    print("3. Delete Element")
    print("4. Search Element")
    print("5. Find Minimum")
    print("6. Find Maximum")
    print("7. Exit")

def display_array(arr):
    print("Current Array:", arr)

def insert_element(arr, element):
    arr.append(element)
    arr.sort()
    print("Element", element, "inserted into the array.")

def delete_element(arr, element):
    if element in arr:
        arr.remove(element)
        print("Element", element, "deleted from the array.")
    else:
        print("Element", element, "not found in the array.")

def search_element(arr, element):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            print("Element", element, "found at index position:", mid)
            return
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    print("Element", element, "not found in the array.")

def find_minimum(arr):
    if arr:
        print("Minimum element in the array:", min(arr))
    else:
        print("Array is empty.")

def find_maximum(arr):
    if arr:
        print("Maximum element in the array:", max(arr))
    else:
        print("Array is empty.")

if __name__ == "__main__":
    arr = [i for i in range(16)]

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_array(arr)
        elif choice == "2":
            element = int(input("Enter element to insert: "))
            insert_element(arr, element)
        elif choice == "3":
            element = int(input("Enter element to delete: "))
            delete_element(arr, element)
        elif choice == "4":
            element = int(input("Enter element to search: "))
            search_element(arr, element)
        elif choice == "5":
            find_minimum(arr)
        elif choice == "6":
            find_maximum(arr)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
