# difficulty: medium (walk in the park)
# time: 14 mins (shame)
https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # delete the node, meaning the value should not exist in the linked list, num of node should decrease by 1, all the nodes before and after the node should be in the same order; don't remove the node from the memory
        # use three pointers to keep track of the prev, curr, and next nodes
        curr = node
        prev = None
        curr_next = node.next

        # overwrite the node value with node.next value until the end
        while curr_next:
            curr.val = curr_next.val
            prev = curr
            curr = curr_next
            curr_next = curr_next.next
        
        # delete the last node
        prev.next = None

        # no return value, modify node in-place, no need to find the head node

        
