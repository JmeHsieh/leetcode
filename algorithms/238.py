# https://leetcode.com/problems/product-of-array-except-self


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_n = len(nums)
        result = [1] * len_n

        # left --> right
        prod = 1
        for i in range(1, len_n):
            prod *= nums[i - 1]
            result[i] *= prod

        # left <-- right
        prod = 1
        for i in range(len_n - 2, -1, -1):
            prod *= nums[i + 1]
            result[i] *= prod

        return result
