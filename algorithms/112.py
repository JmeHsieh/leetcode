# https://leetcode.com/problems/path-sum


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def dfs_(node, currentSum, targetSum):
            if node is None:
                return False

            currentSum += node.val
            if node.left is None and node.right is None:
                return currentSum == targetSum
            return dfs_(node.left, currentSum, targetSum) or dfs_(node.right, currentSum, targetSum)

        return dfs_(root, 0, sum)
