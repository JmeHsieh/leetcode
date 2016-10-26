# https://leetcode.com/problems/reverse-string


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for c in xrange(len(s) - 1, -1, -1):
            result.append(s[c])
        return ''.join(result)
