# https://leetcode.com/problems/isomorphic-strings


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        M = {}
        S = set()
        for i in range(len(s)):
            if s[i] not in M:
                if t[i] in S:
                    return False
                M[s[i]] = t[i]
                S.add(t[i])
            elif M[s[i]] != t[i]:
                return False
        return True
