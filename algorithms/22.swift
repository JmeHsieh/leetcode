// https://leetcode.com/problems/generate-parentheses

class Solution {
    func generateParenthesis(n: Int) -> [String] {
        var queue = [("", 0, n, n)]
        var result = [String]()

        while queue.count > 0 {
            var (s, w, lpq, rpq) = queue.removeFirst()
            s += "("
            w += 1
            lpq -= 1

            if lpq == 0 || rpq == 0 {
                let s_ = s + String(count: rpq, repeatedValue: ")" as Character)
                result.append(s_)
            } else {
                for r in 0...rpq {
                    if w-r >= 0 {
                        let s_ = s + String(count: r, repeatedValue: ")" as Character)
                        queue.append((s_, w-r, lpq, rpq-r))
                    }
                }
            }
        }

        return result
    }
}
