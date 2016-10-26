# https://leetcode.com/problems/number-of-1-bits


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        while n > 0:
            s += n & 1
            n = n >> 1
        return s
