# https://leetcode.com/problems/power-of-four


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num >= 4 and num % 4 == 0:
            num /= 4
        return num == 1
