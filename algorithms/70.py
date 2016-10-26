# https://leetcode.com/problems/climbing-stairs


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # list all possible (x, y) such that: x + 2y = n
        # ex: n = 11, (x, y) = (11, 0), (9, 1), (7, 2), (5, 3), (3, 4), (1, 5)
        p = 0
        for i in range(int(math.floor(n / 2)) + 1):
            y = i
            x = n - 2 * i
            p += (math.factorial(x + y) / (math.factorial(x) * math.factorial(y)))

        return p
