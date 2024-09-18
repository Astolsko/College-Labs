class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(node):
    if node:
        inorder(node.left)
        print(node.key, end=' ')
        inorder(node.right)

def preorder(node):
    if node:
        print(node.key, end=' ')
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.key, end=' ')

def bfs(root):
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.key, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Binary Tree:")
    print("    1")
    print("   / \\")
    print("  2   3")
    print(" / \\ / \\")
    print("4  5 6  7")
    print()

    while True:
        print("\nChoose the traversal method:")
        print("1. Inorder Traversal")
        print("2. Preorder Traversal")
        print("3. Postorder Traversal")
        print("4. Breadth First Search (BFS)")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            print("Inorder Traversal:", end=' ')
            inorder(root)
        elif choice == '2':
            print("Preorder Traversal:", end=' ')
            preorder(root)
        elif choice == '3':
            print("Postorder Traversal:", end=' ')
            postorder(root)
        elif choice == '4':
            print("BFS Traversal:", end=' ')
            bfs(root)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice")
main()
