// https://leetcode.com/problems/remove-duplicates-from-sorted-list

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
    func deleteDuplicates(head: ListNode?) -> ListNode? {
        var c = head
        while c?.next != nil {
            if c?.val == c?.next?.val {
                c?.next = c?.next?.next
            } else {
                c = c?.next
            }
        }
        return head
    }
}
