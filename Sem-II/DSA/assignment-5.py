# performing insertion deletion searching max min operation on sorted linked lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class SortedLinkedList:
    def __init__(self):
        self.head = None
    def insert(self, val):
        new_node = ListNode(val)
        if not self.head or val < self.head.val:
            new_node.next = self.head
            self.head = new_node
            return
        curr = self.head
        while curr.next and curr.next.val < val:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
    def delete(self, val):
        if not self.head:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        prev, curr = None, self.head
        while curr and curr.val != val:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
    def search(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False
    def find_max(self):
        if not self.head:
            return None
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.val
    def find_min(self):
        return self.head.val if self.head else None
    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
if __name__ == "__main__":
    sorted_ll = SortedLinkedList()
    while True:
        print("\nOperations on Sorted Linked List:")
        print("1. Display Linked List")
        print("2. Insert Element")
        print("3. Delete Element")
        print("4. Search Element")
        print("5. Find Minimum")
        print("6. Find Maximum")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            sorted_ll.display()
        elif choice == "2":
            val = int(input("Enter element to insert: "))
            sorted_ll.insert(val)
            print("Element", val, "inserted into the sorted linked list.")
        elif choice == "3":
            val = int(input("Enter element to delete: "))
            sorted_ll.delete(val)
            print("Element", val, "deleted from the sorted linked list.")
        elif choice == "4":
            val = int(input("Enter element to search: "))
            if sorted_ll.search(val):
                print("Element", val, "found in the sorted linked list.")
            else:
                print("Element", val, "not found in the sorted linked list.")
        elif choice == "5":
            min_val = sorted_ll.find_min()
            if min_val is not None:
                print("Minimum element in the sorted linked list:", min_val)
            else:
                print("Sorted linked list is empty.")
        elif choice == "6":
            max_val = sorted_ll.find_max()
            if max_val is not None:
                print("Maximum element in the sorted linked list:", max_val)
            else:
                print("Sorted linked list is empty.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

