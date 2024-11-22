import math
class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []

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

def print_tree(Node, depth=0):
    if not Node:
        return
    print("  " * depth + f"Node(val={Node.val})")
    for child in Node.children:
        print_tree(child, depth + 1)


def abprune(Node, depth, alpha, beta, maximizingPlayer):
	# base case
    if depth == 0 or len(Node.children) == 0:
        return Node.val
    if maximizingPlayer:
        for child in Node.children:
            alpha = max(alpha, abprune(child, depth-1,alpha,beta,False))
            if alpha >= beta:
                print(f"Depth: {depth}, Alpha: {alpha}, Beta: {beta}, Maximizing: {maximizingPlayer}")
                break
        return alpha
    
    else:
        for child in Node.children:
            beta = min(beta, abprune(child,depth-1,alpha,beta,True))
            if alpha >= beta:
                print(f"Depth: {depth}, Alpha: {alpha}, Beta: {beta}, Maximizing: {maximizingPlayer}")
                break
        return beta

values=[10,5,7,11,12,8,9,8,5,12,11,12,9,8,7,10]
tgt_d=int(math.log(len(values),2))
root = construct_tree(values)
alpha = float("-inf")
beta = float("inf")
print(f"The optimal Value is : {abprune(root,tgt_d,alpha,beta,True)}")

