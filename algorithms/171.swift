// https://leetcode.com/problems/excel-sheet-column-number

class Solution {
    func titleToNumber(s: String) -> Int {

        // build map
        let letters = Array("ABCDEFGHIJKLMNOPQRSTUVWXYZ".characters)
        var map: [Character: Int] = [:]
        for i in 0..<letters.count {
            map[letters[i]] = i+1
        }

        // calculate
        var sum = 0
        let cs = Array(s.characters)
        for i in 0..<cs.count {
            sum = sum*26 + map[cs[i]]!
        }

        return sum
    }
}
