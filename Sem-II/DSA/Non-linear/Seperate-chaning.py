class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SeparateChainingHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash_function(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)
        self.size += 1

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def display(self):
        for index in range(self.capacity):
            print(f"Index {index}: ", end="")
            current = self.table[index]
            while current:
                print(f"({current.key}: {current.value})", end=" -> " if current.next else "")
                current = current.next
            print("None")

def main():
    hash_table = SeparateChainingHashTable()
    while True:
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == '1':
            key = input("Enter key to insert: ")
            value = input("Enter value to insert: ")
            hash_table.insert(key, value)
            print("Key-value pair inserted successfully.")
        elif choice == '2':
            key = input("Enter key to search: ")
            result = hash_table.search(key)
            if result:
                print(f"Value for key {key}:", result)
            else:
                print("Key not found in the hash table.")
        elif choice == '3':
            key = input("Enter key to delete: ")
            hash_table.delete(key)
            print("Key-value pair deleted successfully.")
        elif choice == '4':
            hash_table.display()
        elif choice == '5':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
main()
