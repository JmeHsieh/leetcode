// https://leetcode.com/problems/reverse-integer/

class Solution {
    func reverse(x: Int) -> Int {
        var r = 0
        var n = abs(x)
        while n > 0 {
            r = 10*r + n%10
            if Double(r) > pow(2.0, 31.0)-1 { return 0 }
            n /= 10
        }

        return (x>=0) ? r : -r
    }
}
