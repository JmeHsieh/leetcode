# https://leetcode.com/problems/implement-strstr


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # Try to use KMP algorithm

        def compute_lps(pattern):
            len_p = len(pattern)
            lps = [0] * len_p
            max_len = 0
            i = 1
            while i < len_p:
                if pattern[i] == pattern[max_len]:
                    max_len += 1
                    lps[i] = max_len
                else:
                    if max_len != 0:
                        max_len = lps[max_len - 1]
                        continue
                    else:
                        lps[i] = 0
                i += 1

            return lps

        def kmp_match(pattern, text):
            len_p = len(pattern)
            len_t = len(text)
            lps = compute_lps(pattern)
            result = []
            idx_p = 0
            idx_t = 0

            while idx_t < len_t:
                if pattern[idx_p] == text[idx_t]:
                    idx_p += 1
                    idx_t += 1

                if idx_p == len_p:
                    result.append(idx_t - idx_p)
                    idx_p = lps[idx_p - 1]
                elif idx_t < len_t and pattern[idx_p] != text[idx_t]:
                    if idx_p != 0:
                        idx_p = lps[idx_p - 1]
                    else:
                        idx_t += 1

            return result

        # main -
        if len(needle) == 0:
            return 0
        indexes = kmp_match(needle, haystack)
        return indexes[0] if len(indexes) > 0 else -1
