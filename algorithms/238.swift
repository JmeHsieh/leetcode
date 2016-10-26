// https://leetcode.com/problems/product-of-array-except-self

class Solution {
    func productExceptSelf(nums: [Int]) -> [Int] {
        var result = [Int](count: nums.count, repeatedValue:1)
        var i = 0
        var j = nums.count-1
        var left = 1
        var right = 1

        while j > 0 {
            left *= nums[i]
            right *= nums[j]
            result[i+1] *= left
            result[j-1] *= right
            i += 1
            j -= 1
        }

        return result
    }
}
