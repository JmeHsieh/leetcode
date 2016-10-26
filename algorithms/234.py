# https://leetcode.com/problems/palindrome-linked-list


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        # get list length
        length = 0
        current = head
        while current is not None:
            length += 1
            current = current.next

        # reverse first-half
        previous = None
        current = head
        next = head.next
        for _ in range((length + 1) / 2):
            current.next = previous
            previous = current
            current = next
            next = next.next

        # compare two sub-lists:
        l1 = previous
        l2 = current

        # if length is odd, move l1 one step to left
        if length % 2 == 1:
            l1 = l1.next

        # start comparing
        while l1 is not None and l2 is not None:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return True
