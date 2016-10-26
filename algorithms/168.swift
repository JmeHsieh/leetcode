// https://leetcode.com/problems/excel-sheet-column-title

class Solution {
    func convertToTitle(n: Int) -> String {
        let aScalars = "A".unicodeScalars
        let aCode = aScalars[aScalars.startIndex].value
        var n = n
        var result = [Int]()
        while n > 0 {
            n -= 1
            result.insert(n % 26, atIndex: 0)
            n /= 26
        }
        return String(result.map { Character(UnicodeScalar(aCode + UInt32($0))) })
    }
}
