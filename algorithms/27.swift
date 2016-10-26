// https://leetcode.com/problems/remove-element

class Solution {
    func removeElement(inout nums: [Int], _ val: Int) -> Int {
        var i = 0
        while i < nums.count {
            if nums[i] == val { nums.removeAtIndex(i) }
            else { i += 1 }
        }
        return nums.count
    }
}
