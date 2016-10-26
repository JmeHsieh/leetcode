# https://leetcode.com/problems/implement-stack-using-queues


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        for i in range(len(self.q) - 1):
            temp = self.q[0]        # Queue.peek
            del self.q[0]           # Queue.pop
            self.q.append(temp)     # Queue.push

    def pop(self):
        """
        :rtype: nothing
        """
        del self.q[0]

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0
