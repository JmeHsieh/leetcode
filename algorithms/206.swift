// https://leetcode.com/problems/reverse-linked-list

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
    func reverseList(head: ListNode?) -> ListNode? {
        var h = head
        var newHead: ListNode? = nil
        while h != nil {
            let next = h!.next
            h!.next = newHead
            newHead = h
            h = next
        }
        return newHead
    }
}
