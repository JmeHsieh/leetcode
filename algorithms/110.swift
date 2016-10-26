// https://leetcode.com/problems/balanced-binary-tree

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
    func isBalanced(root: TreeNode?) -> Bool {
        func dfsHeight(node: TreeNode?) -> Int {
            guard let n = node else { return 0 }

            let leftHeight = dfsHeight(n.left)
            if leftHeight == -1 { return -1 }

            let rightHeight = dfsHeight(n.right)
            if rightHeight == -1 { return -1 }

            if abs(leftHeight - rightHeight) > 1 { return -1 }
            return max(leftHeight, rightHeight) + 1
        }
        return dfsHeight(root) != -1
    }
}
