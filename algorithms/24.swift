// https://leetcode.com/problems/swap-nodes-in-pairs

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func swapPairs(head: ListNode?) -> ListNode? {
        var c = head
        while c != nil && c!.next != nil {
            let t = c!.val
            c!.val = c!.next!.val
            c!.next!.val = t
            c = c!.next!.next
        }
        return head
    }
}
