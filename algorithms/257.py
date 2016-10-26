# https://leetcode.com/problems/binary-tree-paths


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):

        result = []

        def dfs(node, currentString, result):
            if node is None:
                return
            currentString += "%s->" % str(node.val)
            if node.left is None and node.right is None:
                result.append(currentString[:-2])
            dfs(node.left, currentString, result)
            dfs(node.right, currentString, result)

        dfs(root, "", result)
        return result
