class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        new_node = [item, priority]
        for i in range(len(self.queue)):
            if priority < self.queue[i][1]:
                self.queue.insert(i, new_node)
                return
        self.queue.append(new_node)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
            return
        return self.queue.pop(0)[0]

    def display(self):
        for item in self.queue:
            print(f"{item[0]} ({item[1]})")

    def size(self):
        return len(self.queue)
queue = PriorityQueue()
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Size")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the item to enqueue: ")
        priority = int(input("Enter the priority: "))
        queue.enqueue(item, priority)
    elif choice == 2:
        print("Dequeued:", queue.dequeue())
    elif choice == 3:
        queue.display()
    elif choice == 4:
        print("Queue size:", queue.size())
    elif choice == 5:
        break
    else:
        print("Invalid choice")
