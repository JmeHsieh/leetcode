// https://leetcode.com/problems/factorial-trailing-zeroes

class Solution {
    func trailingZeroes(n: Int) -> Int {
        var p = 1.0
        var zs = 0
        while Double(n)/pow(5.0, p) >= 1 {
            zs += Int(Double(n)/pow(5.0, p))
            p += 1.0
        }
        return zs
    }
}
