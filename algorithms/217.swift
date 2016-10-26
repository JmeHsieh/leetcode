// https://leetcode.com/problems/contains-duplicate

class Solution {
    func containsDuplicate(nums: [Int]) -> Bool {
        var n = nums
        n.sortInPlace()
        for i in 0..<max(n.count-1, 0) {
            if n[i] == n[i+1] { return true }
        }
        return false
    }
}
