// https://leetcode.com/problems/valid-sudoku

class Solution {
    func isValidSudoku(board: [[Character]]) -> Bool {
        var M = [Int:[[Int]]]()
        for i in 0..<board.count {
            for j in 0..<board[i].count {
                let c = String(board[i][j])
                if c == "." { continue }

                let d = Int(c)!
                let g = i/3 * 3 + j/3
                if M.keys.contains(d) {
                    var rows = M[d]![0]
                    var cols = M[d]![1]
                    var groups = M[d]![2]
                    if rows.contains(i) || cols.contains(j) || groups.contains(g) { return false }
                    rows.append(i)
                    cols.append(j)
                    groups.append(g)
                    M[d] = [rows, cols, groups]
                } else {
                    M[d] = [[i], [j], [g]]
                }
            }
        }
        return true
    }
}
