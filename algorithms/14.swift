// https://leetcode.com/problems/longest-common-prefix

class Solution {
    func longestCommonPrefix(strs: [String]) -> String {
        guard strs.count > 0 else { return "" }

        let minStrLength = strs.map { $0.characters.count }.reduce(Int.max, combine: min)
        for i in 0..<minStrLength {
            if Set(strs.map { $0.characters[$0.characters.startIndex.advancedBy(i)] }).count > 1 {
                return strs[0].substringToIndex(strs[0].characters.startIndex.advancedBy(i))
            }
        }
        return strs[0].substringToIndex(strs[0].characters.startIndex.advancedBy(minStrLength))
    }
}
