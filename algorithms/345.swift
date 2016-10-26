// https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution {
    func reverseVowels(s: String) -> String {
        let v = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        var s_ = Array(s.characters)
        var i = 0
        var j = s_.count-1
        while i < j {
            if !v.contains(String(s_[i])) {
                i += 1
                continue
            }
            if !v.contains(String(s_[j])) {
                j -= 1
                continue
            }
            let t = s_[i]
            s_[i] = s_[j]
            s_[j] = t
            i += 1
            j -= 1
        }
        return String(s_)
    }
}
