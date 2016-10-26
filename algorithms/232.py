# https://leetcode.com/problems/implement-queue-using-stacks


class Queue(object):
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

    def pop(self):
        """
        :rtype: nothing
        """
        temp = []
        top = None

        # pop to temp
        while len(self.q):          # Stack.isEmpty
            top = self.q[-1]        # Stack.peek
            del self.q[-1]          # Stack.pop
            if len(self.q):         # Stack.isEmpty
                temp.append(top)

        # pop back to self.q
        while len(temp):            # Stack.isEmpty
            top = temp[-1]          # Stack.peek
            del temp[-1]            # Stack.pop
            self.q.append(top)      # Stack.push

    def peek(self):
        """
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0
