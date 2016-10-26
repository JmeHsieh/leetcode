# https://leetcode.com/problems/min-stack


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        self.m = sys.maxsize

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x < self.m:
            self.m = x
        self.q.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.q.pop()

        # update min
        self.m = min(self.q) if len(self.q) > 0 else sys.maxsize

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1] if len(self.q) > 0 else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.m


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
