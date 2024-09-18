

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def addFront(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def addRear(self, item):
        new_node = Node(item)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def removeFront(self):
        if self.isEmpty():
            print("Deque is empty")
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None

    def removeRear(self):
        if self.isEmpty():
            print("Deque is empty")
            return
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None

    def display(self):
        if self.isEmpty():
            print("Deque is empty")
            return
        current = self.front
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

deque = Deque()

while True:
    print("1. Add front")
    print("2. Add rear")
    print("3. Remove front")
    print("4. Remove rear")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the item to add at front: ")
        deque.addFront(item)
    elif choice == 2:
        item = input("Enter the item to add at rear: ")
        deque.addRear(item)
    elif choice == 3:
        deque.removeFront()
    elif choice == 4:
        deque.removeRear()
    elif choice == 5:
        deque.display()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
