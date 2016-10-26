// https://leetcode.com/problems/contains-duplicate-ii

class Solution {
    func containsNearbyDuplicate(nums: [Int], _ k: Int) -> Bool {
        var s = Set<Int>()
        for i in 0..<nums.count {
            if i > k { s.remove(nums[i-k-1]) }
            if s.contains(nums[i]) { return true }
            s.insert(nums[i])
        }
        return false
    }
}
