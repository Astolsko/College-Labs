

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            print("Dequeued:", temp.data)

    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    def size(self):
        current = self.front
        count = 0
        while current is not None:
            count += 1
            current = current.next
        print("Queue size:", count)

    def display(self):
        current = self.front
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

queue = Queue()

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Size")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter the data to enqueue: ")
        queue.enqueue(data)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.peek()
    elif choice == 4:
        queue.size()
    elif choice == 5:
        queue.display()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
