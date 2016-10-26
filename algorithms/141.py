# https://leetcode.com/problems/linked-list-cycle


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        c, n = head, head.next
        while c != n:
            if n is None or n.next is None:
                return False
            c = c.next
            n = n.next.next
        return True
