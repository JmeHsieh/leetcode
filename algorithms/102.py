# https://leetcode.com/problems/binary-tree-level-order-traversal


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result = []
        queue = []
        if root is not None:
            queue.append((0, root))

        while len(queue):
            level, node = queue.pop(0)
            if node.left is not None:
                queue.append((level + 1, node.left))
            if node.right is not None:
                queue.append((level + 1, node.right))
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
        return result
