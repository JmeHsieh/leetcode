# https://leetcode.com/problems/compare-version-numbers


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        for i in range(max(len(v1), len(v2))):
            i1 = v1[i] if i < len(v1) else 0
            i2 = v2[i] if i < len(v2) else 0
            if i1 > i2:
                return 1
            elif i1 < i2:
                return -1

        return 0
