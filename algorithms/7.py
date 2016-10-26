# https://leetcode.com/problems/reverse-integer/


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        n = abs(x)
        while n > 0:
            r = 10 * r + n % 10
            n //= 10

        if r > pow(2, 31) - 1:
            return 0
        else:
            return r if x >= 0 else -r
