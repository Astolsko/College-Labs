 # Stack Implementation using Doubly Linked List in Python

This code implements a stack data structure using a doubly linked list in Python. A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle, meaning that the last element added to the stack is the first one to be removed.

## Understanding the Code

### 1. Node Class:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

- The `Node` class represents a node in the doubly linked list. Each node has three attributes:
  - `data`: Stores the data or value of the node.
  - `prev`: A reference to the previous node in the list.
  - `next`: A reference to the next node in the list.

### 2. Stack Class:

```python
class Stack:
    def __init__(self):
        self.head = None  # Initialize an empty stack
        self.size = 0     # Keep track of the number of elements in the stack
```

- The `Stack` class represents the stack data structure. It has two attributes:
  - `head`: A reference to the top of the stack (the last element added).
  - `size`: The number of elements currently in the stack.

### 3. Stack Operations:

The `Stack` class provides several methods to perform various operations on the stack:

- `is_empty()`: Checks if the stack is empty.

- `push(data)`: Adds a new element to the top of the stack.

- `pop()`: Removes and returns the element at the top of the stack.

- `peek()`: Returns the element at the top of the stack without removing it.

- `display()`: Prints the elements of the stack from top to bottom.

### 4. Menu-Driven Interface:

The code includes a menu-driven interface that allows users to interact with the stack and perform various operations. The `display_menu()` function displays the menu options, and the `stack_operations(stack)` function handles user input and performs the corresponding operations on the stack.

### 5. Main Function:

```python
if __name__ == "__main__":
    stack = Stack()
    stack_operations(stack)
