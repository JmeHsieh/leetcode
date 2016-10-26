// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution {
    func removeDuplicates(inout nums: [Int]) -> Int {
        var j = 1
        while j < nums.count {
            if nums[j] == nums[j-1] { nums.removeAtIndex(j) }
            else { j += 1 }
        }
        return nums.count
    }
}
