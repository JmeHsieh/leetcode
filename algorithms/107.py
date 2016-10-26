# https://leetcode.com/problems/binary-tree-level-order-traversal-ii


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # bfs
        result = []
        queue = [(0, root)]
        while len(queue) > 0:
            level, node = queue.pop(0)
            if node is None:
                continue
            if len(result) < level + 1:
                result.insert(0, [])
            result[-level - 1].append(node.val)
            queue.append((level + 1, node.left))
            queue.append((level + 1, node.right))
        return result
