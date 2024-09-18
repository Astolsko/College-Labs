class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class UnbalancedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def delete(self, data):
        if self.root is None:
            return

        self.root = self._delete(data, self.root)

    def _delete(self, data, node):
        if node is None:
            return node

        if data < node.data:
            node.left = self._delete(data, node.left)
        elif data > node.data:
            node.right = self._delete(data, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            node.data = self._get_predecessor(node.left)
            node.left = self._delete(node.data, node.left)

        return node

    def _get_predecessor(self, node):
        if node.right is None:
            return node.data
        return self._get_predecessor(node.right)

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, node):
        if node is None:
            return False

        if data == node.data:
            return True

        if data < node.data:
            return self._search(data, node.left)

        return self._search(data, node.right)

    def max(self):
        if self.root is None:
            return None

        return self._max(self.root)

    def _max(self, node):
        if node.right is None:
            return node.data

        return self._max(node.right)

    def min(self):
        if self.root is None:
            return None

        return self._min(self.root)

    def _min(self, node):
        if node.left is None:
            return node.data

        return self._min(node.left)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0

        return max(self._height(node.left), self._height(node.right)) + 1

    def depth(self, data):
        if self.root is None:
            return None

        return self._depth(data, self.root)

    def _depth(self, data, node):
        if node is None:
            return None

        if data == node.data:
            return 0

        if data < node.data:
            return self._depth(data, node.left) + 1

        return self._depth(data, node.right) + 1

    def display(self):
        display_tree(self.root)

# Function to display the tree with proper indentation
def display_tree(root):
    def print_tree(node, space):
        if node is None:
            return
        space += 5
        print_tree(node.right, space)
        print(" " * space + str(node.data))
        print_tree(node.left, space)

    if root is None:
        print("Tree is empty.")
    else:
        print_tree(root, 0)

# Create an unbalanced binary tree
tree = UnbalancedBinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(20)

# Perform operations
while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Max")
    print("5. Min")
    print("6. Height")
    print("7. Depth")
    print("8. Display")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the data to insert: "))
        tree.insert(data)
    elif choice == 2:
        data = int(input("Enter the data to delete: "))
        tree.delete(data)
    elif choice == 3:
        data = int(input("Enter the data to search: "))
        if tree.search(data):
            print("Data found")
        else:
            print("Data not found")
    elif choice == 4:
        print("Maximum value:", tree.max())
    elif choice == 5:
        print("Minimum value:", tree.min())
    elif choice == 6:
        print("Height of the tree:", tree.height())
    elif choice == 7:
        data = int(input("Enter the data to find its depth: "))
        depth = tree.depth(data)
        if depth is None:
            print("Data not found")
        else:
            print("Depth of the data:", depth)
    elif choice == 8:
        tree.display()
    elif choice == 9:
        break
    else:
        print("Invalid choice")
