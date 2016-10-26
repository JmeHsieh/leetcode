// https://leetcode.com/problems/power-of-four

class Solution {
    func isPowerOfFour(num: Int) -> Bool {
        var n = num

        while (n >= 4 && n % 4 == 0) {
            n /= 4
        }
        return (n==1)
    }
}
