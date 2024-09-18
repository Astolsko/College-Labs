class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Pushed:", data)

    def pop(self):
        if self.head is None:
            print("Stack is empty")
        else:
            popped_node = self.head
            self.head = self.head.next
            print("Popped:", popped_node.data)

    def peek(self):
        if self.head is None:
            print("Stack is empty")
        else:
            print("Top element:", self.head.data)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        print("Size:", count)

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

stack = Stack()

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter the data to push: ")
        stack.push(data)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.size()
    elif choice == 5:
        stack.display()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
