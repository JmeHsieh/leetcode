// https://leetcode.com/problems/length-of-last-word

class Solution {
    func lengthOfLastWord(s: String) -> Int {
        let ss = s.characters.split { $0 == " " }.map(String.init)
        return ss.last?.characters.count ?? 0
    }
}
