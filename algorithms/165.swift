// https://leetcode.com/problems/compare-version-numbers

class Solution {
    func compareVersion(version1: String, _ version2: String) -> Int {
        let v1 = version1.componentsSeparatedByString(".").map { Int($0) }
        let v2 = version2.componentsSeparatedByString(".").map { Int($0) }
        for i in 0..<max(v1.count, v2.count) {
            let i1 = (i < v1.count) ? v1[i] : 0
            let i2 = (i < v2.count) ? v2[i] : 0
            if i1 > i2 { return 1 }
            else if i1 < i2 { return -1 }
        }
        return 0
    }
}
