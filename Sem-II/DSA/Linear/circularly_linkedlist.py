class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete(self, value):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        if self.head.data == value:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            print(f"Deleted {value} from the circular linked list.")
            return

        prev = None
        current = self.head
        while current.next != self.head:
            if current.data == value:
                prev.next = current.next
                print(f"Deleted {value} from the circular linked list.")
                return
            prev = current
            current = current.next
        if current.data == value:
            prev.next = self.head
            print(f"Deleted {value} from the circular linked list.")
            return
        print(f"{value} not found in the circular linked list.")

    def search(self, value):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        current = self.head
        index = 0
        while True:
            if current.data == value:
                print(f"{value} found at index {index}.")
                return
            current = current.next
            index += 1
            if current == self.head:
                break
        print(f"{value} not found in the circular linked list.")

    def find_min(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        min_val = self.head.data
        current = self.head.next
        while True:
            if current.data < min_val:
                min_val = current.data
            current = current.next
            if current == self.head:
                break
        print(f"The minimum value in the circular linked list is {min_val}.")

    def find_max(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        max_val = self.head.data
        current = self.head.next
        while True:
            if current.data > max_val:
                max_val = current.data
            current = current.next
            if current == self.head:
                break
        print(f"The maximum value in the circular linked list is {max_val}.")

    def display(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

cll = CircularLinkedList()
while True:
    print("1. Insert at end")
    print("2. Delete value")
    print("3. Search value")
    print("4. Find minimum value")
    print("5. Find maximum value")
    print("6. Display list")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter the value to insert at end: "))
        cll.insert_end(value)
    elif choice == 2:
        value = int(input("Enter the value to delete: "))
        cll.delete(value)
    elif choice == 3:
        value = int(input("Enter the value to search: "))
        cll.search(value)
    elif choice == 4:
        cll.find_min()
    elif choice == 5:
        cll.find_max()
    elif choice == 6:
        print("Circular linked list:")
        cll.display()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
