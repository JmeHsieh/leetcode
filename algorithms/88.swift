// https://leetcode.com/problems/merge-sorted-array

class Solution {
    func merge(inout nums1: [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
        if m == 0 { return nums1 = nums2 }
        if n == 0 { return }

        // move nums1 all the way right
        for i in (nums1.count-1).stride(to: nums1.count-1-m, by: -1) {
            nums1[i] = nums1[i-(nums1.count-m)]
        }

        var i = 0
        var n1 = nums1.count-m      // index for nums1
        var n2 = 0                  // index for nums2
        while n1 < (m+n) && n2 < n {
            if nums1[n1] <= nums2[n2] {
                nums1[i] = nums1[n1]
                n1 += 1
            } else {
                nums1[i] = nums2[n2]
                n2 += 1
            }
            i += 1
        }

        // if there is any nums2 left
        if n2 < n { nums1[m+n2..<m+n] = nums2[n2..<n] }
    }
}
