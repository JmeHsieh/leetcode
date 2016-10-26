# https://leetcode.com/problems/intersection-of-two-linked-lists


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if headA is None or headB is None:
            return None

        def getLen(node):
            l = 0
            while node is not None:
                l += 1
                node = node.next
            return l

        pa, pb = headA, headB
        la, lb = getLen(headA), getLen(headB)
        while la > lb:
            pa = pa.next
            la -= 1
        while lb > la:
            pb = pb.next
            lb -= 1

        while pa is not pb:
            pa = pa.next
            pb = pb.next
        return pa

    # Solution-1
    #
    # def getIntersectionNode(self, headA, headB):
    #     """
    #     :type head1, head1: ListNode
    #     :rtype: ListNode
    #     """

    #     if headA == None or headB == None:
    #         return None

    #     # mark A
    #     temp = headA
    #     while temp != None:
    #         temp.val = -temp.val
    #         temp = temp.next

    #     # walk through B and check if any B is marked as A
    #     result = headB
    #     while result != None:
    #         if result.val < 0:
    #             break
    #         result = result.next

    #     # recover A
    #     temp = headA
    #     while temp != None:
    #         temp.val = -temp.val
    #         temp = temp.next

    #     return result
