# https://leetcode.com/problems/count-and-say


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        # [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...]

        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s

        # Solution - 3
        #
        # s = '1'
        # for _ in range(n-1):
        #     s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
        # return s

        # Solution - 2
        #
        # if n <= 1:
        #     return '1'
        # if n == 2:
        #     return '11'
        #
        # result = ""
        # counter = 1
        # s = self.countAndSay(n-1)
        # for i in range(len(s)-1):
        #     if s[i] == s[i+1]:
        #         counter += 1
        #     else:
        #         result += "%d%s" % (counter, s[i])
        #         counter = 1
        # result += "%d%s" % (counter, s[-1])
        # return result

        # Solution - 1
        #
        # result = ""
        # count = 1
        # r = x % 10
        # x = x // 10
        # while r != 0:
        #     next = x % 10
        #     if next == r:
        #         count += 1
        #         x = x // 10
        #     else:
        #         result = "%d%d" % (count, r) + result
        #         count = 1
        #         r = next
        #         x = x // 10
        # return result
