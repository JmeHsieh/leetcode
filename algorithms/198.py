# https://leetcode.com/problems/house-robber


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_sum, odd_sum = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                even_sum = max(odd_sum, nums[i] + even_sum)
            else:
                odd_sum = max(even_sum, nums[i] + odd_sum)
        return max(even_sum, odd_sum)
