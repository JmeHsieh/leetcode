# https://leetcode.com/problems/factorial-trailing-zeroes


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 1
        zs = 0
        while n / (pow(5, p)) >= 1:
            zs += math.floor(n / pow(5, p))
            p += 1
        return int(zs)
