# https://leetcode.com/problems/add-digits


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num if num < 10 else 1 + (num - 1) % 9
