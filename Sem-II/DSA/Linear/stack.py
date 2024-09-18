stack = []
def push(item):
    stack.append(item)
    print("pushed item: " + item)
def pop():
    if len(stack) > 0:
        popped = stack.pop()
        print("popped item: " + popped)
    else:
        print("Stack is empty")
def peek():
    if len(stack) > 0:
        print("Top item is: " + stack[len(stack)-1])
    else:
        print("Stack is empty")
def size():
    print("Size of the stack is: " + str(len(stack)))

def main():
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = input("Enter the item to push: ")
            push(item)
        elif choice == 2:
            pop()
        elif choice == 3:
            peek()
        elif choice == 4:
            size()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
