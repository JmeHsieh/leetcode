# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        me = head
        pioneer = head

        # first, place pioneer n-steps forward
        while n > 0 and pioneer is not None:
            pioneer = pioneer.next
            n -= 1
        if pioneer is None:
            return head.next if n == 0 else head

        # march
        while pioneer.next is not None:
            pioneer = pioneer.next
            me = me.next
        me.next = me.next.next

        return head
