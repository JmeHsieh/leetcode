# https://leetcode.com/problems/valid-parentheses


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c not in dict:
                stack.append(c)
            elif len(stack) == 0 or dict[c] != stack.pop():
                return False
        return len(stack) == 0
