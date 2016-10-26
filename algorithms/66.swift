// https://leetcode.com/problems/plus-one

class Solution {
    func plusOne(digits: [Int]) -> [Int] {
        var ds = digits
        for i in (ds.count-1).stride(to: -1, by: -1) {
            if ds[i] < 9 {
                ds[i] += 1
                return ds
            }
            ds[i] = 0
        }
        ds.insert(1, atIndex: 0)
        return ds
    }
}
