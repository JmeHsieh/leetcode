// https://leetcode.com/problems/path-sum

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
    func hasPathSum(root: TreeNode?, _ sum: Int) -> Bool {
        func dfs_(node: TreeNode?, _ currentSum: Int, _ targetSum: Int) -> Bool {
            guard let n = node else { return false }
            let c = currentSum + n.val
            if n.left == nil && n.right == nil { return c == targetSum }
            else { return dfs_(n.left, c, targetSum) || dfs_(n.right, c, targetSum) }
        }
        return dfs_(root, 0, sum)
    }
}
