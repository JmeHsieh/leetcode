// https://leetcode.com/problems/two-sum/

class Solution {
    func twoSum(nums: [Int], _ target: Int) -> [Int] {
        // lookup + build map along the way
        var map = [Int: Int]()
        for i1 in 0..<nums.count {
            if let i2 = map[target - nums[i1]] {
                return [i1, i2]
            } else {
                map[nums[i1]] = i1
            }
        }
        return []
    }
}
