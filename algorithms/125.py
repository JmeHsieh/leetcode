# https://leetcode.com/problems/valid-palindrome


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Solution - 2
        # Just Golfing
        s = [e for e in s.lower() if e.isalnum()]
        return s == s[::-1]

        # Solution - 1
        #
        # s = re.sub('[^a-z0-9]', '', s.lower())
        # len_s = len(s)
        # if len_s <= 1:
        #     return True

        # center = (len_s-1) // 2
        # if len_s % 2 == 0:
        #     return s[:center+1] == s[center+1:][::-1]
        # else:
        #     return s[:center] == s[center+1:][::-1]
