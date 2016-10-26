// https://leetcode.com/problems/majority-element

class Solution {
    func majorityElement(nums: [Int]) -> Int {
        var major = nums.first!
        var count = 1
        for i in 1..<nums.count {
            if count == 0 {
                major = nums[i]
                count = 1
            } else if (nums[i] != major) {
                count -= 1
            } else {
                count += 1
            }
        }
        return major
    }
}
