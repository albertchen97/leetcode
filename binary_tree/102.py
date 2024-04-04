# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# BFS
# Time: O(N)
# Space: Bounded by the maximum width of the tree O(2^N)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([])
        level = []
        result = []

        queue.append(root)
        prev_count = 1
        curr_count = 0

        while queue:
            # Append all the children of the previous level
            while prev_count > 0:
                if queue:
                    node = queue.popleft()
                    prev_count -= 1
                    level.append(node.val)
                if node.left:
                    queue.append(node.left)
                    curr_count += 1
                if node.right:
                    queue.append(node.right)
                    curr_count += 1
            
            # Get the number of nodes in the previous level before going to the next level
            prev_count = curr_count
            curr_count = 0
            
            # Append the current level list to the result list
            result.append(level)
            
            # Empty the level list
            level = []
        
        return result
