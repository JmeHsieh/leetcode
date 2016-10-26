// https://leetcode.com/problems/power-of-two

class Solution {
    func isPowerOfTwo(n: Int) -> Bool {
        return n != 0 && (n & (n-1) == 0)
    }
}
