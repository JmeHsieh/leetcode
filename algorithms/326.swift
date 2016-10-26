// https://leetcode.com/problems/power-of-three

class Solution {
    func isPowerOfThree(n: Int) -> Bool {
        var x = n
        if x < 1 {
            return false
        } else {
            while x % 3 == 0 {
                x = x / 3
            }
            return x == 1
        }
    }
}
