# https://leetcode.com/problems/remove-duplicates-from-sorted-array


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # try not to remove the duplicate elements
        dpcount = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dpcount += 1
            else:
                nums[i - dpcount] = nums[i]
        return len(nums) - dpcount
