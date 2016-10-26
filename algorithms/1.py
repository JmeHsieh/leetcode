# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i1 in range(len(nums)):
            diff = target - nums[i1]
            if diff in map:
                return [i1, map[diff]]
            else:
                map[nums[i1]] = i1
        return []
