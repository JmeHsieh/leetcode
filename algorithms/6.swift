// https://leetcode.com/problems/zigzag-conversion

class Solution {
    func convert(s: String, _ numRows: Int) -> String {
        guard s.characters.count > numRows && numRows > 1 else { return s }

        var s = Array(s.characters).map { String($0) }
        var result = [String](count: numRows, repeatedValue:"")
        result[0] = s[0]
        var idx_r = 1
        var idx_s = 1
        var direction = 1
        while idx_s < s.count {
            result[idx_r] += s[idx_s]
            if idx_r == 0 || idx_r == (numRows - 1) { direction = -direction }
            idx_r += direction
            idx_s += 1
        }
        return result.reduce("", combine: (+))
    }
}
