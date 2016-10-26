# https://leetcode.com/problems/reverse-vowels-of-a-string


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            li = l[i].lower()
            if li != 'a' and li != 'e' and li != 'i' and li != 'o' and li != 'u':
                i += 1
                continue
            lj = l[j].lower()
            if lj != 'a' and lj != 'e' and lj != 'i' and lj != 'o' and lj != 'u':
                j -= 1
                continue
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        return ''.join(str(x) for x in l)
