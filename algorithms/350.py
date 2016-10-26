# https://leetcode.com/problems/intersection-of-two-arrays-ii


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        i, j, c, o, result = 0, 0, [], [], []
        nums1.sort()
        nums2.sort()
        c, o = nums1, nums2
        while i < len(c) and j < len(o):
            if c[i] < o[j]:
                i += 1
            elif c[i] == o[j]:
                result.append(c[i])
                i += 1
                j += 1
            else:
                j += 1
        return result
