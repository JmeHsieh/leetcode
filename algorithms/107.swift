// https://leetcode.com/problems/binary-tree-level-order-traversal-ii

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
    func levelOrderBottom(root: TreeNode?) -> [[Int]] {
        // dfs
        func trace(root: TreeNode?, _ level: Int, inout _ result: [[Int]]) {
            guard let r = root else { return }
            if result.count < level+1 { result.insert([], atIndex: 0) }
            result[result.count-level-1].append(r.val)
            trace(r.left, level+1, &result)
            trace(r.right, level+1, &result)
        }
        var result = [[Int]]()
        trace(root, 0, &result)
        return result
    }
}
