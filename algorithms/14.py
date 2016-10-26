# https://leetcode.com/problems/longest-common-prefix


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""

        minStrLength = min(map(len, strs))
        for i in range(minStrLength):
            if len(set(map(lambda s: s[i], strs))) != 1:
                return strs[0][:i]
        return strs[0][:minStrLength]
