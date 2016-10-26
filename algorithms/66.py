# https://leetcode.com/problems/plus-one


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        i, adding = len(digits) - 1, 1
        while i >= 0 and adding != 0:
            d = digits[i] + adding
            (digits[i], adding) = (d, 0) if d < 10 else (0, 1)
            i -= 1

        if adding != 0:
            digits.insert(0, 1)
        return digits
