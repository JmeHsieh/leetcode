// https://leetcode.com/problems/valid-parentheses

class Solution {
    func isValid(s: String) -> Bool {
        var stack = [String]()
        let dict = [")":"(", "]":"[", "}":"{"]
        for c in s.characters {
            let cs = String(c)
            if !dict.keys.contains(cs) {
                stack.append(cs)
            } else if stack.count == 0 || dict[cs] != stack.popLast() {
                return false
            }
        }
        return stack.count == 0
    }
}
