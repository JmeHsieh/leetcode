// https://leetcode.com/problems/word-pattern

class Solution {
    func wordPattern(pattern: String, _ str: String) -> Bool {
        let p = Array(pattern.characters).map { String($0) }
        let s = str.characters.split { $0 == " " }.map(String.init)
        var pMap = [String: Int]()
        var sMap = [String: Int]()
        if p.count != s.count { return false }

        for i in 0..<p.count {

            // both not seen
            if !pMap.keys.contains(p[i]) && !sMap.keys.contains(s[i]) {
                pMap[p[i]] = i
                sMap[s[i]] = i
                continue
            }

            // both seen
            if let p_i = pMap[p[i]], let s_i = sMap[s[i]] {
                if p_i != s_i { return false }
                pMap[p[i]] = i
                sMap[s[i]] = i
                continue
            }

            // one seen, one not
            return false
        }

        return true
    }
}
