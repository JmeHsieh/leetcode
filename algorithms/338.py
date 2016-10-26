# https://leetcode.com/problems/counting-bits


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        result = [0]
        while len(result) < num + 1:
            result += list(map(lambda x: x + 1, result))
        return result[:num + 1]
