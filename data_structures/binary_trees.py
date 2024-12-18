# trees -> root node, child nodes, parent nodes
# here a tree can be complete tree where there are some missing nodes in the end branch
# a perfect tree where every node is binarized and categorized
# time -> O(n) and space -> O(n)

# Depth First Search
# it prioritize depth where it travels deep down searching throughtyhe left side and slowly moves to the right side.
# treversal is of three types -> preorder, inorder, postorder
# built with stack and recursion
# empty stack with root node on the stack
# while the stack is not empty
# pop the stack -> processing and check if we have the right node, and left node we put this on the stack
# we move to the left and repeat the same step to compute the available nodes and then move to left node
# while moving to next layer the stack is poped
# at the end the stack becomes empty

# Breadth First Search
# it visits the tree level by level and it prioroize the breadth of the tree
# built with queve
# queve with initial node
# pop the initial node and process it
# if we have left,append to the queve abd process it in repeat

# Binary Search Tree
# any node in the left is smaller than all the node in the right this neglects many nodes which are unnecessary to process
# time complexity id O(logn)

class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left 
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

# creating a simple Tree
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print(A)

class TraversalAnalysis:
    def __init__(self, node) -> None:
        self.node = node

    # pre order traversal
    def preorder_Traversal(self, node):
        if not node:
            return
        
        print(node)
        self.preorder_Traversal(node.left)
        self.preorder_Traversal(node.right)

    # in order traversal
    def inorder_traversal(self, node):
        if not node:
            return False
        
        self.inorder_traversal(node.left)
        print(node)
        self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if not node:
            return False
        
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node)

    def preorder_traversal_iterative(node):
        stack = [node]

        while stack:
            node = stack.pop()

            print(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

analysis = TraversalAnalysis(A)

analysis.preorder_Traversal()
analysis.preorder_traversal_iterative()
analysis.inorder_traversal()
analysis.postorder_traversal()

# Breadth First Search
from collections import deque

def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

level_order(A)

# Depth First Search

def dfs_search(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    return dfs_search(node.left, target) or dfs_search(node.right, target)

dfs_search(A)

# Binary Search Tree

def bst(node, target):
    if not node:
        return False
    
    if target < node.val:
        return bst(node.left, target)
    
    else:
        return bst(node.right, target)