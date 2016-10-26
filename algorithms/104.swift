// https://leetcode.com/problems/maximum-depth-of-binary-tree

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }å
 */

class Solution {
    func maxDepth(root: TreeNode?) -> Int {
        if root == nil {
            return 0
        } else if root?.left == nil && root?.right == nil {
            return 1
        } else if root?.left == nil {
            return 1 + maxDepth(root?.right)
        } else if root?.right == nil {
            return 1 + maxDepth(root?.left)
        } else {
            return 1 + max(maxDepth(root?.left), maxDepth(root?.right))
        }
    }
}
