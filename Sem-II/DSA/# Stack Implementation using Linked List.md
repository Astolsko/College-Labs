 # Stack Implementation using Linked List in Python

This code implements a stack data structure using a linked list in Python. A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle, meaning the last element added to the stack is the first one to be removed.

## Understanding the Code

### 1. Node Class:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

- The `Node` class represents each element in the linked list.
- Each node has two attributes: `data` to store the value and `next` to point to the next node in the list.

### 2. Stack Class:

```python
class Stack:
    def __init__(self):
        self.head = None  # Initialize an empty stack
        self.size = 0     # Keep track of the number of elements in the stack
```

- The `Stack` class represents the stack data structure.
- It has two attributes: `head` to point to the top of the stack and `size` to keep track of the number of elements in the stack.

### 3. Stack Operations:

- **`is_empty`**: Checks if the stack is empty.

```python
    def is_empty(self):
        return self.size == 0  # Check if the stack is empty
```

- **`push`**: Adds an element to the top of the stack.

```python
    def push(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:   # If the stack is empty, set the new node as the head
            self.head = new_node
        else:
            new_node.next = self.head  # If the stack is not empty, set the new node as the new head and link it to the previous head
            self.head = new_node
        self.size += 1  # Increment size of the stack
```

- **`pop`**: Removes and returns the element at the top of the stack.

```python
    def pop(self):
        if self.is_empty():
            print("Stack is empty")  
            return None
        