// https://leetcode.com/problems/house-robber

class Solution {
    func rob(nums: [Int]) -> Int {
        var prevNo = 0
        var prevYes = 0
        var temp = 0
        for i in 0..<nums.count {
            temp = prevNo
            prevNo = max(prevNo, prevYes)
            prevYes = nums[i]+temp
        }
        return max(prevNo, prevYes)
    }
}
