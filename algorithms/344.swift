// https://leetcode.com/problems/reverse-string

class Solution {
    func reverseString(s: String) -> String {
        let s_ = [Character](s.characters)
        var result = [Character]()
        for i in (s_.count-1).stride(through: 0, by: -1) {
            result.append(s_[i])
        }
        return String(result)
    }
}
