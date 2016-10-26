# https://leetcode.com/problems/rotate-array


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        # Solution - 2
        #
        def inplace_reverse(arr, start, length):
            if length <= 1:
                return
            i = start
            j = start + length - 1
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        inplace_reverse(nums, 0, len(nums))
        inplace_reverse(nums, 0, k)
        inplace_reverse(nums, k, len(nums) - k)

        # Solution - 1
        #
        # while k > 0:
        #     nums.insert(0, nums.pop())
        #     k -= 1
