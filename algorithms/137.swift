// https://leetcode.com/problems/single-number-ii

class Solution {
    func singleNumber(nums: [Int]) -> Int {
        var b1 = 0
        var b0 = 0
        for n in nums {
            b0 = b0^n & ~b1
            b1 = b1^n & ~b0
        }
        return b0
    }
}
