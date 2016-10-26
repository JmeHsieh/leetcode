# https://leetcode.com/problems/contains-duplicate-ii


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # Solution - 3
        S = set()
        for i in range(len(nums)):
            if i > k:
                S.remove(nums[i - k - 1])
            if nums[i] in S:
                return True
            else:
                S.add(nums[i])
        return False

        # Solution - 2
        # for i in range(len(nums)):
        #     nums[i] = (nums[i], i)
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i][0] == nums[i-1][0] and abs(nums[i][1]-nums[i-1][1]) <= k:
        #         return True
        # return False

        # Solution - 1
        # M = {}
        # for i in range(len(nums)):
        #     d = nums[i]
        #     if d in M:
        #         if i-M[d][-1] <= k:
        #             return True
        #         else:
        #             M[d].append(i)
        #     else:
        #         M[d] = [i]

        # return False
