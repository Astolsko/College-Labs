class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_value(head, value):
    new_node = Node(value)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
    print(f"Inserted {value} into the linked list.")
    return head
def delete_value(head, value):
    if head is None:
        print("Linked list is empty.")
        return head
    if head.data == value:
        head = head.next
        print(f"Deleted {value} from the linked list.")
        return head
    prev = None
    current = head
    while current:
        if current.data == value:
            prev.next = current.next
            print(f"Deleted {value} from the linked list.")
            return head
        prev = current
        current = current.next
    print(f"{value} not found in the linked list.")
    return head

def search_value(head, value):
    if head is None:
        print("Linked list is empty.")
        return
    index = 0
    current = head
    while current:
        if current.data == value:
            print(f"{value} found at index {index}.")
            return
        current = current.next
        index += 1
    print(f"{value} not found in the linked list.")

def find_min(head):
    if head is None:
        print("Linked list is empty.")
        return
    min_val = head.data
    current = head.next
    while current:
        if current.data < min_val:
            min_val = current.data
        current = current.next
    print(f"The minimum value in the linked list is {min_val}.")

def find_max(head):
    if head is None:
        print("Linked list is empty.")
        return
    max_val = head.data
    current = head.next
    while current:
        if current.data > max_val:
            max_val = current.data
        current = current.next
    print(f"The maximum value in the linked list is {max_val}.")

def display_list(head):
    if head is None:
        print("Linked list is empty.")
        return
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
head = None
while True:
    print("1. Insert value")
    print("2. Delete value")
    print("3. Search value")
    print("4. Find minimum value")
    print("5. Find maximum value")
    print("6. Display list")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter the value to insert: "))
        head = insert_value(head, value)
    elif choice == 2:
        value = int(input("Enter the value to delete: "))
        head = delete_value(head, value)
    elif choice == 3:
        value = int(input("Enter the value to search: "))
        search_value(head, value)
    elif choice == 4:
        find_min(head)
    elif choice == 5:
        find_max(head)
    elif choice == 6:
        display_list(head)
    elif choice == 7:
        print("Exiting")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
