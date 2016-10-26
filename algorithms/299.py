# https://leetcode.com/problems/bulls-and-cows


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g = list(secret), list(guess)
        A, B = 0, 0

        i = 0
        while i < len(s):
            if g[i] == s[i]:
                A += 1
                del s[i]
                del g[i]
            else:
                i += 1
        i = 0
        while i < len(s):
            if g[i] in s:
                B += 1
                s.remove(g[i])
                del g[i]
            else:
                i += 1

        return "%dA%dB" % (A, B)
