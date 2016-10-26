# https://leetcode.com/problems/remove-duplicates-from-sorted-list


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        c = head
        while c.next:
            if c.val == c.next.val:
                c.next = c.next.next
            else:
                c = c.next
        return head
