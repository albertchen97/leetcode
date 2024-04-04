#!/usr/bin/env python

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

def input_binary_tree():
    input_values = input().split()
    index = 0
    num_nodes = int(input_values[index])
    index += 1
    if (num_nodes == 0):
        return None
        
    nodes = []
    current_parent_index = 0
    
    root = TreeNode(int(input_values[index]))
    index += 1
    nodes.append(root)
    
    for i in range(1, num_nodes, 2):
        left_val = int(input_values[index])
        index += 1
        if (left_val != -1):
            left = TreeNode(left_val)
            nodes.append(left)
            nodes[current_parent_index].left = left
        
        right_val = int(input_values[index])
        index += 1
        if (right_val != -1):
            right = TreeNode(right_val)
            nodes.append(right)
            nodes[current_parent_index].right = right
        
        current_parent_index += 1
        
    return root

def description(root):
    if root is None:
        return " "

    queue = []

    output = str(root.val)
    queue.append(root)
    cursor = 0

    while cursor < len(queue):
        node = queue[cursor]
        cursor += 1

        if node.left is not None:
            output += " " + str(node.left.val)
            queue.append(node.left)

        if node.right is not None:
            output += " " + str(node.right.val)
            queue.append(node.right)

    return output

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None
"""
# Input: root of a binary tree (TreeNode)
# Output: sum of all left leaves (int)
def sumOfLeftLeaves(root: TreeNode, isLeftChild = False) -> int :
    """
    Write your code here
    :type root: TreeNode
    :rtype: int
    """
    # Left Leaf: The leaf that is the left child of another node.
    # Leaf: A leaf with no children.
    
    isLeaf = not root.left and not root.right
    isLeftLeaf = isLeaf and isLeftChild
    
    if isLeftLeaf:
        return root.val
    
    if not root.left:
        leftSum = 0
    else:
        leftSum = sumOfLeftLeaves(root.left, True)

    if not root.right:
        rightSum = 0
    else:
        rightSum = sumOfLeftLeaves(root.right, False)
    
    return leftSum + rightSum

root = input_binary_tree()
result = sumOfLeftLeaves(root)
print(result)
