# https://leetcode.com/problems/symmetric-tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def copy_rotate(node):
            if node is None:
                return None

            root = TreeNode(node.val)
            left, right = None, None
            if node.left is not None:
                left = copy_rotate(node.left)
            if node.right is not None:
                right = copy_rotate(node.right)
            root.left, root.right = right, left
            return root

        def same_tree(tree1, tree2):
            if tree1 is not None and tree2 is not None:
                if (tree1.val != tree2.val) or (not same_tree(tree1.left, tree2.left)) or (not same_tree(tree1.right, tree2.right)):
                    return False
            elif (tree1 is not None and tree2 is None) or (tree1 is None and tree2 is not None):
                return False
            return True

        return same_tree(root, copy_rotate(root))
