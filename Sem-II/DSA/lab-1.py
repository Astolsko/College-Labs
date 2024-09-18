#STACK IMPLEMENTATION
stack = []
def is_empty():
    return stack == []
def push(item, max_size):
    if len(stack) < max_size:
        stack.append(item)
        print(stack)
    else:
        print("Overflow: Stack is full")
def pop():
    if is_empty():
        print("Underflow: Stack is empty.")
    else:
        return stack.pop()
def peek():
    if not is_empty():
        return stack[-1]
def size():
    return len(stack)
def main():
    max_size = int(input("Enter the size of the stack: "))
    while True:
        print("1.Push")
        print("2.Pop")
        print("3.Peek")
        print("4.Size")
        print("5.isEmpty")
        print("6.Exit")
        option = int(input("Enter your choice: "))
        if option == 1:
            item = input("Enter the item to push: ")
            push(item, max_size)
        elif option == 2:
            print("Popped item:", pop())
        elif option == 3:
            print("Top item:", peek())
        elif option == 4:
            print("Size of the stack:", size())
        elif option == 5:
            if is_empty():
                print("The stack is empty.")
            else:
                print("The stack is not empty.")
        elif option == 6:
            break
        else:
            print("Invalid choice. Please try again.")
main()
