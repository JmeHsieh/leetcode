# https://leetcode.com/problems/palindrome-number/


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False

        acc = 0
        while x / 10 >= acc:
            acc = acc * 10 + x % 10
            if acc == x:
                return True
            x = math.floor(x / 10)
        return x == acc
