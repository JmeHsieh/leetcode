// https://leetcode.com/problems/remove-linked-list-elements

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
    func removeElements(head: ListNode?, _ val: Int) -> ListNode? {
        guard let h = head else { return nil }

        var current = h
        var next = h.next
        while let n = next {
            if n.val == val {
                current.next = n.next
            } else {
                current = n
            }
            next = n.next
        }
        if h.val == val { return h.next }
        else { return h }
    }
}
