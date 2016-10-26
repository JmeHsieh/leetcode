// https://leetcode.com/problems/string-to-integer-atoi/

class Solution {
    func myAtoi(str: String) -> Int {
        var s = str.characters.map { String($0) }

        // remove leading spaces
        while s.count > 0 && s[0] == " " {
            s.removeFirst()
        }

        guard s.count > 0 else { return 0 }

        // extract sign
        var positive = true
        if s[0] == "+" {
            positive = true
            s.removeFirst()
        } else if s[0] == "-" {
            positive = false
            s.removeFirst()
        }

        // converting while handling overflow
        var result = 0
        let digits = Set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        for i in 0..<s.count {
            if !digits.contains(s[i]) { break }

            if Int32.max/10 < Int32(result) || (Int32.max/10 == Int32(result) && Int32.max%10 < Int32(s[i])) {
                return positive ? Int(Int32.max) : Int(Int32.min)
            }

            result = result*10 + Int(s[i])!
        }

        return positive ? result : -result
    }
}
