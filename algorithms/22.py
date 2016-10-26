# https://leetcode.com/problems/generate-parentheses


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        queue = [('', 0, n, n)]

        while len(queue) > 0:
            (s, w, lpq, rpq) = queue.pop(0)
            s += '('
            w += 1
            lpq -= 1
            if lpq == 0 or rpq == 0:
                s += ')' * rpq
                result.append(s)
            else:
                for r in range(rpq + 1):
                    if w - r >= 0:
                        queue.append((s + ')' * r, w - r, lpq, rpq - r))

        return result
