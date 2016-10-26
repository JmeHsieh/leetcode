# https://leetcode.com/problems/balanced-binary-tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs_check(node):
            left_height, right_height = 0, 0
            if node is None:
                return (0, True)
            left_height, left_balanced = dfs_check(node.left)
            if not left_balanced:
                return (0, False)
            right_height, right_balanced = dfs_check(node.right)
            if not right_balanced:
                return (0, False)
            return (max(left_height, right_height) + 1, abs(left_height - right_height) <= 1)

        height, balanced = dfs_check(root)
        return balanced
