# Find height of a binary tree which is not balanced in python
class Node():
    def __init__(self,value):
        self.value=value
        self.left = None
        self.right = None
'''
# Sample Binary Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
print(tree_height(root))'''

def binary_tree():
    root_value = int(input("Enter the value for the root node : "))
    root = Node(root_value)
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        left_value = input(f"Enter the value for the left child of {current_node.value} (or 'None' if no left child) : ")
        if left_value.lower() != 'none':
            left_child = Node(int(left_value))
            current_node.left = left_child
            queue.append(left_child)
        right_value = input(f"Enter the value for the right child of {current_node.value} (or 'None' if no right child) : ")
        if right_value.lower() != 'none':
            right_child = Node(int(right_value))
            current_node.right = right_child
            queue.append(right_child)
    return root
def tree_height(node):
    
    if node is None:
        return -1
    else:
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)
        return 1 + max(left_height, right_height)
root = binary_tree()
print(" Height of the binary tree : ",tree_height(root))
