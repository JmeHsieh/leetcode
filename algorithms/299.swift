// https://leetcode.com/problems/bulls-and-cows

class Solution {
    func getHint(secret: String, _ guess: String) -> String {
        var A = 0
        var B = 0
        var counter = [Int](count: 10, repeatedValue:0)
        var s_ = Array(secret.characters)
        var g_ = Array(guess.characters)
        for i in 0..<s_.count {
            let ds = Int(String(s_[i]))!
            let dg = Int(String(g_[i]))!
            if ds == dg {
                A += 1
            } else {
                counter[ds] += 1
                counter[dg] -=  1
                if counter[ds] <= 0 { B += 1 }
                if counter[dg] >= 0 { B += 1 }
            }
        }
        return "\(A)A\(B)B"
    }
}
