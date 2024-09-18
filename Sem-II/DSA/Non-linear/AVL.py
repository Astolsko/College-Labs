

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))
        balance = self._getBalance(node)
        if balance > 1:
            if key < node.left.key:
                return self._rightRotate(node)
            else:
                node.left = self._leftRotate(node.left)
                return self._rightRotate(node)
        if balance < -1:
            if key > node.right.key:
                return self._leftRotate(node)
            else:
                node.right = self._rightRotate(node.right)
                return self._leftRotate(node)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            node.key = self._getPredecessor(node.left)
            node.left = self._delete(node.left, node.key)
        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))
        balance = self._getBalance(node)
        if balance > 1:
            if self._getBalance(node.left) < 0:
                node.left = self._leftRotate(node.left)
            return self._rightRotate(node)
        if balance < -1:
            if self._getBalance(node.right) > 0:
                node.right = self._rightRotate(node.right)
            return self._leftRotate(node)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, node):
        if node is None:
            return None
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, node):
        if node is None:
            return None
        current = node
        while current.right is not None:
            current = current.right
        return current

    def _getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def _getBalance(self, node):
        if node is None:
            return 0
        return self._getHeight(node.left) - self._getHeight(node.right)

    def _leftRotate(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))
        right_child.height = 1 + max(self._getHeight(right_child.left), self._getHeight(right_child.right))
        return right_child

    def _rightRotate(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        node.height = 1 + max(self._getHeight(node.left), self._getHeight(node.right))
        left_child.height = 1 + max(self._getHeight(left_child.left), self._getHeight(left_child.right))
        return left_child

    def _getPredecessor(self, node):
        current = node.left
        while current.right is not None:
            current = current.right
        return current.key

def print_menu():
    print("AVL Tree Operations:")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Find Minimum")
    print("5. Find Maximum")
    print("6. Display Tree")
    print("7. Exit")

def create_predefined_tree():
    avl = AVLTree()
    elements = [10, 5, 15, 3, 7, 12, 17, 2, 4, 6, 8, 11, 13, 16, 18, 1]
    for element in elements:
        avl.insert(element)
    return avl

def display_tree(root):
    def print_tree(node, space):
        if node is None:
            return
        space += 5
        print_tree(node.right, space)
        print(" " * space + str(node.key))
        print_tree(node.left, space)

    if root is None:
        print("Tree is empty.")
    else:
        print_tree(root, 0)

if __name__ == "__main__":
    avl = create_predefined_tree()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            key = int(input("Enter key to insert: "))
            avl.insert(key)
            print("Key", key, "inserted into the tree.")
        elif choice == "2":
            key = int(input("Enter key to delete: "))
            if avl.search(key):
                avl.delete(key)
                print("Key", key, "deleted from the tree.")
            else:
                print("Key", key, "not found in the tree.")
        elif choice == "3":
            key = int(input("Enter key to search: "))
            if avl.search(key):
                print("Key", key, "found in the tree.")
            else:
                print("Key", key, "not found in the tree.")
        elif choice == "4":
            min_key = avl.find_min()
            if min_key is not None:
                print("Minimum key in the tree:", min_key)
            else:
                print("Tree is empty.")
        elif choice == "5":
            max_key = avl.find_max()
            if max_key is not None:
                print("Maximum key in the tree:", max_key)
            else:
                print("Tree is empty.")
        elif choice == "6":
            print("Current Tree:")
            display_tree(avl.root)
            print()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
