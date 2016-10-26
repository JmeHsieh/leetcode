# https://leetcode.com/problems/move-zeroes


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            if nums[i] != 0 and count != 0:
                nums[i - count] = nums[i]
                nums[i] = 0
