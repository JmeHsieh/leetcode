// https://leetcode.com/problems/palindrome-number/

class Solution {
    func isPalindrome(x: Int) -> Bool {
        if x < 0 || (x != 0 && x % 10 == 0) { return false }
        var a = x
        var b = 0
        while a > b {
            b = b*10 + a%10
            a /= 10
        }
        return b==a || (b/10)==a
    }
}
