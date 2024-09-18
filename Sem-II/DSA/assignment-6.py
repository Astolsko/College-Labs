# performing insertion deletion searching max min operation on unsorted linked lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class UnsortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

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
        max_val = float('-inf')
        while curr:
            max_val = max(max_val, curr.val)
            curr = curr.next
        return max_val
    def find_min(self):
        if not self.head:
            return None
        curr = self.head
        min_val = float('inf')
        while curr:
            min_val = min(min_val, curr.val)
            curr = curr.next
        return min_val
    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
if __name__ == "__main__":
    unsorted_ll = UnsortedLinkedList()
    while True:
        print("\nOperations on Unsorted Linked List:")
        print("1. Display Linked List")
        print("2. Insert Element")
        print("3. Delete Element")
        print("4. Search Element")
        print("5. Find Minimum")
        print("6. Find Maximum")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            unsorted_ll.display()
        elif choice == "2":
            val = int(input("Enter element to insert: "))
            unsorted_ll.insert(val)
            print("Element", val, "inserted into the unsorted linked list.")
        elif choice == "3":
            val = int(input("Enter element to delete: "))
            unsorted_ll.delete(val)
            print("Element", val, "deleted from the unsorted linked list.")
        elif choice == "4":
            val = int(input("Enter element to search: "))
            if unsorted_ll.search(val):
                print("Element", val, "found in the unsorted linked list.")
            else:
                print("Element", val, "not found in the unsorted linked list.")
        elif choice == "5":
            min_val = unsorted_ll.find_min()
            if min_val is not None:
                print("Minimum element in the unsorted linked list:", min_val)
            else:
                print("Unsorted linked list is empty.")
        elif choice == "6":
            max_val = unsorted_ll.find_max()
            if max_val is not None:
                print("Maximum element in the unsorted linked list:", max_val)
            else:
                print("Unsorted linked list is empty.")
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
