// https://leetcode.com/problems/happy-number

class Solution {
    func isHappy(n: Int) -> Bool {
        guard n >= 1 else { return false }

        // cycle: 4, 16, 37, 58, 89, 145, 42, 20, 4, ...
        var x = n
        while x != 1 {
            x = String(x).characters.map { Int(pow(Double(String($0))!, 2)) }.reduce(0, combine: +)
            if x == 4 { return false }
        }
        return true
    }
}
