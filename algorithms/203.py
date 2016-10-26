# https://leetcode.com/problems/remove-linked-list-elements


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None

        current = head
        next = head.next
        while next is not None:
            if next.val == val:
                current.next = next.next
            else:
                current = next
            next = next.next

        return head if head.val != val else head.next
