class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, value):
        if self.head is None:
            print("Doubly linked list is empty.")
            return

        if self.head.data == value:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            print(f"Deleted {value} from the doubly linked list.")
            return

        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                print(f"Deleted {value} from the doubly linked list.")
                return
            current = current.next
        print(f"{value} not found in the doubly linked list.")

    def search(self, value):
        if self.head is None:
            print("Doubly linked list is empty.")
            return

        current = self.head
        index = 0
        while current:
            if current.data == value:
                print(f"{value} found at index {index}.")
                return
            current = current.next
            index += 1
        print(f"{value} not found in the doubly linked list.")

    def find_min(self):
        if self.head is None:
            print("Doubly linked list is empty.")
            return

        min_val = self.head.data
        current = self.head.next
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        print(f"The minimum value in the doubly linked list is {min_val}.")

    def find_max(self):
        if self.head is None:
            print("Doubly linked list is empty.")
            return

        max_val = self.head.data
        current = self.head.next
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        print(f"The maximum value in the doubly linked list is {max_val}.")

    def display_forward(self):
        if self.head is None:
            print("Doubly linked list is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        if self.head is None:
            print("Doubly linked list is empty.")
            return

        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
dll = DoublyLinkedList()
while True:
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Delete value")
    print("4. Search value")
    print("5. Find minimum value")
    print("6. Find maximum value")
    print("7. Display forward")
    print("8. Display backward")
    print("9. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter the value to insert at beginning: "))
        dll.insert_beginning(value)
    elif choice == 2:
        value = int(input("Enter the value to insert at end: "))
        dll.insert_end(value)
    elif choice == 3:
        value = int(input("Enter the value to delete: "))
        dll.delete(value)
    elif choice == 4:
        value = int(input("Enter the value to search: "))
        dll.search(value)
    elif choice == 5:
        dll.find_min()
    elif choice == 6:
        dll.find_max()
    elif choice == 7:
        print("Doubly linked list (forward):")
        dll.display_forward()
    elif choice == 8:
        print("Doubly linked list (backward):")
        dll.display_backward()
    elif choice == 9:
        print("Exiting")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
