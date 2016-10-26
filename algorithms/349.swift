// https://leetcode.com/problems/intersection-of-two-arrays

class Solution {
    func intersection(nums1: [Int], _ nums2: [Int]) -> [Int] {
        let set1 = Set(nums1)
        let set2 = Set(nums2)
        return Array(set1.intersect(set2))
    }
}
