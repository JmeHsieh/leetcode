// https://leetcode.com/problems/rectangle-area

class Solution {
    func computeArea(A: Int, _ B: Int, _ C: Int, _ D: Int, _ E: Int, _ F: Int, _ G: Int, _ H: Int) -> Int {
        let r_abcd = (C-A) * (D-B)
        let r_efgh = (G-E) * (H-F)
        var r_overlapped = 0
        if C>E && G>A && H>B && D>F { r_overlapped = min(C-E, G-A, C-A, G-E) * min(H-B, D-F, D-B, H-F) }
        return r_abcd + r_efgh - r_overlapped
    }
}
