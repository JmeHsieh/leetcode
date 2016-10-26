# https://leetcode.com/problems/word-pattern


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p = list(pattern)
        s = str.split(" ")
        if len(p) != len(s):
            return False

        x = list(zip(p, s))
        return len(set(p)) == len(set(x)) == len(set(s))
