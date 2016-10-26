// https://leetcode.com/problems/single-number

class Solution {
    func singleNumber(nums: [Int]) -> Int {
        return nums.reduce(0, combine: (^))
    }
}
