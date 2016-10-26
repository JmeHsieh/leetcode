// https://leetcode.com/problems/binary-tree-level-order-traversal

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
    func levelOrder(root: TreeNode?) -> [[Int]] {
        var result = [[Int]]()
        func dfs_(node: TreeNode?, _ level: Int) {
            guard let n = node else { return }
            if result.count < level+1 { result.append([]) }
            result[level].append(n.val)
            dfs_(n.left, level+1)
            dfs_(n.right, level+1)
        }
        dfs_(root, 0)
        return result
    }
}
