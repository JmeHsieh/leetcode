// https://leetcode.com/problems/same-tree

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
    func isSameTree(p: TreeNode?, _ q: TreeNode?) -> Bool {
        if let p = p, q = q {
            return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)
        } else if p == nil && q == nil {
            return true
        } else {
            return false
        }
    }
}
