# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# from collections import deque
#
# # BFS
# # Time: O(N)
# # Space: Bounded by the maximum width of the tree O(2^N)
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#
#         queue = deque([])
#         level = []
#         result = []
#
#         queue.append(root)
#         prev_count = 1
#         curr_count = 0
#
#         while queue:
#             # Append all the children of the previous level
#             while prev_count > 0:
#                 if queue:
#                     node = queue.popleft()
#                     prev_count -= 1
#                     level.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                     curr_count += 1
#                 if node.right:
#                     queue.append(node.right)
#                     curr_count += 1
#             
#             # Get the number of nodes in the previous level before going to the next level
#             prev_count = curr_count
#             curr_count = 0
#             
#             # Append the current level list to the result list
#             result.append(level)
#             
#             # Empty the level list
#             level = []
#         
#         return result
class Node:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

def list_to_binary_tree(nums):
  if not nums: return None

  root = Node(nums.pop(0))
  queue = [root]

  while queue:
    node = queue.pop(0)

    if nums:
      left_val = nums.pop(0)
      if left_val != None:
        node.left = Node(left_val)
        queue.append(node.left)

    if nums:
      right_val = nums.pop(0)
      if right_val != None:
        node.right = Node(right_val)
        queue.append(node.right)

  return root

def level_order(root):
  # ret = []
  # if root:
  #   curr_level = [root]
  #   while curr_level:
  #     children = []
  #     next_level = []
  #     for node in curr_level:
  #       next_level.append(node.val)
  #       if node.left:
  #         children.append(node.left)
  #       if node.right:
  #         children.append(node.right)
  #     ret.append(next_level)
  #     curr_level = children if len(children) > 0 else None
  # return ret

  # Recursive Solution
  if not root: return

  if len(results) == curr_level:
      results.append([])

  results[curr_level] = 


def main():
  tests = [
    { 'input': None,                              'output': [] },
    { 'input': [1],                               'output': [[1]] },
    { 'input': [2, 1],                            'output': [[2], [1]] },
    { 'input': [2, None, 1],                      'output': [[2], [1]] },
    { 'input': [2, 1, 3],                         'output': [[2], [1, 3]] },
    # { 'input': [3, 2, None, 1],                   'output': [[3], [2], [1]] },
    # { 'input': [1, None, 2, None, 3],             'output': [[1], [2], [3]] },
    # { 'input': [3, 2, 4, None, None, 5, 6],       'output': [[3], [2, 4], [5, 6]] },
    # { 'input': [3, 5, 1, 4, 9, None, 2],          'output': [[3], [5, 1], [4, 9, 2]] },
    # { 'input': [3, 9, 20, None, None, 15, 7],     'output': [[3], [9, 20], [15, 7]] },
    # { 'input': [2, 1, 4, None, None, 9],          'output': [[2], [1, 4], [9]] },
    # { 'input': [2, 1, None, None, 9, 3, None, 6], 'output': [[2], [1], [9], [3], [6]] },
  ]

  for i in range(len(tests)):
    print('Test', i+1, 'Pass:',
      level_order(list_to_binary_tree(tests[i]['input'])) == tests[i]['output']
    )

main() 
