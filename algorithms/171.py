# https://leetcode.com/problems/excel-sheet-column-number


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        for i in range(len(s)):
            val = ord(s[i]) - 64
            r = r * 26 + val

        return r
