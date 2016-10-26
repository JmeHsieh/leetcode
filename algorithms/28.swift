// https://leetcode.com/problems/implement-strstr

class Solution {
    func strStr(haystack: String, _ needle: String) -> Int {
        let ln = needle.characters.count
        let lh = haystack.characters.count
        guard lh >= ln else { return -1 }

        for i in 0..<(lh-ln+1) {
            let r = haystack.startIndex.advancedBy(i)..<haystack.startIndex.advancedBy(i+ln)
            if haystack.substringWithRange(r) == needle { return i }
        }
        return -1
    }
}
