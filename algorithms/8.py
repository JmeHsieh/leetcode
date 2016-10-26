# https://leetcode.com/problems/string-to-integer-atoi/


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        # extract [['sign', 'str']] using regex
        s = re.findall('(^[\+\-]{0,1})0*(\d+)', str.strip())
        if len(s) == 0:
            return 0
        positive = True if s[0][0] != '-' else False
        str = s[0][1]

        result = 0
        int_max = pow(2, 31) - 1
        int_min = -pow(2, 31)
        for i in range(len(str)):
            if ord(str[i]) < ord('0') or ord(str[i]) > ord('9'):
                break

            d = ord(str[i]) - ord('0')

            # check for overflow
            if int_max // 10 < result or (int_max // 10 == result and int_max % 10 < d):
                return int_max if positive else int_min

            result = result * 10 + d

        return result if positive else -result
