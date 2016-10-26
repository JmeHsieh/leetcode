# https://leetcode.com/problems/add-binary


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return '{:b}'.format(int(a, 2) + int(b, 2))
