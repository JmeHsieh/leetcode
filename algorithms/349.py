# https://leetcode.com/problems/intersection-of-two-arrays


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        if nums1 == [] or nums2 == []:
            return []

        i, j, c, o, result = 0, 0, [], [], []
        nums1.sort()
        nums2.sort()
        if nums1[0] < nums2[0]:
            (c, o) = (nums1, nums2)
        else:
            (c, o) = (nums2, nums1)

        while i < len(c):
            if c[i] < o[j]:
                i += 1
                continue
            elif c[i] == o[j]:
                if result == [] or result[-1] != c[i]:
                    result.append(c[i])
            elif j < len(o) - 1:
                (c, o) = (o, c)
                (i, j) = (j, i)
            i += 1

        return result
