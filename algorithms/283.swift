// https://leetcode.com/problems/move-zeroes

class Solution {
    func moveZeroes(inout nums: [Int]) {
        var count = 0
        for i in 0..<nums.count {
            if nums[i] == 0 {
                count += 1
            }
            if nums[i] != 0 && count != 0 {
                nums[i-count] = nums[i]
                nums[i] = 0
            }
        }
    }
}
