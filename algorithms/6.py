# https://leetcode.com/problems/zigzag-conversion


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows:
            return s
        elif numRows == 1:
            return s

        cycle = 2 * numRows - 2
        result = [''] * numRows
        result[0] = s[0::cycle]
        result[numRows - 1] = s[numRows - 1::cycle]
        for i in range(1, numRows - 1):
            j = i
            dynamic_cycle = cycle - 2 * i
            while j < len(s):
                result[i] += s[j]
                j += dynamic_cycle
                dynamic_cycle = abs(dynamic_cycle - cycle)

        return reduce(lambda a, b: a + b, result)
