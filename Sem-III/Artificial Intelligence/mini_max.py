import math

class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []

def minimax(node, curr_depth, maximizing_player):
    if curr_depth == 0 or not node.children:
        return node.val

    if maximizing_player:
        best_val = float("-inf")
        for child in node.children:
            val = minimax(child, curr_depth - 1, False)
            best_val = max(best_val, val)
        return best_val
    else:
        best_val = float("inf")
        for child in node.children:
            val = minimax(child, curr_depth - 1, True)
            best_val = min(best_val, val)
        return best_val

def construct_tree(score):
    def build_tree(depth, index, max_depth):
        if depth == max_depth:
            return Node(val=score[index])
        node = Node()
        node.children.append(build_tree(depth + 1, index * 2, max_depth))
        node.children.append(build_tree(depth + 1, index * 2 + 1, max_depth))
        return node

    max_depth = int(math.log2(len(score)))
    return build_tree(0, 0, max_depth)

def print_tree(node, depth=0):
    if not node:
        return
    print("  " * depth + f"Node(val={node.val})")
    for child in node.children:
        print_tree(child, depth + 1)

score = [3, 5, 2, 9, 12, 5, 23, 23]
# score = [10,5,7,11,12,8,9,8,5,12,11,12,9,8,7,10]
root = construct_tree(score)
# print_tree(root)
length = math.log(len(score),2)
val = minimax(root, length, True)
print(f"The value is: {val}")
