#QUEUE IMPLEMENTATION
#Follows FIFO [FIRST IN FIRST OUT] Rule
queue = []
def push(queue, element):
    queue.append(element)
    print(queue)
def remove(queue):
    if not queue:
        print("Underflow.")
    else:
        element = queue.pop(0)
        print("Element", element, "has been removed.")
def is_empty(queue):
    if not queue:
        print("Queue is empty.")
    else:
        print("Queue is not empty.")
def display_queue(queue):
    if not queue:
        print("Queue is empty.")
    else:
        print("Queue:", queue)
def display_front(queue):
    if not queue:
        print("Queue is empty.")
    else:
        print("Front of the Queue:", queue[0])
def main():
    while True:
        print("1. Push")
        print("2. Remove")
        print("3. Check if Queue is Empty")
        print("4. Display Queue")
        print("5. Display Front of the Queue")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            element = input("Enter the element to push: ")
            push(queue, element)
        elif choice == '2':
            remove(queue)
        elif choice == '3':
            is_empty(queue)
        elif choice == '4':
            display_queue(queue)
        elif choice == '5':
            display_front(queue)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
main()

