// https://leetcode.com/problems/palindrome-linked-list

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
    func isPalindrome(head: ListNode?) -> Bool {
        if head == nil || head?.next == nil { return true }

        // get length
        var length = 0
        var current = head
        while current != nil {
            length += 1
            current = current?.next
        }

        current = head
        var previous: ListNode? = nil
        var next: ListNode? = current?.next

        // reverse first half
        for _ in 0..<Int(ceil(Double(length)/2.0)) {
            current?.next = previous
            previous = current
            current = next
            next = next?.next
        }

        // move l1 one step left if length is odd
        var l1 = previous
        var l2 = current
        if length % 2 == 1 { l1 = l1?.next }

        // compare first-half and last-half
        while l1 != nil && l2 != nil {
            if l1!.val != l2!.val { return false }
            l1 = l1?.next
            l2 = l2?.next
        }

        return true
    }
}
