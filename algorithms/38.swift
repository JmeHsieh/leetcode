// https://leetcode.com/problems/count-and-say

class Solution {
    func countAndSay(n: Int) -> String {
        // [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...]

        if n <= 1 { return "1" }
        if n == 2 { return "11" }

        var result = ""
        var count = 1
        let x = countAndSay(n-1)
        let xs = x.characters.map { String($0) }
        for i in 0..<xs.count-1 {
            if xs[i] == xs[i+1] {
                count += 1
            } else {
                result += "\(count)\(xs[i])"
                count = 1
            }
        }
        result += "\(count)\(xs[xs.count-1])"
        return result
    }
}
