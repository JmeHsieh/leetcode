# https://leetcode.com/problems/happy-number


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n < 1:
            return False

        # cycle: 4, 16, 37, 58, 89, 145, 42, 20, 4, ...
        while n != 1:
            n = sum(map(lambda x: int(x)**2, list(str(n))))
            if n == 4:
                return False
        return True
