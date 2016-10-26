// https://leetcode.com/problems/counting-bits

class Solution {
    func countBits(num: Int) -> [Int] {
        var result = [0]
        while result.count < num+1 { result += result.map { $0 + 1 } }
        return Array(result[0...num])
    }
}
