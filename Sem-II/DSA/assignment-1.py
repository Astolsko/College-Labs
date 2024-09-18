# 16 elements balanced binary search tree ,perform insertion deletion and search, finding min and max in BINARY SEARCH TREE
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        self.root = self._insert(self.root, key)
    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root
    def delete(self, key):
        self.root = self._delete(self.root, key)
    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)
        return root
    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
    def search(self, key):
        return self._search(self.root, key)
    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)
    def find_min(self):
        return self._find_min(self.root)
    def _find_min(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current.key
    def find_max(self):
        return self._find_max(self.root)
    def _find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current.key
def print_menu():
    print("Binary Search Tree Operations:")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Find Minimum")
    print("5. Find Maximum")
    print("6. Exit")
def create_predefined_tree():
    bst = BinarySearchTree()
    elements = [10, 5, 15, 3, 7, 12, 17, 2, 4, 6, 8, 11, 13, 16, 18, 1]
    for element in elements:
        bst.insert(element)
    return bst
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
    bst = create_predefined_tree()
    while True:
        print("Current Tree:")
        display_tree(bst.root)
        print()

        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            key = int(input("Enter key to insert: "))
            bst.insert(key)
            print("Key", key, "inserted into the tree.")
        elif choice == "2":
            key = int(input("Enter key to delete: "))
            if bst.search(key):
                bst.delete(key)
                print("Key", key, "deleted from the tree.")
            else:
                print("Key", key, "not found in the tree.")
        elif choice == "3":
            key = int(input("Enter key to search: "))
            if bst.search(key):
                print("Key", key, "found in the tree.")
            else:
                print("Key", key, "not found in the tree.")
        elif choice == "4":
            min_key = bst.find_min()
            if min_key is not None:
                print("Minimum key in the tree:", min_key)
            else:
                print("Tree is empty.")
        elif choice == "5":
            max_key = bst.find_max()
            if max_key is not None:
                print("Maximum key in the tree:", max_key)
            else:
                print("Tree is empty.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
