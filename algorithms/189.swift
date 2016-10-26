// https://leetcode.com/problems/rotate-array

class Solution {
    func rotate(inout nums: [Int], _ k: Int) {
        func inplace_reverse(inout arr: [Int], _ start: Int, _ length: Int) {
            var i = start
            var j = i+length-1
            var tmp = 0
            while i < j {
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
                i += 1
                j -= 1
            }
        }

        let k = k % nums.count
        inplace_reverse(&nums, 0, nums.count)
        inplace_reverse(&nums, 0, k)
        inplace_reverse(&nums, k, nums.count-k)
    }
}
