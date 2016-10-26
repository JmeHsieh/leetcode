// https://leetcode.com/problems/ugly-number

class Solution {
    func isUgly(num: Int) -> Bool {
        guard num > 0 else { return false }
        var n = num
        while n % 5 == 0 { n /= 5 }
        while n % 3 == 0 { n /= 3 }
        while n % 2 == 0 { n /= 2 }
        return n==1
    }
}
