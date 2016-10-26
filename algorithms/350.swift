// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution {
    func intersect(nums1: [Int], _ nums2: [Int]) -> [Int] {
        let n1 = nums1.sort()
        let n2 = nums2.sort()

        var result = [Int]()
        var i = 0
        var j = 0

        while i < n1.count && j < n2.count {
            if n1[i] < n2[j] {
                i += 1
            } else if (n1[i] == n2[j]) {
                result.append(n1[i])
                i += 1
                j += 1
            } else {
                j += 1
            }
        }
        return result
    }
}
