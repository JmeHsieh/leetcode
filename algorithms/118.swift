// https://leetcode.com/problems/pascals-triangle

class Solution {
    func generate(numRows: Int) -> [[Int]] {
        var result = [[Int]]()
        for i in 0..<numRows {
            result.append([Int](count:i+1, repeatedValue:0))
            result[i][0] = 1
            result[i][result[i].endIndex-1] = 1

            // Can't form Range with end < start, so don't use 'for j in 1..<i {}'
            var j = 1
            while j < i {
                result[i][j] = result[i-1][j-1] + result[i-1][j]
                j += 1
            }
        }
        return result
    }
}
