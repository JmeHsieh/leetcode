// https://leetcode.com/problems/symmetric-tree

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
 * }
 */

class Solution {
    func isSymmetric(root: TreeNode?) -> Bool {
        func symmetric_(left: TreeNode?, _ right: TreeNode?) -> Bool {
            guard let l = left, r = right else { return left == nil && right == nil }
            if l.val != r.val { return false }
            return symmetric_(l.left, r.right) && symmetric_(l.right, r.left)
        }
        return root == nil || symmetric_(root?.left, root?.right)
    }
}
