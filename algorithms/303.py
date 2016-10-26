# https://leetcode.com/problems/range-sum-query-immutable


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.acc = [0]
        for n in nums:
            self.acc.append(self.acc[-1] + n)

    def sumRange(self, i, j):
        """sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.acc[j + 1] - self.acc[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
