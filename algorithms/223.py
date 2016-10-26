# https://leetcode.com/problems/rectangle-area


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        r_abcd = (C - A) * (D - B)
        r_efgh = (G - E) * (H - F)
        r_overlapped = 0
        if C > E and G > A and H > B and D > F:
            r_overlapped = min(C - E, G - A, C - A, G - E) * min(H - B, D - F, D - B, H - F)

        return r_abcd + r_efgh - r_overlapped
