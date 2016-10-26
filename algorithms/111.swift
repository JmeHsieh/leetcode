// https://leetcode.com/problems/minimum-depth-of-binary-tree

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
    func minDepth(root: TreeNode?) -> Int {
        func dfs(node: TreeNode?, _ count: Int) -> Int {
            guard let n = node else { return count }
            let count = count + 1

            if n.left != nil && n.right != nil {
                return min(dfs(n.left, count), dfs(n.right, count))
            }
            else {
                return max(dfs(n.left, count), dfs(n.right, count))
            }
        }
        return dfs(root, 0)
    }
}
