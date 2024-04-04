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
from typing import List 

# Input: TreeNode
# Output: List[int]
# Time Complexity: O(N)
# Space Complexity: O(N) Worst Case; O(logN) Best/Average Case
def preorderTraversal(root: TreeNode) -> List[int]:
    """
    Write your code here
    :type root: TreeNode
    :rtype: List
    """
    
    result_list = []
    
    # Helper function
    def traverse(node: TreeNode) -> List[int]:
        if node:
            result_list.append(node.val)
            traverse(node.left)
            traverse(node.right)
    
    traverse(root)
    
    return result_list
    
    
    

root = input_binary_tree()
result = preorderTraversal(root)

for val in result:
  print(val)
