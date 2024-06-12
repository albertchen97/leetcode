# https://leetcode.com/problems/linked-list-cycle/description/
# difficulty: easy (humiliating)
# time: 4 mins (garbage)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # input: node head
        # output: boolean (has cycle or not)
        # two pointers, fast and slow
        if not head:
            return False
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False



