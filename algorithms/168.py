# https://leetcode.com/problems/excel-sheet-column-title


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ord_A = ord('A')
        result = []
        while n > 0:
            n, r = divmod(n - 1, 26)
            result.insert(0, r)
        return ''.join(chr(x + ord_A) for x in result)
