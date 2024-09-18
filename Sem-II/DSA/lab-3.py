#Implement stacks using singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None  # Initialize an empty stack
        self.size = 0     # Keep track of the number of elements in the stack

    def is_empty(self):
        return self.size == 0  # Check if the stack is empty

    def push(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:   # If the stack is empty, set the new node as the head
            self.head = new_node
        else:
            new_node.next = self.head  # If the stack is not empty, set the new node as the new head and link it to the previous head
            self.head = new_node
        self.size += 1  # Increment size of the stack

    def pop(self):
        if self.is_empty():
            print("Stack is empty")  
            return None
        else:
            data = self.head.data  # Get the data from the current head
            self.head = self.head.next   # Move the head to the next node
            self.size -= 1  # Decrement the size of the stack
            return data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")  
            return None
        else:
            return self.head.data  # Return the data from the current head

    def display(self):
        if self.is_empty():
            print("Stack is empty")  
        else:
            current = self.head
            print("Stack (top to bottom):", end=" ")
            while current:
                print(current.data, end=" ")
                current = current.next
            print()


# Function to display menu options
def display_menu():
    print("\nStack Menu:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

# Function to interact with the stack based on user input
def stack_operations(stack):
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter the element to push: ")
            stack.push(data)
        elif choice == "2":
            popped_element = stack.pop()
            if popped_element is not None:
                print("Popped element:", popped_element)
        elif choice == "3":
            top_element = stack.peek()
            if top_element is not None:
                print("Top element of the stack:", top_element)
        elif choice == "4":
            stack.display()
        elif choice == "5":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    stack = Stack()
    stack_operations(stack)

