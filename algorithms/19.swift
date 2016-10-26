// https://leetcode.com/problems/remove-nth-node-from-end-of-list

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
    func removeNthFromEnd(head: ListNode?, _ n: Int) -> ListNode? {
        var n = n
        var me = head
        var pioneer = head

        // setup pioneer
        while n > 0 && pioneer != nil {
            pioneer = pioneer!.next
            n -= 1
        }
        if pioneer == nil {
            if n == 0 { return head!.next }
            else { return head }
        }

        // march
        while pioneer!.next != nil {
            pioneer = pioneer!.next
            me = me!.next
        }

        me!.next = me!.next!.next
        return head
    }
}
